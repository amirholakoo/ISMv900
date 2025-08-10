<script>
import { initFlowbite } from 'flowbite'
import Card from './Card'
import modal from "@/components/Modal.vue";
import Alert from "@/components/Alert.vue";
import Input from "@/components/custom/Input.vue";
import ModalButton from "@/components/custom/ModalButton.vue";

export default {
  name: "addSupplier",
  components: {
    ModalButton,
    Input,
    Alert,
    modal,
    Card
  },
  mounted() {
    initFlowbite();
  },
  data(){
    return{
      forms: {
        supplier_name: {type: 'input', name: 'نام و نام خانوادگی فروشنده/شرکت',title: 'نام و نام خانوادگی فروشنده/شرکت', data: '', value: '', lable:'text'},
        address: {type: 'input', name: 'آدرس',title: 'آدرس', data: '', value: '', lable:'text'},
        phone: {type: 'input', name: 'شماره همراه',title: 'شماره همراه', data: '', value: '', lable:'phone'},
        comment: {type: 'input', name: 'توضیحات',title: 'توضیحات', data: '', value: '', lable:'comment'},
        username: {type: 'input', name: 'نام کاربر',title: 'نام کاربر', data: '', value: '', lable:'text'},
      },
      success: false,
      error: false,
      errors: [],
    }
  },
  watch:{
    success(c, p){
      if (c == true) {
        setTimeout(() => {
          this.success = false
          location.reload();
        }, 5000)
      }
    },
  },
  methods: {
    async addSupplier() {
      const params = {
        "supplier_name": this.forms.supplier_name.value,
        "address": this.forms.address.value,
        "phone": this.forms.phone.value,
        "username": this.forms.username.value,
        "comments": this.forms.comment.value,
      };
      this.errors = []
      for (const key in this.forms) {
        if (this.forms[key].value == ''){
          if (key!='comment'){
            this.forms[key].error = true
          this.errors.push({'message': `${this.forms[key].name} مورد نیاز است`})
          }
        }else {
           this.forms[key].error = false
        }
      }
      if (this.errors.length == 0){
        this.error = false
        const response = await this.axios.post('/myapp/addSupplier/', {}, {params: params})
        console.log(response.data); // Access response data
        if (response.data['status'] == 'success'){
          this.success = true
        }else {
          this.error = true
          this.errors = response.data['errors']
          for (const responseElement of this.errors) {
                      console.log(responseElement)
          }
        }
      } else {
        this.error = true
      }
    }
  },
}
</script>

<template>
  <Card title="اضافه کردن فروشنده جدید">
    <form class="flex flex-col items-center mt-5 gap-4">
      <div v-if="error" class="flex p-4 mb-4 text-sm text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400" role="alert">
            <svg class="flex-shrink-0 inline w-4 h-4 me-3 mt-[2px]" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
              <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/>
            </svg>
            <span class="sr-only">Danger</span>
            <div>
              <span class="font-medium">خطا! لطفا اطلاعات را برسی کنید:</span>
                <ul class="mt-1.5 list-disc list-inside">
                  <li v-for="error in errors">{{ error.message }}</li>
              </ul>
            </div>
          </div>
      <div v-if="success" class="flex p-4 mb-4 text-sm text-green-800 rounded-lg bg-green-50 dark:bg-gray-800 dark:text-green-400" role="alert">
        <svg class="flex-shrink-0 inline w-4 h-4 me-3 mt-[2px]" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
          <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/>
        </svg>
        <div>
          <span class="font-medium">
            قروشنده جدید با نام {{ forms.supplier_name.value }} با موفقیت به سیستم اضافه شد.
            <template v-for="(val, key) in forms">
                <p v-if="key=='reel_numbers'">شماره رول:</p>
                <ul v-if="key=='reel_numbers'">
                  <li v-for="item in val.value" :key="item">{{ item }}</li>
                </ul>
                <p v-else>{{val.title}}: {{val.value}}</p>
            </template>
          </span>
        </div>
      </div>

      <template v-for="(val, form_name) in forms">
        <template v-if="val.type=='input'">
              <Input
                :formName="form_name"
                :label="val.name"
                :type="val.lable"
                :disabled="val.disabled"
                @update="val.value = $event"
                @InputError="error = $event"
              />
        </template>
      </template>
      <modal type="confirm" :disabled="error">
        <template v-slot:button>اضافه کردن</template>
        <template v-slot:text>
          <div class="flex flex-col gap-2 font-bold">
            <template v-for="(val, key) in forms">
                <p>{{val.title}}: {{val.value}}</p>
            </template>
          </div>
        </template>
        <template v-slot:btns>
          <div>
            <ModalButton @close="addSupplier" />
          </div>
        </template>
      </modal>
    </form>
  </Card>
</template>

<script>
import {initFlowbite} from "flowbite";
import modal from "@/components/Modal.vue";
import Alert from "@/components/Alert.vue";
import Card from "@/components/Card.vue";

export default {
  name: "addNewAnbar",
  components: {Card, Alert, modal},
  data(){
    return {
      forms: {
        location: {type: 'input', name: 'محل انبار',title: 'محل انبار', data: '', value: ''},
        username: {type: 'input', name: 'نام کاربر',title: 'نام کاربر', data: '', value: ''},
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
  methods:{
    async addNewAnbar() {
      const params = {
        'location': this.forms.location.value,
        'username': this.forms.username.value
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
        const response = await this.axios.post('/myapp/addNewAnbar/', {}, {params: params})
        console.log(response.data); // Access response data
        if (response.data['status'] == 'success'){
          this.success = true
        }else {
          this.error = true
          this.errors = response.data['errors']
        }
      } else {
        this.error = true
      }
    }
  },
}
</script>

<template>
  <Card title="افزودن انبار جدید">
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
            انبار جدید با نام {{ forms.location.value }} با موفقیت به سیستم اضافه شد.
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
          <div class="relative">
            <input v-model="val.value" type="text" :id="form_name" :class="[val.error ? 'text-red-900 border-red-500 focus:border-red-500' : 'text-gray-900 focus:border-green-500 border-gray-300']" class="block px-2.5 pb-2.5 pt-4 w-full text-sm  bg-transparent rounded-lg border-1 appearance-none focus:outline-none focus:ring-0 peer" placeholder="" />
            <label :for="form_name" :class="[val.error ? 'peer-focus:text-red-500 text-red-500' : 'peer-focus:text-green-500 text-gray-500']" class="absolute text-sm dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2  peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">
              {{val.name}}
            </label>
          </div>
        </template>
      </template>
      <modal type="confirm">
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
            <button data-modal-hide="popup-modal" aria-label="Close" @click="addNewAnbar" type="button" class="inline-flex justify-center w-full px-2 py-1.5 text-xs font-medium text-center text-white        bg-green-500 hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-green-300  rounded-lg dark:bg-blue-500 dark:hover:bg-blue-600 dark:focus:ring-blue-800">درسته</button>
          </div>
        </template>
      </modal>
    </form>
  </Card>
</template>

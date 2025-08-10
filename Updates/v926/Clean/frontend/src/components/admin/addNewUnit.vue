<script>
import {initFlowbite} from "flowbite";
import modal from "@/components/Modal.vue";
import Alert from "@/components/Alert.vue";
import Card from "@/components/Card.vue";
import Input from "@/components/custom/Input.vue";
import Dropdown from "@/components/custom/Dropdown.vue";
import ModalButton from "@/components/custom/ModalButton.vue";

export default {
  name: "addNewUnit",
  components: {ModalButton, Dropdown, Input, Card, Alert, modal},
  data(){
    return {
      forms: {
        supplier_name: {type: 'dropdown', name: 'فروشنده',title: 'فروشنده', data: '', value: ''},
        material_type: {type:'dropdown', name: 'جنس ماده جدید',title: 'جنس ماده جدید', data:'', value: ''},
        unit_name: {type:'input', name:'نام واحد', title:'نام واحد', value: ''},
        count: {type:'input', name: 'مفدار',title: 'مفدار', value: '', lable:'number'},
        username: {type:'input', name: 'نام کاربر',title: 'نام کاربر', value: ''},
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
  mounted() {
    initFlowbite();
    this.axios.get('/myapp/api/getSupplierNames').then((response) => {
      console.log(response.data)
      this.forms.supplier_name.data = response.data['supplier_names']
    })
  },
  methods:{
    clicked(k, name){
      console.log(k, name)
      if (k == 'supplier_name'){
        this.forms.supplier_name.name = name
        this.forms.supplier_name.value = name
        const params = {
          'supplier_name': this.forms.supplier_name.value
        }
        this.axios.get('/myapp/api/getMaterialTypes', {params:params}).then((response) => {
          console.log(response.data)
          this.forms.material_type.data = response.data['material_types']
        })
      }
      if (k == 'material_type'){
        this.forms.material_type.name = name
        this.forms.material_type.value = name
      }
    },
    async addNewUnit() {
      const params = {
        'supplier_name': this.forms.supplier_name.value,
        'material_type': this.forms.material_type.value,
        'unit_name': this.forms.unit_name.value,
        'count': parseInt(this.forms.count.value.replace(/,/g, '')),
        'username': this.forms.username.value,
      };
      this.errors = []
      for (const key in this.forms) {
        if (this.forms[key].value == ''){
          this.forms[key].error = true
          this.errors.push({'status': 'error', 'message': `${this.forms[key].name} مورد نیاز است`})
        }else {
           this.forms[key].error = false
        }
      }
      if (this.errors.length == 0){
        this.error = false
        const response = await this.axios.post('/myapp/addUnit/', {}, {params: params})
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
    },
  }
}
</script>

<template>
  <Card title="اضافه کردن واحد جدید">
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
            واحد جدید با نام {{ forms.unit_name.value }} با موفقیت به سیستم اضافه شد.
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
              :value="val.value"
              @InputError="error = $event"
            />
        </template>
        <template v-if="val.type=='dropdown'">
          <Dropdown :formName="form_name">
            <template v-slot:btnName>
              {{val.name}}
            </template>
            <template v-slot:list>
              <li v-for="(data, index) in val.data" :key="index">
                <a @click="clicked(form_name, data)" type="button" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">
                  {{ data }}
                </a>
              </li>
            </template>
          </Dropdown>
        </template>
      </template>
      <modal type="confirm" :disabled="error">
        <template v-slot:button>اضافه کردن</template>
        <template v-slot:text>
          <div class="flex flex-col gap-2 font-bold">
            <template v-for="(val, key) in forms">
                <p v-if="key=='reel_numbers'">شماره رول:</p>
                <ul v-if="key=='reel_numbers'">
                  <li v-for="item in val.value" :key="item">{{ item }}</li>
                </ul>
                <p v-else>{{val.title}}: {{val.value}}</p>
            </template>
          </div>
        </template>
        <template v-slot:btns>
          <div>
            <ModalButton @close="addNewUnit" />
          </div>
        </template>
      </modal>
    </form>
  </Card>
</template>
<script>
import {initFlowbite} from "flowbite";
import modal from "@/components/Modal.vue";
import Alert from "@/components/Alert.vue";
import Card from "@/components/Card.vue";

export default {
  name: "loaded",
  components: {Card, Alert, modal},
  data(){
    return {
      forms: {
        lic_number: {type: 'dropdown', name: 'شماره پلاک',title: 'شماره پلاک', data: '', value: ''},
        unloading_location: {type: 'dropdown', name: 'محل بار شده',title: 'محل تخلیه', data: '', value: ''},
        width: {type: 'dropdown', name: 'عرض',title: 'عرض', data: '', value: ''},
        reel_numbers: {type: 'check', name: 'عرض',title: 'عرض', data: '', value: []},
        forklift_driver: {type:'input', name: 'اسم راننده فرک لیفت',title: 'اسم راننده فرک لیفت', value: ''},
      },
      success: false,
      error: false,
      errors: [],
    }
  },
  mounted() {
    initFlowbite();
    this.axios.get('/myapp/api/getShipmentLicenseNumbersByStatus/LoadingUnloading').then((response) => {
      console.log(response.data)
      this.forms.lic_number.data = response.data['license_numbers']
    })
    this.axios.get('/myapp/api/getAnbarTableNames').then((response) => {
      console.log(response.data)
      this.forms.unloading_location.data = response.data['data']
    })
  },
  methods:{
    clicked(k, name){
      console.log(k, name)
      if (k == 'lic_number'){
        this.forms.lic_number.name = name
        this.forms.lic_number.value = name
      }
      if (k == 'unloading_location'){
        this.forms.unloading_location.name = name
        this.forms.unloading_location.value = name
        const params = {
          'anbar_location': this.forms.unloading_location.value
        }
        this.axios.get('/myapp/api/getWidths', {params:params}).then((response) => {
          console.log(response.data)
          this.forms.width.data = response.data['widths']
        })
      }
      if (k == 'width'){
        this.forms.width.value = name
        this.forms.width.name = name
        const params = {
          'anbar_location': this.forms.unloading_location.value,
          'width': this.forms.width.value,
        }
        this.axios.get('/myapp/api/getReelNumbersByWidthAndStatus', {params:params}).then((response) => {
          console.log(response.data)
          this.forms.reel_numbers.data = response.data['reel_numbers']
        })
      }
    },
    addReal(reel){
      const index = this.forms.reel_numbers.value.indexOf(reel);
      if (index >= 0) {
        this.forms.reel_numbers.value.splice(index, 1); // Remove the item if it's already checked
      } else {
        this.forms.reel_numbers.value.push(reel); // Add the item if it's not checked
      }
      console.log(this.forms.reel_numbers.value)
    },
    async addSupplier() {
      const params = {
        'lic_number': this.forms.lic_number.value,
        'loading_location': this.forms.unloading_location.value,
        'width': this.forms.width.value,
        'reel_numbers': JSON.stringify(Array.from(this.forms.reel_numbers.value)),
        'forklift_driver': this.forms.forklift_driver.value,
      };
      console.log(params)
      const response = await this.axios.post('/myapp/api/loaded', {}, {params: params})
      console.log(response.data); // Access response data
      if (response.data['status'] == 'success'){
        this.success = true
      }else {
        this.error = true
        this.errors = response.data['errors']
      }
    },
  }
}
</script>

<template>
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
      <template v-for="(val, form_name) in forms">
        <template v-if="val.type=='input'">
          <div class="relative">
            <input v-model="val.value" type="text" :id="form_name" class="block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder="" />
            <label :for="form_name" class="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">
              {{val.name}}
            </label>
          </div>
        </template>
        <template v-else-if="val.type=='check'">
          <h3 class="font-semibold text-gray-900 dark:text-white">شماره رول:</h3>
          <ul class="w-48 overflow-y-auto max-h-48 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg dark:bg-gray-700 dark:border-gray-600 dark:text-white">
            <li v-for="reel in val.data" :key="reel" class="w-full border-b border-gray-200 rounded-t-lg dark:border-gray-600">
              <div class="flex items-center ps-3">
                <input @click="addReal(reel)" :id="'vue-checkbox-' + reel" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500">
                <label :for="'vue-checkbox-' + reel" class="w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">{{ reel }}</label>
              </div>
            </li>
          </ul>
        </template>
        <template v-else>
          <button :id="form_name + 'Button'" :data-dropdown-toggle="form_name+'dropdown'" class="justify-between w-44 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">
            {{val.name}}
            <svg class="w-2.5 h-2.5 ms-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
            </svg>
          </button>
          <!-- Dropdown menu -->
          <div :id="form_name+'dropdown'" class="z-50 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700">
            <ul class="overflow-y-auto h-auto max-h-48 py-2 text-sm text-gray-700 dark:text-gray-200" :aria-labelledby="form_name + 'Button'">
              <li v-for="data in val.data">
                <a @click='clicked(form_name ,data)' type="button" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">
                  {{ data }}
                </a>
              </li>
            </ul>
        </div>
        </template>
      </template>
      <modal type="confirm">
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
            <button data-modal-hide="popup-modal" aria-label="Close" @click="addSupplier" type="button" class="inline-flex justify-center w-full px-2 py-1.5 text-xs font-medium text-center text-white bg-blue-600 rounded-lg hover:bg-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-500 dark:hover:bg-blue-600 dark:focus:ring-blue-800">درسته</button>
          </div>
        </template>
      </modal>
    <!--  <Alert v-if="success" type="Success">-->
    <!--    <template v-slot:SuccessContent>-->
    <!--      ماده حام  {{material_name}} - {{ material_type }} با موفقیت به دیتابیس اضافه شد.-->
    <!--    </template>-->
    <!--  </Alert>-->
</template>
<script>
import {initFlowbite} from "flowbite";
import modal from "@/components/Modal.vue";
import Alert from "@/components/Alert.vue";
import Card from "@/components/Card.vue";

export default {
  name: "purchase",
  components: {Card, Alert, modal},
  data(){
    return {
      forms: {
        lic_number: {type: 'dropdown', name: 'شماره پلاک',title: 'شماره پلاک', data: '', value: ''},
        supplier_name: {type:'input', name: 'اسم مشتری', value: ''},
        material_type: {type:'input', name: 'لیست رول ها', value: ''},
        material_name: {type:'input', name: 'لیست رول ها', value: ''},
        weight1: {type:'input', name: 'وزن 1', value: ''},
        weight2: {type:'input', name: 'وزن 2', value: ''},
        net_weight: {type:'input', name: 'وزن خالص', value: ''},
        unloaded_location: {type:'input', name: 'محل انبار', value: ''},
        unit: {type:'input', name: 'اسم پوفایل مصرفی', value: ''},
        quantity: {type:'input', name: 'قیمت هر کیلوگرم', value: ''},
        quality: {type: 'dropdown', name: 'مالیات بر ارزش افزوده',title: 'مالیات بر ارزش افزوده', data: '', value: ''},
        penalty: {type:'input', name: 'قمیت کل', value: ''},
        price_pre_kg: {type:'input', name: 'هزینه اضافی', value: ''},
        vat: {type: 'dropdown', name: 'وضعیت فاکتور',title: 'وضعیت فاکتور', data: '', value: ''},
        total_price: {type:'input', name: 'قمیت کل', value: ''},
        extra_cost: {type:'input', name: 'هزینه اضافی', value: ''},
        invoice_status: {type: 'dropdown', name: 'وضعیت فاکتور',title: 'وضعیت فاکتور', data: '', value: ''},
        supplier_invoice: {type:'input', name: 'شماره فاکتور', value: ''},
        payment_status:{type:'dropdown', name: 'وضعیت پرداخت',title: 'وضعیت پرداخت', data: '', value: ''},
        document_info: {type:'input', name: 'اظلاعات سند', value: ''},
        commnet: {type:'input', name: 'کامنت', value: ''},
        username: {type:'input', name: 'نام کاربری', value: ''},
      },
      success: false,
      error: false,
      errors: [],
    }
  },
  mounted() {
    initFlowbite();
    this.axios.get('/myapp/api/getLicenseNumbers').then((response) => {
      console.log(response.data)
      this.drowpdownList.lic_number.data = response.data['license_numbers']
    })
    this.axios.get('/myapp/api/getAnbarTableNames').then((response) => {
      console.log(response.data)
      this.drowpdownList.unloading_location.data = response.data['data']
    })
    this.axios.get('/myapp/api/getUnitNames').then((response) => {
      console.log(response.data)
      this.drowpdownList.unit.data = response.data['unit_names']
    })
  },
  methods:{
    clicked(k, name){
      console.log(k, name)
      if (k == 'lic_number'){
        this.drowpdownList.lic_number.name = name
        this.drowpdownList.lic_number.value = name
      }
      if (k == 'unloading_location'){
        this.drowpdownList.unloading_location.name = name
        this.drowpdownList.unloading_location.value = name
      }
      if (k == 'unit'){
        this.drowpdownList.unit.name = name
        this.drowpdownList.unit.value = name
      }
    },
    async addSupplier() {
      const params = {
        "license_number": this.drowpdownList.lic_number.value,
        "unloading_location": this.drowpdownList.unloading_location.value,
        "unit": this.drowpdownList.unit.value,
        "quantity": this.forms.Quantity.value,
        "quality": this.forms.Quality.value,
        "forklift_driver": this.forms.forklift_driver.value
      };
      const response = await this.axios.post('/myapp/api/unload', {}, {params: params})
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
  <Card title="ایجاد سفارش خرید">
    <div class="flex flex-col gap-2 justify-center items-center">
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
        <template v-else>
          <button :id="form_name + 'Button'" :data-dropdown-toggle="form_name+'dropdown'" class="justify-between w-44 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">
            {{val.name}}
            <svg class="w-2.5 h-2.5 ms-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
            </svg>
          </button>
          <!-- Dropdown menu -->
          <div :id="form_name+'dropdown'" class="z-50 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700">
            <ul class="overflow-y-auto h-48 py-2 text-sm text-gray-700 dark:text-gray-200" :aria-labelledby="form_name + 'Button'">
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
                <p>{{val.name}}: {{val.value}}</p>
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
    </div>
  </Card>
</template>
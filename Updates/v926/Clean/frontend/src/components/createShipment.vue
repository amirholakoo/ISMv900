<script>
import {initFlowbite, initDropdowns} from "flowbite";
import modal from "@/components/Modal.vue";
import Alert from "@/components/Alert.vue";
import Card from "@/components/Card.vue";
import Lic_numer from "@/components/lic_numer.vue";
import {LicenseNumberParser, parseLicenseNumber} from "@/components/lic_num_split";
import Input from "@/components/custom/Input.vue";
import Dropdown from "@/components/custom/Dropdown.vue";
import ModalButton from "@/components/custom/ModalButton.vue";

export default {
  name: "createShipment",
  components: {ModalButton, Dropdown, Input, Lic_numer, Card, Alert, modal},
  data(){
    return {
      forms: {
        lic_number: {status:true, type: 'dropdown', name: 'شماره پلاک',title: 'شماره پلاک', data: '', value: ''},
        shipmet_type: {
          status:true, 
          type: 'dropdown', 
          name: 'نوع بار نامه',
          title: 'نوع بار نامه', 
          data: [
            { display: 'ورودی', value: 'Incoming' },
            { display: 'خروجی', value: 'Outgoing' }
          ], 
          value: 'Incoming'
        },
        supplier_name: {status:true, type: 'dropdown', name: 'اسم فروشنده',title: 'اسم تامین کننده', data: '', value: ''},
        material_type: {status:true, type: 'dropdown', name: 'نوع ماده',title: 'نوع ماده', data: '', value: ''},
        material_name: {status:true, type: 'dropdown', name: 'اسم ماده',title: 'اسم ماده', data: '', value: ''},
        customer_name: {status:false, type: 'dropdown', name: 'اسم مشتری',title: 'اسم مشتری', data: '', value: ''},
        username: {status:true, type: 'input', name: 'نام کاربر',title:'نام کاربر', value: ''},
      },
      Incoming: true,
      success: false,
      error: false,
      errors: [],
      lic: ''
    }
  },
  watch:{
    success(c, p){
      if (c == true) {
        setTimeout(() => {
          this.success = false
          window.location.href = '/myapp/addShipment/';
        }, 5000)
      }
    },
  },
  mounted() {
    // console.log(this.$route.query.license_number)
    if (this.$route.query.license_number){
      this.forms.lic_number.name = this.$route.query.license_number
      this.forms.lic_number.value = this.$route.query.license_number
    }
    initFlowbite();
    this.axios.get('/myapp/api/getLicenseNumbers').then((response) => {
      console.log(response.data)
      this.forms.lic_number.data = response.data['free_truck']
    })
    this.axios.get('/myapp/api/getSupplierNames').then((response) => {
      console.log(response.data)
      this.forms.supplier_name.data = response.data['supplier_names']
    })

    this.axios.get('/myapp/api/getCustomerNames').then((response) => {
      console.log(response.data)
      this.forms.customer_name.data = response.data['customer_names']
      console.log(this.forms.customer_name.data)
    })
  },
  methods:{
    clicked(k, name){
      console.log(k, name)
      if (k == 'lic_number'){
        this.forms.lic_number.name = name
        this.forms.lic_number.value = name
      }
      if (k == 'supplier_name'){
        this.forms.supplier_name.name = name
        this.forms.supplier_name.value = name
        let params = {
          'supplier_name': name,
        }
        this.axios.get('/myapp/api/getMaterialTypes',{params: params}).then((response) => {
          console.log(response.data)
          this.forms.material_type.data = response.data['material_types']
        })
        this.axios.get('/myapp/api/getMaterialNames', { params: params }).then((response) => {
          console.log(response.data)
          this.forms.material_name.data = response.data['material_names']
        })
      }
      if (k == 'material_type'){
        this.forms.material_type.name = name
        this.forms.material_type.value = name
      }
      if (k == 'material_name'){
        this.forms.material_name.name = name
        this.forms.material_name.value = name
      }
      if (k == 'shipmet_type'){
        this.forms.shipmet_type.name = name
        this.forms.shipmet_type.value = name
        if (name=='Incoming'){
            this.forms.supplier_name.status = true
            this.forms.material_type.status = true
            this.forms.material_name.status = true
            this.forms.customer_name.status = false
            this.Incoming = true
        }else {
            this.forms.supplier_name.status = false
            this.forms.material_type.status = false
            this.forms.material_name.status = false
            this.forms.customer_name.status = true
            this.Incoming = false
        }
      }
      if (k == 'customer_name'){
        console.log(name)
        this.forms.customer_name.name = name
        this.forms.customer_name.value = name
      }
    },
    async addShipment() {
      const params = {
        "license_number": this.forms.lic_number.value,
        "supplier_name": this.forms.supplier_name.value,
        "material_type": this.forms.material_type.value,
        "material_name": this.forms.material_name.value,
        "shipment_type": this.forms.shipmet_type.value,
        "customer_name": this.forms.customer_name.value,
        "username": this.forms.username.value,
        "Incoming": this.Incoming,
      };
      this.errors = []; // Reset errors array


      // Additional checks for specific conditions
      if (this.forms.shipmet_type.value === "Incoming") { // Corrected property name
        if (this.forms.supplier_name.value === '') {
          this.errors.push({status: 'error', message: 'سام تامین کننده را انتخاب کنید'});
        }
        console.log('mat', this.forms.material_type.value)
        if (this.forms.material_type.value === '') {
          this.errors.push({status: 'error', message: 'نوع ماده را انتخاب کنید'});
        }
        if (this.forms.material_name.value === '') {
          this.errors.push({status: 'error', message: 'اسم ماده را انتخاب کنید'});
        }
      } else {
        if (this.forms.customer_name.value === '') {
          this.errors.push({status: 'error', message: 'اسم مشتری را انتخاب کنید'});
        }
      }

      // Check for username
      if (this.forms.username.value === '') {
        this.errors.push({status: 'error', message: 'نام کاربری را وارد کنید'});
      }

      if (this.errors.length == 0){
        console.log('no error')
        this.error = false
        console.log(this.errors)
        const response = await this.axios.post('/myapp/addShipment/', {}, {params: params})
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
  },
}
</script>

<template>
   <Card title="افزودن بارنامه">
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
      <div v-if="success" class="flex p-4 mb-4 text-sm text-green-800 rounded-lg bg-green-50 dark:bg-gray-800 dark:text-green-400" role="alert">
        <svg class="flex-shrink-0 inline w-4 h-4 me-3 mt-[2px]" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
          <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/>
        </svg>
        <div>
          <span class="font-medium">
            بارنامه جدید با موفقیت به سیستم اضافه شد.
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
        <template v-if="val.type=='dropdown'">
            <button :id="form_name + 'Button'" :data-dropdown-toggle="form_name+'dropdown'" :class="[val.status ? '': 'hidden']" class="justify-between w-44 text-white bg-green-500 hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">
              {{val.name}}
              <svg class="w-2.5 h-2.5 ms-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
              </svg>
            </button>
            <!-- Dropdown menu -->
            <div :id="form_name+'dropdown'" class="w-44 z-50 hidden bg-white divide-y divide-gray-100 rounded-lg shadow dark:bg-gray-700">
              <ul class="overflow-y-auto h-auto max-h-48 py-2 text-sm text-gray-700 dark:text-gray-200" :aria-labelledby="form_name + 'Button'">
                <li v-for="data in val.data">
                  <a @click='clicked(form_name, data.value || data)' type="button" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">
                    {{ data.display || data }}
                  </a>
                </li>
              </ul>
          </div>
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
            <ModalButton @close="addShipment" />
          </div>
        </template>
      </modal>
    </div>
   </Card>
</template>
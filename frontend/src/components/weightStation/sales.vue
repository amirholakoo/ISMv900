<script>
import {initFlowbite} from "flowbite";
import modal from "@/components/Modal.vue";
import Alert from "@/components/Alert.vue";
import Card from "@/components/Card.vue";
import ModalButton from "@/components/custom/ModalButton.vue";
import Input from "@/components/custom/Input.vue";
import Dropdown from "@/components/custom/Dropdown.vue";

export default {
  name: "sales",
  components: {Dropdown, Input, ModalButton, Card, Alert, modal},
  data(){
    return {
      forms: {
        lic_number: {type: 'dropdown', name: 'شماره پلاک',title: 'شماره پلاک', data: '', value: ''},
        customer_name: {type:'input', name: 'اسم مشتری',title: 'اسم مشتری', value: '', disabled:true},
        list_of_reels: {type:'list', name: 'لیست رول ها',title: 'لیست رول ها', value: '', disabled:true},
        weight1: {type:'input', name: 'وزن 1',title: 'وزن 1', value: '', disabled:true, lable:'number'},
        weight2: {type:'input', name: 'وزن 2',title: 'وزن 2', value: '', disabled:true, lable:'number'},
        net_weight: {type:'input', name: 'وزن خالص', title: 'وزن خالص', value: '', disabled:true, lable:'number'},
        loading_location: {type:'input', name: 'محل بار شده',title: 'محل بار شده', value: '', disabled:true},
        consuption_profile_name: {type:'input', name: 'اسم پوفایل مصرفی',title: 'اسم پوفایل مصرفی', value: '', disabled:true},
        price_pre_kg: {type:'input', name: 'قیمت هر کیلوگرم', title: 'قیمت هر کیلوگرم', value: '', numbertype:true, lable:'number'},
        vat: {type: 'dropdown', name: 'مالیات بر ارزش افزوده',title: 'مالیات بر ارزش افزوده', data: ['0%', '1%', '2%', '3%', '4%', '5%', '6%', '7%', '8%', '9%', '10%'], value: '0'},
        total_price: {type:'input', name: 'قمیت کل',title: 'قمیت کل', value: '', disabled:true, lable:'number'},
        extra_cost: {type:'input', name: 'هزینه اضافی',title: 'هزینه اضافی', value: '', numbertype:true, lable:'number'},
        invoice_status: {type: 'dropdown', name: 'وضعیت فاکتور',title: 'وضعیت فاکتور', data: ['Sent', 'NA'], value: ''},
        invoice_number: {type:'input', name: 'شماره فاکتور', title: 'شماره فاکتور', value: '', lable:'number'},
        payment_status:{type:'dropdown', name: 'وضعیت پرداخت',title: 'وضعیت پرداخت', data: ['Terms', 'Paid'], value: ''},
        document_info: {type:'input', name: 'اظلاعات سند',title: 'اظلاعات سند', value: ''},
        commnet: {type:'input', name: 'توضیحات',title: 'توضیحات', value: '', lable:'comment'},
        username: {type:'input', name: 'نام کاربر',title: 'نام کاربر', value: ''},
      },
      success: false,
      error: false,
      errors: [],
    }
  },
  computed:{
    formattedValue() {
      return this.formatNumber(this.inputValue);
    },
    total_price(){
      let vat = this.forms.vat.value;
      vat = parseInt(vat.replace('%', ''))
      let price = parseInt(this.forms.net_weight.value.replace(/,/g, '')) * parseInt(this.forms.price_pre_kg.value.replace(/,/g, ''))
      if (vat == 0 ){
        return price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
      } else {
         return (price+(price * (vat/100))).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
      }
    }
  },
  mounted() {
    initFlowbite();
    const params = {
      "status": 'Office',
      "location": 'Office',
      'shipment_type': 'Outgoing',
    }
    this.axios.post('/myapp/api/getShipmentLicenseNumbers', {}, {params: params}).then((response) => {
      console.log('lics:',response.data)
      this.forms.lic_number.data = response.data['license_numbers']
    })
  },
  watch: {
    success(c, p) {
      if (c == true) {
        setTimeout(() => {
          this.success = false
          location.reload();
        }, 5000)
      }
    },
  },
  methods:{
    formatNumber(value) {
      return value.replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    },
    formatInput() {
      this.forms.extra_cost.value = this.formatNumber(this.forms.extra_cost.value);
      this.forms.price_pre_kg.value = this.formatNumber(this.forms.price_pre_kg.value);
    },
    clicked(k, name){
      console.log(k, name)
      if (k == 'lic_number'){
        this.forms.lic_number.name = name
        this.forms.lic_number.value = name
        const params = {
          "license_number": this.forms.lic_number.value,
        }
        this.axios.post('/myapp/api/getShipmentDetails2ByLicenseNumber', {},{params:params}).then((response) => {
          console.log(response.data)
          this.forms.customer_name.value = response.data['customer_name']
          this.forms.list_of_reels.value = response.data['list_of_reels']
          this.forms.weight1.value = response.data['weight1'].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
          this.forms.weight2.value = response.data['weight2'].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
          this.forms.net_weight.value = response.data['net_weight'].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
          this.forms.loading_location.value = response.data['unloaded_location']
          this.forms.consuption_profile_name.value = response.data['consuption_profile_name']
        })
      }
      if (k == 'vat'){
        this.forms.vat.name = name
        this.forms.vat.value = name
        console.log(this.total_price)
        this.forms.total_price.value = this.total_price
        
      }
      if (k == 'invoice_status'){
        this.forms.invoice_status.name = name
        this.forms.invoice_status.value = name
      }
      if (k == 'payment_status'){
        this.forms.payment_status.name = name
        this.forms.payment_status.value = name
      }
    },
    async createsSales() {
      let vat = this.forms.vat.value;
      const params = {
        'lic_number': this.forms.lic_number.value,
        'customer_name': this.forms.customer_name.value,
        'list_of_reels': this.forms.list_of_reels.value,
        'weight1': parseInt(this.forms.weight1.value.replace(/,/g, '')),
        'weight2': parseInt(this.forms.weight2.value.replace(/,/g, '')),
        'net_weight': parseInt(this.forms.net_weight.value.replace(/,/g, '')),
        'loading_location': this.forms.loading_location.value,
        'consuption_profile_name': this.forms.consuption_profile_name.value,
        'price_pre_kg': this.forms.price_pre_kg.value.replace(/,/g, ''),
        'vat': parseInt(vat.replace('%', '')) ,
        'total_price': parseInt(this.forms.total_price.value.replace(/,/g, '')),
        'extra_cost': parseInt(this.forms.extra_cost.value.replace(/,/g, '')),
        'invoice_status': this.forms.invoice_status.value,
        'invoice_number': parseInt(this.forms.invoice_number.value.replace(/,/g, '')),
        'payment_status': this.forms.payment_status.value,
        'document_info': this.forms.document_info.value,
        'commnet': this.forms.commnet.value,
        'username': this.forms.username.value,
      };
      console.log(params)
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
        const response = await this.axios.post('/myapp/createSalesOrder/', {}, {params: params})
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
  <Card title="ایجاد سفارش فروش">
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
            مشتری جدید با نام {{ forms.customer_name.value }} با موفقیت به سیستم اضافه شد.
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
        <template v-if="val.type=='list'">
          <h3 class="font-semibold text-gray-900 dark:text-white">لیست شماره رول:</h3>
          <ul class="w-48 overflow-y-auto max-h-48 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg dark:bg-gray-700 dark:border-gray-600 dark:text-white">
            <li v-for="reel in val.value.split(',')" :key="reel" class="w-full p-2  border-b border-gray-200 rounded-t-lg dark:border-gray-600">
                {{ reel }}
            </li>
          </ul>
        </template>
<!--                <template v-if="val.type=='input'">-->
<!--          <div class="relative">-->
<!--            <template v-if="val.numbertype">-->
<!--              <input v-model="val.value" @input="formatInput" type="text" :id="form_name" :class="[val.error ? 'text-red-900 border-red-500 focus:border-red-500' : 'text-gray-900 focus:border-green-500 border-gray-300']" class="block px-2.5 pb-2.5 pt-4 w-full text-sm  bg-transparent rounded-lg border-1 appearance-none focus:outline-none focus:ring-0 peer" placeholder="" :disabled="val.disabled"/>-->
<!--            </template>-->
<!--            <template v-else>-->
<!--              <input v-model="val.value" type="text" :id="form_name" :class="[val.error ? 'text-red-900 border-red-500 focus:border-red-500' : 'text-gray-900 focus:border-green-500 border-gray-300']" class="block px-2.5 pb-2.5 pt-4 w-full text-sm  bg-transparent rounded-lg border-1 appearance-none focus:outline-none focus:ring-0 peer" placeholder="" :disabled="val.disabled"/>-->
<!--            </template>-->
<!--            <label :for="form_name" :class="[val.error ? 'peer-focus:text-red-500 text-red-500' : 'peer-focus:text-green-500 text-gray-500']" class="absolute text-sm dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2  peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">-->
<!--              {{val.name}}-->
<!--            </label>-->
<!--          </div>-->
<!--        </template>-->
<!--        <template v-if="val.type=='dropdown'">-->
<!--          <button :id="form_name + 'Button'" :data-dropdown-toggle="form_name+'dropdown'" class="justify-between w-44 text-white bg-green-500 hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">-->
<!--            {{val.name}}-->
<!--            <svg class="w-2.5 h-2.5 ms-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">-->
<!--              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>-->
<!--            </svg>-->
<!--          </button>-->
<!--          &lt;!&ndash; Dropdown menu &ndash;&gt;-->
<!--          <div :id="form_name+'dropdown'" class="z-50 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700">-->
<!--            <ul class="overflow-y-auto h-auto max-h-48 py-2 text-sm text-gray-700 dark:text-gray-200" :aria-labelledby="form_name + 'Button'">-->
<!--              <li v-for="data in val.data">-->
<!--                <a @click='clicked(form_name ,data)' type="button" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">-->
<!--                  {{ data }}-->
<!--                </a>-->
<!--              </li>-->
<!--            </ul>-->
<!--        </div>-->
<!--        </template>-->
        <template v-if="val.type=='input'">
            <Input
              :formName="form_name"
              :label="val.name"
              :type="val.lable"
              :disabled="val.disabled"
              @update="val.value = $event"
              :value="val.value"
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
<!--            <button data-modal-hide="popup-modal" aria-label="Close" @click="createsSales" type="button" class="inline-flex justify-center w-full px-2 py-1.5 text-xs font-medium text-center text-white        bg-green-500 hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-green-300  rounded-lg dark:bg-blue-500 dark:hover:bg-blue-600 dark:focus:ring-blue-800">درسته</button>-->
            <ModalButton @close="createsSales"/>
          </div>
        </template>
      </modal>
    </form>
  </Card>
</template>
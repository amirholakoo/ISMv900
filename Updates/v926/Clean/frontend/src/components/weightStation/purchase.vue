<script>
import {initFlowbite} from "flowbite";
import modal from "@/components/Modal.vue";
import Alert from "@/components/Alert.vue";
import Card from "@/components/Card.vue";
import Input from "@/components/custom/Input.vue";
import Dropdown from "@/components/custom/Dropdown.vue";
import ModalButton from "@/components/custom/ModalButton.vue";

export default {
  name: "purchase",
  components: {ModalButton, Dropdown, Input, Card, Alert, modal},
  data(){
    return {
      forms: {
        lic_number: {type: 'dropdown', name: 'شماره پلاک',title: 'شماره پلاک', data: '', value: ''},
        supplier_name: {type:'input', name: 'اسم تامین کننده', title: 'اسم تامین کننده', value: '', disabled:true},
        material_type: {type:'input', name: 'نوع ماده',  title: 'نوع ماده', value: '', disabled:true},
        material_name: {type:'input', name: 'اسم ماده',  title: 'اسم ماده', value: '', disabled:true},
        weight1: {type:'input', name: 'وزن 1', title: 'وزن 1', value: '', disabled:true, lable:'number'},
        weight2: {type:'input', name: 'وزن 2', title: 'وزن 2', value: '', disabled:true, lable:'number'},
        net_weight: {type:'input', name: 'وزن خالص', title: 'وزن خالص', value: '', disabled:true, lable:'number'},
        adjusted_weight: {type:'input', name: 'وزن تنظیم شده', title: 'وزن تنظیم شده', value: '', lable:'number'},
        unloaded_location: {type:'input', name: 'محل تخلیه شده', title: 'محل تخلیه شده', value: '', disabled:true},
        unit: {type:'input', name: 'واحد',  title: 'واحد', value: '', disabled:true},
        quantity: {type:'input', name: 'مقدار', title: 'مقدار', value: '', disabled:true, lable:'number'},
        quality: {type: 'input', name: 'کیفیت',title: 'مالیات بر ارزش افزوده', value: '', disabled:true},
        penalty: {type:'input', name: 'جریمه', title: 'جریمه', value: '', numbertype:true, lable:''},
        price_pre_kg: {type:'input', name: 'قیمت تومان هر کیلوگرم', title: 'قیمت تومان هر کیلوگرم', value: '', numbertype:true, lable:'number'},
        vat: {type: 'dropdown', name: 'مالیات بر ارزش افزوده',title: 'مالیات بر ارزش افزوده', data: ['0%', '9%', '10%'], value: '0'},
        total_price: {type:'input', name: 'قمیت کل تومان', title: 'قمیت کل تومان', value: '', disabled:true, lable:'number'},
        extra_cost: {type:'input', name: 'هزینه اضافی تومان', title: 'هزینه اضافی تومان', value: '', numbertype:true, lable:'number'},
        invoice_status: {type: 'dropdown', name: 'وضعیت فاکتور',title: 'وضعیت فاکتور', data: ['Received', 'NA'], value: ''},
        supplier_invoice: {type:'input', name: 'شماره فاکتور تامین کننده', title: 'شماره فاکتور تامین کننده', value: '', lable:'number'},
        payment_status:{type:'dropdown', name: 'وضعیت پرداخت',title: 'وضعیت پرداخت', data: ['Terms', 'Paid'], value: ''},
        document_info: {type:'input', name: 'اظلاعات سند', title: 'اظلاعات سند', value: '', lable:''},
        commnet: {type:'input', name: 'توضیحات', title: 'توضیحات', value: '', lable:'comment'},
        username: {type:'input', name: 'نام کاربر', title: 'نام کاربر', value: ''},
      },
      success: false,
      error: false,
      errors: [],
      originalNetWeight: '', // Store original net weight for logging
      weightAdjustmentMessage: '', // Store weight adjustment message for alert
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
    'forms.adjusted_weight.value': function(newVal) {
      if (newVal) {
        // Store original weight before updating
        const originalWeight = this.forms.net_weight.value;
        
        // Update net weight
        this.forms.net_weight.value = newVal;
        
        // Create adjustment message
        this.weightAdjustmentMessage = `${this.forms.username.value} changed net weight from ${originalWeight} to ${newVal}`;
        
        // Log the change
        const params = {
          "username": this.forms.username.value,
          "license_number": this.forms.lic_number.value,
          "original_weight": originalWeight,
          "adjusted_weight": newVal,
          "action": "weight_adjustment"
        }
        this.axios.post('/myapp/api/logWeightAdjustment', {}, {params: params}).then((response) => {
          console.log('Weight adjustment logged:', response.data);
        }).catch((error) => {
          console.error('Error logging weight adjustment:', error);
        });
      }
    }
  },
  computed:{
    formattedValue() {
      return this.formatNumber(this.inputValue);
    },
    total_price(){
      let vat = this.forms.vat.value;
      vat = parseInt(vat.replace('%', ''))
      // Use net_weight directly since adjusted_weight will update it
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
       'shipment_type': 'Incoming',
    }
    this.axios.post('/myapp/api/getShipmentLicenseNumbers', {}, {params: params}).then((response) => {
      console.log('lics:',response.data)
      this.forms.lic_number.data = response.data['license_numbers']
    })
  },
  methods:{
    formatNumber(value) {
      return value.replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    },
    formatInput() {
      // this.forms.penalty.value = this.formatNumber(this.forms.penalty.value);
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
        this.axios.post('/myapp/api/getShipmentDetailsByLicenseNumber', {},{params:params}).then((response) => {
          console.log(response.data)
          this.forms.supplier_name.value = response.data['supplier_name']
          this.forms.material_type.value = response.data['material_type']
          this.forms.material_name.value = response.data['material_name']
          this.forms.weight1.value = response.data['weight1'].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
          this.forms.weight2.value = response.data['weight2'].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
          this.forms.net_weight.value = response.data['net_weight'].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
          this.forms.unloaded_location.value = response.data['unload_location']
          this.forms.unit.value = response.data['unit']
          this.forms.quantity.value = response.data['quantity'].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
          this.forms.quality.value = response.data['quality'].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
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
    async createPurchase() {
      let vat = this.forms.vat.value;
      const params = {
        'license_number': this.forms.lic_number.value,
        'supplier_name': this.forms.supplier_name.value,
        'material_type': this.forms.material_type.value,
        'material_name': this.forms.material_name.value,
        'weight1': parseInt(this.forms.weight1.value.replace(/,/g, '')),
        'weight2': parseInt(this.forms.weight2.value.replace(/,/g, '')),
        'net_weight': parseInt(this.forms.net_weight.value.replace(/,/g, '')),
        'adjusted_weight': parseInt(this.forms.adjusted_weight.value.replace(/,/g, '')),
        'unloaded_location': this.forms.unloaded_location.value,
        'unit': this.forms.unit.value,
        'quantity': parseInt(this.forms.quantity.value.replace(/,/g, '')),
        'quality': parseInt(this.forms.quality.value.replace(/,/g, '')),
        'penalty': parseInt(this.forms.penalty.value.replace(/,/g, '')),
        'price_pre_kg': parseInt(this.forms.price_pre_kg.value.replace(/,/g, '')),
        'vat': parseInt(vat.replace('%', '')) ,
        'total_price': parseInt(this.forms.total_price.value.replace(/,/g, '')),
        'extra_cost': parseInt(this.forms.extra_cost.value.replace(/,/g, '')),
        'invoice_status': this.forms.invoice_status.value,
        'supplier_invoice': parseInt(this.forms.supplier_invoice.value.replace(/,/g, '')),
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
        const response = await this.axios.post('/myapp/createPurchaseOrder/', {}, {params: params})
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
  <Card title="ایجاد سفارش خرید">
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
             با موفقیت به سیستم اضافه شد.
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
            <template v-if="weightAdjustmentMessage" class="mb-4">
              <Alert type="warning" :message="weightAdjustmentMessage"/>
            </template>
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
<!--            <button data-modal-hide="popup-modal" aria-label="Close" @click="createPurchase" type="button" class="inline-flex justify-center w-full px-2 py-1.5 text-xs font-medium text-center text-white        bg-green-500 hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-green-300  rounded-lg dark:bg-blue-500 dark:hover:bg-blue-600 dark:focus:ring-blue-800">درسته</button>-->
            <ModalButton @close="createPurchase"/>
          </div>
        </template>
      </modal>
    </form>
  </Card>
</template>
<script>
import { initFlowbite } from 'flowbite'
import Card from './Card'
import Alert from "@/components/Alert.vue";
import modal from "@/components/Modal.vue";
import QRCode from 'qrcode';

export default {
  name: "addNewReel",
  components: {
    modal,
    Alert,
    Card,
  },
  data(){
    return{
      qrcode: '',
      hide: false,
      reel_number: '',
      width: '',
      GSM: '',
      length: '',
      breaks: '',
      grade: '',
      consumption_profile_name: '',
      success: false,
      error: false,
      errors: [],
      consumption_profile_names: '',
    }
  },
  mounted() {
    initFlowbite();
    this.axios.get('/myapp/api/getConsumptionProfileNames').then((response) => {
      console.log(response.data)

        this.consumption_profile_names = response.data['profile_names']

    })
  },
  methods: {
    async addSupplier() {
      const params = {
        "reel_number": this.reel_number,
        "width": this.width,
        "gsm": this.GSM,
        "length": this.length,
        "breaks": this.breaks,
        "grade": this.grade,
        "consumption_profile_name": this.consumption_profile_name,
      };

      const response = await this.axios.post('/myapp/addNewReel/', {}, {params: params})
      console.log(response.data); // Access response data
      if (response.data['status'] == 'success'){
        this.success = true
        this.qrcode = await QRCode.toDataURL(JSON.stringify(params), {
          width: 256,
          height: 256,
        })
      }else {
        this.error = true
        this.errors = response.data['errors']
      }
    },
    async printQRCode() {

      const printWindow = window.open('', '_blank');
      printWindow.document.write('<html><head><title>چاپ QR-code</title></head><body>');
      printWindow.document.write('<img src="' + this.qrcode + '" />');
      printWindow.document.write('</body></html>');
      printWindow.print();
      printWindow.documents.close();
    },
    consumption_profile_name_clicked(name){
      this.consumption_profile_name = name
    },
  },
}
</script>

<template>
  <Card title="اضافه کردن رول جدید" bgTitle="bg-rose-200">
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
    <div class="relative">
      <input v-model="reel_number" type="text" id="reel_number" class="block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder="" />
      <label for="reel_number" class="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">شماره رول</label>
    </div>
    <div class="relative">
      <input v-model="width" type="text" id="width" class="block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder="" />
      <label for="width" class="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">عرض</label>
    </div>
    <div class="relative">
      <input v-model="GSM" type="text" id="GSM" class="block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder="" />
      <label for="GSM" class="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">گراماژ</label>
    </div>
    <div class="relative">
      <input v-model="length" type="text" id="length" class="block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder="" />
      <label for="length" class="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">طول</label>
    </div>
    <div class="relative">
      <input v-model="breaks" type="text" id="breaks" class="block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder="" />
      <label for="breaks" class="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">پارگی</label>
    </div>
    <div class="relative">
      <input v-model="grade" type="text" id="grade" class="block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder="" />
      <label for="grade" class="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">نمره</label>
    </div>
    <button id="consumption_profile_name_Button"
      data-dropdown-toggle="consumption_profile_name_Dropdown"
      class="justify-between w-44 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">
      نام پروفایل مصرفی
      <svg class="w-2.5 h-2.5 ms-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
      <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
      </svg>
    </button>
    <!--consumption_profile_name Dropdown menu -->
    <div id="consumption_profile_name_Dropdown" class="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700">
        <ul class="overflow-y-auto h-auto max-h-48 py-2 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="consumption_profile_name_Button">
          <li v-for="name in consumption_profile_names" @click="consumption_profile_name_clicked(name)">
            <a type="button" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">
              {{ name }}
            </a>
          </li>
        </ul>
    </div>
    <modal type="confirm">
        <template v-slot:button>اضافه کردن</template>
        <template v-slot:text>
          <div class="flex flex-col gap-2 font-bold">
            <p>شماره رول: {{ reel_number }}</p>
            <p>عرض: {{ width }}</p>
            <p>گراماژ: {{ GSM }}</p>
            <p>طول: {{ length }}</p>
            <p>پارگی: {{ breaks }}</p>
            <p>نمره: {{ grade }}</p>
            <p>پروفایل مصرفی: {{ consumption_profile_name }}</p>
          </div>
        </template>
        <template v-slot:btns>
          <div>
            <button data-modal-hide="popup-modal" aria-label="Close" @click="addSupplier" type="button" class="inline-flex justify-center w-full px-2 py-1.5 text-xs font-medium text-center text-white bg-blue-600 rounded-lg hover:bg-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-500 dark:hover:bg-blue-600 dark:focus:ring-blue-800">درسته</button>
          </div>
        </template>
    </modal>

  <div v-if="success" :class="{'hidden': hide}" class="backdrop-blur-sm bg-white/30 flex fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
    <div class="relative p-4 w-full max-w-md max-h-full">
      <div  id="alert-3" class="flex flex-col gap-4 p-4 mb-4 text-green-800 rounded-lg bg-green-50 dark:bg-gray-800 dark:text-green-400" role="alert">
          <header class="flex felx-row justify-between items-center">
            <svg class="flex-shrink-0 w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
            <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/>
          </svg>
            <h class="ms-3 text-sm font-medium">مشتری جدید با نام {{ customer_name }} با موفقیت به دیتابیس اضافه</h>
            <button @click="hide=!hide" type="reset" class="ms-auto -mx-1.5 -my-1.5 bg-green-50 text-green-500 rounded-lg focus:ring-2 focus:ring-green-400 p-1.5 hover:bg-green-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-green-400 dark:hover:bg-gray-700">
            <span class="sr-only">Close</span>
            <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
            </svg>
          </button>
          </header>
          <main class="flex flex-col justify-center items-center gap-2">
            <img :src="qrcode" class="w-[256px] h-[256px]"/>
            <button @click="printQRCode" type="button" class="inline-flex justify-center w-full px-2 py-1.5 text-xs font-medium text-center text-white bg-blue-600 rounded-lg hover:bg-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-500 dark:hover:bg-blue-600 dark:focus:ring-blue-800">چاپ QR Code</button>
          </main>
        </div>
    </div>
  </div>
  </form>
  </Card>
</template>

<!--<script>-->
<!--import {initFlowbite} from "flowbite";-->
<!--import modal from "@/components/Modal.vue";-->
<!--import Alert from "@/components/Alert.vue";-->
<!--import Card from "@/components/Card.vue";-->
<!--import QRCode from "qrcode";-->

<!--export default {-->
<!--  name: "addNewReel",-->
<!--  components: {Card, Alert, modal},-->
<!--  data(){-->
<!--    return {-->
<!--      forms: {-->
<!--        reel_number:{type:'input', name: 'شماره رول', title:'شماره رول', data:'', value:''},-->
<!--        width:{type:'input', name: 'عرض', title:'عرض', data:'', value:''},-->
<!--        GSM:{type:'input', name: 'گراماژ', title:'گراماژ', data:'', value:''},-->
<!--        length:{type:'input', name: 'طول', title:'طول', data:'', value:''},-->
<!--        breaks:{type:'input', name: 'پارگی', title:'پارگی', data:'', value:''},-->
<!--        grade:{type:'input', name: 'نمره', title:'', data:'نمره', value:''},-->
<!--        consumption_profile_name:{type:'dropdown', name: 'پروفایل مصرفی', title:'پروفایل مصرفی', data:'', value:''},-->
<!--      },-->
<!--      success: false,-->
<!--      error: false,-->
<!--      errors: [],-->
<!--      qrcode: '',-->
<!--      hide: false,-->
<!--    }-->
<!--  },-->
<!--  mounted() {-->
<!--    initFlowbite();-->
<!--    this.axios.get('/myapp/api/getConsumptionProfileNames').then((response) => {-->
<!--      console.log(response.data)-->
<!--      this.forms.consumption_profile_name.data = response.data['profile_names']-->
<!--    })-->
<!--  },-->
<!--  methods:{-->
<!--    clicked(k, name){-->
<!--      console.log(k, name)-->
<!--      if (k == 'consumption_profile_name'){-->
<!--        this.forms.consumption_profile_name.name = name-->
<!--        this.forms.consumption_profile_name.value = name-->
<!--      }-->
<!--    },-->
<!--    async addSupplier() {-->
<!--      const params = {-->
<!--        "reel_number": this.reel_number,-->
<!--        "width": this.width,-->
<!--        "gsm": this.GSM,-->
<!--        "length": this.length,-->
<!--        "breaks": this.breaks,-->
<!--        "grade": this.grade,-->
<!--        "consumption_profile_name": this.consumption_profile_name,-->
<!--      };-->
<!--      const response = await this.axios.post('/myapp/addNewReel/', {}, {params: params})-->
<!--      console.log(response.data); // Access response data-->
<!--      if (response.data['status'] == 'success'){-->
<!--        this.success = true-->
<!--        this.qrcode = await QRCode.toDataURL(JSON.stringify(params), {-->
<!--          width: 256,-->
<!--          height: 256,-->
<!--        })-->
<!--      }else {-->
<!--        this.error = true-->
<!--        this.errors = response.data['errors']-->
<!--      }-->
<!--    },-->
<!--    async printQRCode() {-->

<!--      const printWindow = window.open('', '_blank');-->
<!--      printWindow.document.write('<html><head><title>چاپ QR-code</title></head><body>');-->
<!--      printWindow.document.write('<img src="' + this.qrcode + '" />');-->
<!--      printWindow.document.write('</body></html>');-->
<!--      printWindow.print();-->
<!--      printWindow.documents.close();-->
<!--    },-->
<!--  }-->
<!--}-->
<!--</script>-->

<!--<template>-->
<!--  <Card title="اضافه کردن رول جدید">-->
<!--    <div class="flex flex-col gap-2 justify-center items-center">-->
<!--      <div v-if="error" class="flex p-4 mb-4 text-sm text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400" role="alert">-->
<!--            <svg class="flex-shrink-0 inline w-4 h-4 me-3 mt-[2px]" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">-->
<!--              <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/>-->
<!--            </svg>-->
<!--            <span class="sr-only">Danger</span>-->
<!--            <div>-->
<!--              <span class="font-medium">خطا! لطفا اطلاعات را برسی کنید:</span>-->
<!--                <ul class="mt-1.5 list-disc list-inside">-->
<!--                  <li v-for="error in errors">{{ error.message }}</li>-->
<!--              </ul>-->
<!--            </div>-->
<!--          </div>-->
<!--      <template v-for="(val, form_name) in forms">-->
<!--        <template v-if="val.type=='input'">-->
<!--          <div class="relative">-->
<!--            <input v-model="val.value" type="text" :id="form_name" class="block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder="" />-->
<!--            <label :for="form_name" class="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">-->
<!--              {{val.name}}-->
<!--            </label>-->
<!--          </div>-->
<!--        </template>-->
<!--        <template v-else>-->
<!--          <button :id="form_name + 'Button'" :data-dropdown-toggle="form_name+'dropdown'" class="justify-between w-44 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">-->
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
<!--      </template>-->
<!--      <modal type="confirm">-->
<!--        <template v-slot:button>اضافه کردن</template>-->
<!--        <template v-slot:text>-->
<!--          <div class="flex flex-col gap-2 font-bold">-->
<!--            <template v-for="(val, key) in forms">-->
<!--                <p>{{val.name}}: {{val.value}}</p>-->
<!--            </template>-->
<!--          </div>-->
<!--        </template>-->
<!--        <template v-slot:btns>-->
<!--          <div>-->
<!--            <button data-modal-hide="popup-modal" aria-label="Close" @click="addSupplier" type="button" class="inline-flex justify-center w-full px-2 py-1.5 text-xs font-medium text-center text-white bg-blue-600 rounded-lg hover:bg-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-500 dark:hover:bg-blue-600 dark:focus:ring-blue-800">درسته</button>-->
<!--          </div>-->
<!--        </template>-->
<!--      </modal>-->
<!--      <div v-if="success" :class="{'hidden': hide}" class="backdrop-blur-sm bg-white/30 flex fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">-->
<!--    <div class="relative p-4 w-full max-w-md max-h-full">-->
<!--      <div  id="alert-3" class="flex flex-col gap-4 p-4 mb-4 text-green-800 rounded-lg bg-green-50 dark:bg-gray-800 dark:text-green-400" role="alert">-->
<!--          <header class="flex felx-row justify-between items-center">-->
<!--            <svg class="flex-shrink-0 w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">-->
<!--            <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/>-->
<!--          </svg>-->
<!--            <h class="ms-3 text-sm font-medium">مشتری جدید با نام {{ customer_name }} با موفقیت به دیتابیس اضافه</h>-->
<!--            <button @click="hide=!hide" type="reset" class="ms-auto -mx-1.5 -my-1.5 bg-green-50 text-green-500 rounded-lg focus:ring-2 focus:ring-green-400 p-1.5 hover:bg-green-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-green-400 dark:hover:bg-gray-700">-->
<!--            <span class="sr-only">Close</span>-->
<!--            <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">-->
<!--              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>-->
<!--            </svg>-->
<!--          </button>-->
<!--          </header>-->
<!--          <main class="flex flex-col justify-center items-center gap-2">-->
<!--            <img :src="qrcode" class="w-[256px] h-[256px]"/>-->
<!--            <button @click="printQRCode" type="button" class="inline-flex justify-center w-full px-2 py-1.5 text-xs font-medium text-center text-white bg-blue-600 rounded-lg hover:bg-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-500 dark:hover:bg-blue-600 dark:focus:ring-blue-800">چاپ QR Code</button>-->
<!--          </main>-->
<!--        </div>-->
<!--    </div>-->
<!--  </div>-->
<!--    </div>-->
<!--  </Card>-->
<!--</template>-->
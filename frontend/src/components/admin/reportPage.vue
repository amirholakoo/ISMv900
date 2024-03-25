<script>
import { initFlowbite } from 'flowbite'
import Card from '@/components/Card'
import modal from "@/components/Modal.vue";
import Alert from "@/components/Alert.vue";
import Lic_numer from "@/components/lic_numer.vue";
import { jsPDF } from "jspdf";
import html2canvas from 'html2canvas';

export default {
  name: "reportPage",
  components: {
    Lic_numer,
    Card,
    modal,
    Alert
  },
  data(){
    return {
      forms: {
        shipment_list: {
          type:'list',
          name: 'لیست بارنامه',
          title: 'لیست بارنامه',
          value: [],
          fields:[
             'شناسه',
             'نوع حمل و نقل',
             'وضعیت',
             'مکان',
             'شماره مجوز',
             'تاریخ دریافت',
             'زمان ورود',
             'نام مشتری',
             'نام تامین کننده',
             'وزن 1',
             'زمان وزن 1',
             'مکان بارگیری',
             'واحد',
             'تعداد',
             'کیفیت',
             'جریمه',
             'وزن 2',
             'زمان وزن 2',
             'وزن خالص',
             'لیست رل‌ها',
             'نام پروفایل',
             'شناسه فروش',
             'قیمت بر کیلوگرم',
             'هزینه اضافی',
             'نوع ماده',
             'نام ماده',
             'شناسه خرید',
             'مالیات',
             'وضعیت فاکتور',
             'وضعیت پرداخت',
             'زمان خروج',
             'اطلاعات مستند',
             'نظرات',
             'دلیل لغو',
             'نام کاربری',
             'لاگ‌ها'
            ]
        },
      },
      success: false,
      error: false,
      errors: [],
      countdownTime: 900000, // 15 milisecond
      timeLeft: 900000,
    }
  },
  computed: {
    formattedTime() {
      const minutes = Math.floor(this.timeLeft / 60000);
      const seconds = this.timeLeft % 60;
      return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    },
  },
  mounted() {
    this.load_data()
    this.startCountdown();
  },
  methods: {
    async generate_excel_report(model_name){
      console.log(model_name)
      const params = {
        'model_name':model_name,
      }
      const response = await this.axios.post('/myapp/api/generateExcelReport',{}, {params:params})
      console.log(response.data['data'])
    },
    reload(){location.reload();},
    startCountdown() {
      this.interval = setInterval(() => {
        this.timeLeft--;
        if (this.timeLeft <= 0) {
          clearInterval(this.interval);
          this.timeLeft = 0;
          location.reload();
        }
      }, 1000);
    },
    select(obj){
      this.forms.shipment_list.value = obj
    },
    clicked(k, name){
      console.log(k, name)
      if (k == 'letter'){
        this.letter.val = name
      }
      if (k == 'unloading_location'){
        this.forms.unloading_location.name = name
        this.forms.unloading_location.value = name
      }
    },
    async load_data() {
      const response = await this.axios.get('/myapp/api/loadReportData')
      console.log(response.data['data']); // Access response data
      // console.log(JSON.parse(response.data['isExists'])); // Access response data
      this.forms = response.data['data']
      // this.forms.shipment_list.data = response.data['data'].shipments.values
      // this.forms.shipment_list.fields = response.data['data'].shipments.fields
      // console.log(JSON.parse(response.data['shipment_list']))
    },
    printTable(id) {
        let table = document.getElementById(id); // Replace 'yourTableId' with your table's ID
        console.log(table)
        html2canvas(table).then(function(canvas) {
            let imgData = canvas.toDataURL('image/png');
            console.log(imgData)
            var doc = new jsPDF('p', 'mm', 'a4');
            var imgHeight = canvas.height * 210 / canvas.width;
            doc.addImage(imgData, 'PNG', 0, 0, 210, imgHeight);
            doc.save('table.pdf');
        });
    }
  },
}
</script>

<template>
<Card title="گزارش">
  <p class="flex flex-row gap-2 items-center">
    <button @click="reload" class="w-auto block text-white bg-green-500 hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">
      بارگیری مجدد
    </button>
    {{ formattedTime }}
  </p>
  <form class="flex flex-col items-center mt-5 gap-4">
    <template v-for="(val, form_name) in forms">
        <div class="relative w-full h-auto max-h-[500px] overflow-y-scroll overflow-x-auto shadow-md sm:rounded-lg">
            <table :id="form_name" class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                <caption class="p-5 text-lg font-semibold text-left rtl:text-right text-gray-900 bg-white dark:text-white dark:bg-gray-800">

                    <div class="flex flex-row gap-2 items-center">
                      {{val.title}}
                    <button @click="printTable(form_name)" class="w-auto block text-white bg-green-500 hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">
                      PDF
                    </button>
                    <button @click="generate_excel_report(form_name)"  class="w-auto block text-white bg-green-500 hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">
                      XLS
                    </button>
                    </div>
<!--                 <button id="dropdownRadioButton" data-dropdown-toggle="dropdownRadio" class="inline-flex items-center text-gray-500 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-100 font-medium rounded-lg text-sm px-3 py-1.5 dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700" type="button">-->
<!--                <svg class="w-3 h-3 text-gray-500 dark:text-gray-400 me-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">-->
<!--                        <path d="M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm3.982 13.982a1 1 0 0 1-1.414 0l-3.274-3.274A1.012 1.012 0 0 1 9 10V6a1 1 0 0 1 2 0v3.586l2.982 2.982a1 1 0 0 1 0 1.414Z"/>-->
<!--                    </svg>-->
<!--                Last 30 days-->
<!--                <svg class="w-2.5 h-2.5 ms-2.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">-->
<!--                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>-->
<!--                </svg>-->
<!--            </button>-->
<!--                &lt;!&ndash; Dropdown menu &ndash;&gt;-->
<!--                <div id="dropdownRadio" class="z-10 hidden w-48 bg-white divide-y divide-gray-100 rounded-lg shadow dark:bg-gray-700 dark:divide-gray-600" data-popper-reference-hidden="" data-popper-escaped="" data-popper-placement="top" style="position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate3d(522.5px, 3847.5px, 0px);">-->
<!--                <ul class="p-3 space-y-1 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdownRadioButton">-->
<!--                    <li>-->
<!--                        <div class="flex items-center p-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">-->
<!--                            <input id="filter-radio-example-1" type="radio" value="" name="filter-radio" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">-->
<!--                            <label for="filter-radio-example-1" class="w-full ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">Last day</label>-->
<!--                        </div>-->
<!--                    </li>-->
<!--                    <li>-->
<!--                        <div class="flex items-center p-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">-->
<!--                            <input checked="" id="filter-radio-example-2" type="radio" value="" name="filter-radio" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">-->
<!--                            <label for="filter-radio-example-2" class="w-full ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">Last 7 days</label>-->
<!--                        </div>-->
<!--                    </li>-->
<!--                    <li>-->
<!--                        <div class="flex items-center p-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">-->
<!--                            <input id="filter-radio-example-3" type="radio" value="" name="filter-radio" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">-->
<!--                            <label for="filter-radio-example-3" class="w-full ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">Last 30 days</label>-->
<!--                        </div>-->
<!--                    </li>-->
<!--                    <li>-->
<!--                        <div class="flex items-center p-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">-->
<!--                            <input id="filter-radio-example-4" type="radio" value="" name="filter-radio" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">-->
<!--                            <label for="filter-radio-example-4" class="w-full ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">Last month</label>-->
<!--                        </div>-->
<!--                    </li>-->
<!--                    <li>-->
<!--                        <div class="flex items-center p-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">-->
<!--                            <input id="filter-radio-example-5" type="radio" value="" name="filter-radio" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">-->
<!--                            <label for="filter-radio-example-5" class="w-full ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">Last year</label>-->
<!--                        </div>-->
<!--                    </li>-->
<!--                </ul>-->
<!--            </div>-->
                </caption>
                <thead class="text-xs text-gray-100 uppercase bg-green-500 dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                         <template v-for="(i ,k) in val.fields">
                            <th scope="col" class="px-2 py-3">
                                {{i}}
                            </th>
                      </template>
                    </tr>
                </thead>
                <tbody>
                    <template v-for="(v, index) in val.values">
                          <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-green-50 dark:hover:bg-gray-600">
                            <template v-for="(i ,k) in v">
                              <td class="w-4 p-4">
                                {{ i }}
                              </td>
                            </template>
                          </tr>
                    </template>
                </tbody>
            </table>
        </div>
    </template>
  </form>
</Card>
</template>


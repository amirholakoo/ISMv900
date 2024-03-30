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
        shipments:{type:'input', title: 'لیست بارنامه',filter:'فیلتر', data:'', value:'', fields: []},
        sales:{type:'input', title: 'لیست فروش',filter:'فیلتر', data:'', value:'', fields: []},
        purchases:{type:'input', title: 'لیست خرید',filter:'فیلتر', data:'', value:'', fields: []},
        rawMaterial:{type:'input', title: 'لیست مواد',filter:'فیلتر', data:'', value:'', fields: []},
        products:{type:'input', title: 'لیست محصولات',filter:'فیلتر', data:'', value:'', fields: []},
        consumption:{type:'input', title: 'لیست مصرف',filter:'فیلتر', data:'', value:'', fields: []},
      },
      filters: [
        {lable:'یک سال اخیر', value: 'year'},
        {lable:'یک ماه اخیر', value: 'month'},
        {lable:'هفته اخیر', value: 'week'},
        {lable:'امروز', value: 'day'},
      ],
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
    initFlowbite();
    // this.load_data()
    this.startCountdown();
    this.report_shipment('year')
    this.report_Sales('year')
    this.report_Purchases('year')
    this.report_RawMaterial('year')
    this.report_Products('year')
    this.report_Consumption('year')
  },
  methods: {
    async generate_excel_report(model_name){
      console.log(model_name)
      const params = {
        'model_name':model_name,
      }
      const response = await this.axios.post('/myapp/api/generateExcelReport',{}, {params:params,responseType: 'blob',},)
      // Create a URL for the blob
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;

      // Suggest a filename for the downloaded file
      const filename = response.headers['content-disposition'].split('filename=')[1];
      link.setAttribute('download', filename);

      // Append the link to the body
      document.body.appendChild(link);

      // Simulate click to download the file
      link.click();

      // Remove the link from the body
      document.body.removeChild(link);

      console.log(response.data)
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
    clicked(k, data){
      if (k == 'shipments'){
        this.forms.shipments.filter = data.lable
        this.report_shipment(data.value)
      }
      if (k == 'sales'){
        this.forms.sales.filter = data.lable
        this.report_Sales(data.value)
      }
      if (k == 'purchases'){
        this.forms.purchases.filter = data.lable
        this.report_Purchases(data.value)
      }
      if (k == 'rawMaterial'){
        this.forms.rawMaterial.filter = data.lable
        this.report_RawMaterial(data.value)
      }
      if (k == 'products'){
        this.forms.products.filter = data.lable
        this.report_Products(data.value)
      }
      if (k == 'consumption'){
        this.forms.consumption.filter = data.lable
        this.report_Consumption(data.value)
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
    },
 async report_Sales(filter) {
 try {
    const params = {
      'filter': filter,
    }
    const response = await this.axios.post('/myapp/api/reportSales', {}, {params:params})
    console.log(response.data);
    this.forms['sales'].data = response.data['values']
    this.forms['sales'].fields = response.data['fields']
 } catch (error) {
    console.error("Error fetching sales report:", error);
    // Optionally, display an error message to the user
    // this.errorMessage = "Failed to fetch sales report. Please try again.";
 }
},

async report_Purchases(filter) {
 try {
    const params = {
      'filter': filter,
    }
    const response = await this.axios.post('/myapp/api/reportPurchases', {}, {params:params})
    console.log(response.data);
    this.forms['purchases'].data = response.data['values']
    this.forms['purchases'].fields = response.data['fields']
 } catch (error) {
    console.error("Error fetching purchases report:", error);
    // Optionally, display an error message to the user
    // this.errorMessage = "Failed to fetch purchases report. Please try again.";
 }
},

async report_RawMaterial(filter) {
 try {
    const params = {
      'filter': filter,
    }
    const response = await this.axios.post('/myapp/api/reportRawMaterial', {}, {params:params})
    console.log(response.data);
    this.forms['rawMaterial'].data = response.data['values']
    this.forms['rawMaterial'].fields = response.data['fields']
 } catch (error) {
    console.error("Error fetching raw material report:", error);
    // Optionally, display an error message to the user
    // this.errorMessage = "Failed to fetch raw material report. Please try again.";
 }
},

async report_Products(filter) {
 try {
    const params = {
      'filter': filter,
    }
    const response = await this.axios.post('/myapp/api/reportProducts', {}, {params:params})
    console.log(response.data);
    this.forms['products'].data = response.data['values']
    this.forms['products'].fields = response.data['fields']
 } catch (error) {
    console.error("Error fetching products report:", error);
    // Optionally, display an error message to the user
    // this.errorMessage = "Failed to fetch products report. Please try again.";
 }
},

async report_Consumption(filter) {
 try {
    const params = {
      'filter': filter,
    }
    const response = await this.axios.post('/myapp/api/reportConsumption', {}, {params:params})
    console.log(response.data);
    this.forms['consumption'].data = response.data['values']
    this.forms['consumption'].fields = response.data['fields']
 } catch (error) {
    console.error("Error fetching consumption report:", error);
    // Optionally, display an error message to the user
    // this.errorMessage = "Failed to fetch consumption report. Please try again.";
 }
},

async report_shipment(filter) {
 try {
    const params = {
      'filter': filter,
    }
    const response = await this.axios.post('/myapp/api/reportShipment', {}, {params:params})
    console.log(response.data);
    this.forms['shipments'].data = response.data['values']
    this.forms['shipments'].fields = response.data['fields']
    console.log(this.forms.shipments)
 } catch (error) {
    console.error("Error fetching shipment report:", error);
    // Optionally, display an error message to the user
    // this.errorMessage = "Failed to fetch shipment report. Please try again.";
 }
},

  },
}
</script>

<template>


<!--<Card title="گزارش">-->
  <div class="w-screen p-5 container">
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

                      <button :id="form_name + 'Button1'" :data-dropdown-toggle="form_name+'dropdown1'" class="justify-between w-44 text-white bg-green-500 hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">
                        {{ val.filter }}
                        <svg class="w-2.5 h-2.5 ms-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
                        </svg>
                      </button>
                      <!-- Dropdown menu -->
                      <div :id="form_name+'dropdown1'" class="z-50 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700">
                        <ul class="overflow-y-auto h-auto max-h-48 py-2 text-sm text-gray-700 dark:text-gray-200" :aria-labelledby="form_name + 'Button1'">
                          <li v-for="data in filters">
                            <a @click='clicked(form_name ,data)' type="button" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">
                              {{ data.lable }}
                            </a>
                          </li>
                        </ul>
                      </div>

                    </div>

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
                    <template v-for="(v, index) in val.data">
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
  </div>
<!--</Card>-->
</template>


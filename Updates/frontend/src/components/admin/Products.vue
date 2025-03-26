<script>
import { initFlowbite } from 'flowbite'
import Card from '@/components/Card'
import modal from "@/components/Modal.vue";
import Alert from "@/components/Alert.vue";
import Lic_numer from "@/components/lic_numer.vue";
import { jsPDF } from "jspdf";
import html2canvas from 'html2canvas';

export default {
  name: "Products",
  components: {
    Lic_numer,
    Card,
    modal,
    Alert
  },
  data(){
    return {
      forms: {
        products:{type:'input', title: 'لیست محصولات',filter:'یک سال اخیر', data:'', value:'', fields: []},
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
    }
  },
  mounted() {
    initFlowbite();
    this.report_Products('year')
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
      const filename = response.headers['content-disposition'];
      link.setAttribute('download', filename);

      // Append the link to the body
      document.body.appendChild(link);

      // Simulate click to download the file
      link.click();

      // Remove the link from the body
      document.body.removeChild(link);

      console.log(response.data)
    },
    select(obj){
      this.forms.shipment_list.value = obj
    },
    clicked(k, data){
      if (k == 'products'){
        this.forms.products.filter = data.lable
        this.report_Products(data.value)
      }
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

    async report_Products(filter) {
     try {
        const params = {
          'filter': filter,
        }
        const response = await this.axios.post('/myapp/ProductsPage/', {}, {params:params})
        console.log(response.data);
        this.forms['products'].data = response.data['values']
        this.forms['products'].fields = response.data['fields']
     } catch (error) {
        console.error("Error fetching products report:", error);
        // Optionally, display an error message to the user
        // this.errorMessage = "Failed to fetch products report. Please try again.";
     }
    },


  },
}
</script>

<template>


<!--<Card title="گزارش">-->
  <div class="w-screen p-5 container">
<!--  <p class="flex flex-row gap-2 items-center">-->
<!--    <button @click="reload" class="w-auto block text-white bg-green-500 hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">-->
<!--      بارگیری مجدد-->
<!--    </button>-->
<!--    {{ formattedTime }}-->
<!--  </p>-->
  <form class="flex flex-col items-center mt-5 gap-4">
    <template v-for="(val, form_name) in forms">
        <div class="relative w-full h-auto max-h-[500px] overflow-y-scroll overflow-x-auto shadow-md sm:rounded-lg">
            <table :id="form_name" class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                <caption class="p-5 text-lg font-semibold text-left rtl:text-right text-gray-900 bg-white dark:text-white dark:bg-gray-800">

                    <div class="flex flex-row gap-2 items-center">
                      {{val.title}}
<!--                      <button @click="printTable(form_name)" class="w-auto block text-white bg-green-500 hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">-->
<!--                        PDF-->
<!--                      </button>-->
<!--                      <button @click="generate_excel_report(form_name)"  class="w-auto block text-white bg-green-500 hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">-->
<!--                      XLS-->
<!--                    </button>-->
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
                           <template v-if="i !='id'">
                              <th scope="col" class="px-2 py-3">
                                  {{i}}
                              </th>
                           </template>
                      </template>
                    </tr>
                </thead>
                <tbody>
                    <template v-for="(v, index) in val.data">
                          <tr class="truncate bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-green-50 dark:hover:bg-gray-600">
                            <template v-for="(field ,k) in val.fields">
                              <template v-if="field !='id'">
                                <td class="w-4 p-4">
                                  {{ v[field] }}
                                </td>
                              </template>
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


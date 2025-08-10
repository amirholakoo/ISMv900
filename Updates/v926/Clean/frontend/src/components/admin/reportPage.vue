<script>
import {initFlowbite} from 'flowbite'
import Card from '@/components/Card'
import modal from "@/components/Modal.vue";
import Alert from "@/components/Alert.vue";
import Lic_numer from "@/components/lic_numer.vue";
import {jsPDF} from "jspdf";
import html2canvas from 'html2canvas';

export default {
  name: "reportPage",
  components: {
    Lic_numer,
    Card,
    modal,
    Alert
  },
  data() {
    return {
      forms: {
        shipments: {
          type: 'input',
          title: 'لیست بارنامه',
          filter: 'فیلتر',
          data: '',
          value: '',
          fields: [],
          CopyData: [],
          searchQuery: ''
        },
        sales: {
          type: 'input',
          title: 'لیست فروش',
          filter: 'فیلتر',
          data: '',
          value: '',
          fields: [],
          CopyData: [],
          searchQuery: ''
        },
        purchases: {
          type: 'input',
          title: 'لیست خرید',
          filter: 'فیلتر',
          data: '',
          value: '',
          fields: [],
          CopyData: [],
          searchQuery: ''
        },
        rawMaterial: {
          type: 'input',
          title: 'لیست مواد اولیه',
          filter: 'فیلتر',
          data: '',
          value: '',
          fields: [],
          CopyData: [],
          searchQuery: ''
        },
        products: {
          type: 'input',
          title: 'لیست محصولات',
          filter: 'فیلتر',
          data: '',
          value: '',
          fields: [],
          CopyData: [],
          searchQuery: ''
        },
        consumption: {
          type: 'input',
          title: 'لیست مصرف',
          filter: 'فیلتر',
          data: '',
          value: '',
          fields: [],
          CopyData: [],
          searchQuery: ''
        },
        alerts: {
          type: 'input',
          title: 'هشدار ها',
          filter: 'فیلتر',
          data: [],
          value: '',
          fields: ['date', 'status', 'message'],
          CopyData: [],
          searchQuery: ''
        },
      },
      filters: [
        {lable: 'یک سال اخیر', value: 'year'},
        {lable: 'یک ماه اخیر', value: 'month'},
        {lable: 'هفته اخیر', value: 'week'},
        {lable: 'امروز', value: 'day'},
      ],
      success: false,
      error: false,
      errors: [],

      // Initialize the countdown to 15 minutes (15 * 60 seconds)
      totalSeconds: 5 * 60,
      alerts: [], // Reactive property to store messages
      alertSocket: null, // WebSocket connection
      searchQuery: '',
    }
  },
  computed: {
    // Format the time for display
    formattedTime() {
      const minutes = Math.floor(this.totalSeconds / 60);
      const seconds = this.totalSeconds % 60;
      return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    }
  },
  mounted() {
    initFlowbite();
    // this.load_data()
    this.startCountdown();
    this.report_shipment('year')
    this.report_Products('year')
    this.report_Sales('year')
    this.report_Purchases('year')
    this.report_Consumption('year')
    this.report_RawMaterial('year')
    this.report_alerts('year')
    // Initialize WebSocket connection
    this.alertSocket = new WebSocket('ws://' + window.location.host + '/ws/alert/');

    // Set up message handler
    this.alertSocket.onmessage = (e) => {
      const data = JSON.parse(e.data);
      console.log(this.forms.alerts.data);
      console.log(data.data);
      this.alerts.push({message: data.message});
      this.update_alert(data.data)
    };

    // Handle WebSocket errors
    this.alertSocket.onerror = (error) => {
      console.error('WebSocket Error: ', error);
    };

  },
  beforeDestroy() {
    // Close WebSocket connection when component is destroyed
    if (this.alertSocket) {
      this.alertSocket.close();
    }
  },
  methods: {
    update_alert(d) {
      this.forms.alerts.data.unshift(d);
    },
    async generate_excel_report(model_name) {
      console.log(model_name)
      const params = {
        'model_name': model_name,
      }
      const response = await this.axios.post('/myapp/api/generateExcelReport', {}, {
        params: params,
        responseType: 'blob',
      },)
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
    reload() {
      window.location.reload();
    },
    countdown() {
      if (this.totalSeconds > 0) {
        // Decrement the total seconds by one
        this.totalSeconds -= 1;
      } else {
        // If the countdown has finished, refresh the page
        window.location.reload();
      }
    },
    startCountdown() {
      // Call the countdown function every second
      this.interval = setInterval(this.countdown, 1000);
    },
    select(obj) {
      this.forms.shipment_list.value = obj
    },
    clicked(k, data) {
      if (k == 'shipments') {
        this.forms.shipments.filter = data.lable
        this.report_shipment(data.value)
      }
      if (k == 'sales') {
        this.forms.sales.filter = data.lable
        this.report_Sales(data.value)
      }
      if (k == 'purchases') {
        this.forms.purchases.filter = data.lable
        this.report_Purchases(data.value)
      }
      if (k == 'rawMaterial') {
        this.forms.rawMaterial.filter = data.lable
        this.report_RawMaterial(data.value)
      }
      if (k == 'products') {
        this.forms.products.filter = data.lable
        this.report_Products(data.value)
      }
      if (k == 'consumption') {
        this.forms.consumption.filter = data.lable
        this.report_Consumption(data.value)
      }
      if (k == 'alerts') {
        this.forms.alerts.filter = data.lable
        this.report_alerts(data.value)
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
      html2canvas(table).then(function (canvas) {
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
        const response = await this.axios.post('/myapp/api/reportSales', {}, {params: params})
        console.log(response.data);
        this.forms['sales'].data = response.data['values']
        this.forms['sales'].CopyData = response.data['values']
        this.forms['sales'].fields = response.data['fields']
      } catch (error) {
        console.error("Error fetching sales report:", error);
        this.forms['sales'].data = []
        this.forms['sales'].CopyData = []
        // Optionally, display an error message to the user
        // this.errorMessage = "Failed to fetch sales report. Please try again.";
      }
    },

    async report_Purchases(filter) {
      try {
        const params = {
          'filter': filter,
        }
        const response = await this.axios.post('/myapp/api/reportPurchases', {}, {params: params})
        console.log(response.data);
        this.forms['purchases'].data = response.data['values']
        this.forms['purchases'].CopyData = response.data['values']
        this.forms['purchases'].fields = response.data['fields']
      } catch (error) {
        console.error("Error fetching purchases report:", error);
        this.forms['purchases'].data = []
        this.forms['purchases'].CopyData = []
        // Optionally, display an error message to the user
        // this.errorMessage = "Failed to fetch purchases report. Please try again.";
      }
    },

    async report_RawMaterial(filter) {
      try {
        const params = {
          'filter': filter,
        }
        const response = await this.axios.post('/myapp/api/reportRawMaterial', {}, {params: params})
        console.log(response.data);
        this.forms['rawMaterial'].data = response.data['values']
        this.forms['rawMaterial'].CopyData = response.data['values']
        this.forms['rawMaterial'].fields = response.data['fields']
      } catch (error) {
        console.error("Error fetching raw material report:", error);
        this.forms['rawMaterial'].data = []
        this.forms['rawMaterial'].CopyData = []
        // Optionally, display an error message to the user
        // this.errorMessage = "Failed to fetch raw material report. Please try again.";
      }
    },

    async report_Products(filter) {
      try {
        const params = {
          'filter': filter,
        }
        const response = await this.axios.post('/myapp/api/reportProducts', {}, {params: params})
        console.log(response.data);
        this.forms['products'].data = response.data['values']
        this.forms['products'].CopyData = response.data['values']
        this.forms['products'].fields = response.data['fields']
      } catch (error) {
        console.error("Error fetching products report:", error);
        this.forms['products'].data = []
        this.forms['products'].CopyData = []
        // Optionally, display an error message to the user
        // this.errorMessage = "Failed to fetch products report. Please try again.";
      }
    },

    async report_Consumption(filter) {
      try {
        const params = {
          'filter': filter,
        }
        const response = await this.axios.post('/myapp/api/reportConsumption', {}, {params: params})
        this.forms['consumption'].data = response.data['values']
        this.forms['consumption'].CopyData = response.data['values']
        this.forms['consumption'].fields = response.data['fields']
      } catch (error) {
        console.error("Error fetching consumption report:", error);
        this.forms['consumption'].data = []
        this.forms['consumption'].CopyData = []
        // Optionally, display an error message to the user
        // this.errorMessage = "Failed to fetch consumption report. Please try again.";
      }
    },

    async report_shipment(filter) {
      try {
        const params = {
          'filter': filter,
        }
        const response = await this.axios.post('/myapp/api/reportShipment', {}, {params: params})

        this.forms['shipments'].data = response.data['values']
        this.forms['shipments'].CopyData = response.data['values']
        this.forms['shipments'].fields = response.data['fields']

      } catch (error) {
        console.error("Error fetching shipment report:", error);
        this.forms['shipments'].data = []
        this.forms['shipments'].CopyData = []
        // Optionally, display an error message to the user
        // this.errorMessage = "Failed to fetch shipment report. Please try again.";
      }
    },

    async report_alerts(filter) {
      try {
        const params = {
          'filter': filter,
        }
        const response = await this.axios.post('/myapp/api/reportAlert', {}, {params: params})
        console.log(response.data);
        this.forms['alerts'].data = response.data['values']
        this.forms['alerts'].CopyData = response.data['values']
        this.forms['alerts'].fields = response.data['fields']
        console.log(this.forms.alerts)
      } catch (error) {
        console.error("Error fetching alerts report:", error);

        this.forms['alerts'].data = []
        this.forms['alerts'].CopyData = []
      }
    },

    sortTable(tableName, column) {
      this.forms[tableName].data.sort((a, b) => {
        // Check if the column data is a number
        if (!isNaN(a[column]) && !isNaN(b[column])) {
          return a[column] - b[column];
        }
        // Check if the column data is a string
        if (typeof a[column] === 'string' && typeof b[column] === 'string') {
          // Convert both strings to lowercase for case-insensitive comparison
          const aLower = a[column].toLowerCase();
          const bLower = b[column].toLowerCase();
          if (aLower < bLower) {
            return -1;
          }
          if (aLower > bLower) {
            return 1;
          }
          return 0;
        }
        // If the data is neither a number nor a string, sort alphabetically
        if (a[column] < b[column]) {
          return -1;
        }
        if (a[column] > b[column]) {
          return 1;
        }
        return 0;
      });
    },

    reverseTable(tableName, column) {
      // Reverse the order of the data in the specified column using.reverse()
      this.forms[tableName].data = this.forms[tableName].data.map(row => {
        const reversedRow = {};
        for (const key in row) {
          reversedRow[key] = row[key];
        }
        reversedRow[column] = row[column].reverse();
        return reversedRow;
      });
    },

    filterTable(tableName) {
      if (this.forms[tableName].searchQuery) {
        // this.forms[tableName].CopyData = this.forms[tableName].data
        this.forms[tableName].data = this.forms[tableName].data.filter(item => {
          return Object.values(item).some(value =>
              value !== null && value !== undefined &&
              value.toString().toLowerCase().includes(this.forms[tableName].searchQuery.toLowerCase())
          );
        });
      } else {
        this.forms[tableName].data = this.forms[tableName].CopyData
      }
    }

  },
}
</script>

<template>
  <!--<Card title="گزارش">-->
  <div class="container relative w-screen p-5">
    <!-- The div that should appear in front of all others -->
    <div class="fixed top-0 right-0 left-0 z-10 flex w-full flex-col">
      <template v-for="(alert, index) in alerts" :key="index">
        <Alert :msg="alert.message"></Alert>
      </template>
    </div>
    <p class="flex flex-row items-center gap-2">
      <button @click="reload"
              class="block w-auto rounded-lg bg-green-500 px-5 text-center text-sm font-medium text-white py-2.5 hover:bg-green-600 focus:outline-none focus:ring-4 focus:ring-green-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
              type="button">
        بارگیری مجدد
      </button>
      {{ formattedTime }}
    </p>
    <form class="mt-5 flex flex-col items-center gap-4">
      <template v-for="(val, tableName) in forms">
        <div class="relative h-auto w-full overflow-x-auto overflow-y-scroll shadow-md max-h-[500px] sm:rounded-lg">
          <table :id="tableName" class="w-full text-left rtl:text-right text-sm text-gray-500 dark:text-gray-400">
            <caption
                class="bg-white p-5 text-left rtl:text-right text-lg font-semibold text-gray-900 dark:bg-gray-800 dark:text-white">

              <div class="flex flex-row items-center gap-2">
                <template v-if="tableName == 'products'">
                  <router-link
                      to="/myapp/ProductsPage/"
                      type="button"
                      class="font-medium text-blue-600 hover:underline dark:text-blue-500"
                  >
                    {{ val.title }}
                  </router-link>
                </template>
                <template v-else>
                  {{ val.title }}
                </template>
                <button @click="printTable(tableName)"
                        class="block w-auto rounded-lg bg-green-500 px-5 text-center text-sm font-medium text-white py-2.5 hover:bg-green-600 focus:outline-none focus:ring-4 focus:ring-green-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                        type="button">
                  PDF
                </button>
                <button @click="generate_excel_report(tableName)"
                        class="block w-auto rounded-lg bg-green-500 px-5 text-center text-sm font-medium text-white py-2.5 hover:bg-green-600 focus:outline-none focus:ring-4 focus:ring-green-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                        type="button">
                  XLS
                </button>

                <button :id="tableName + 'Button1'" :data-dropdown-toggle="tableName+'dropdown1'"
                        class="inline-flex w-44 items-center justify-between rounded-lg bg-green-500 px-5 text-center text-sm font-medium text-white py-2.5 hover:bg-green-600 focus:outline-none focus:ring-4 focus:ring-green-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                        type="button">
                  {{ val.filter }}
                  <svg class="w-2.5 h-2.5 ms-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                       viewBox="0 0 10 6">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                          d="m1 1 4 4 4-4"/>
                  </svg>
                </button>
                <!-- Dropdown menu -->
                <div :id="tableName+'dropdown1'"
                     class="z-50 hidden w-44 rounded-lg bg-white shadow divide-y divide-gray-100 dark:bg-gray-700">
                  <ul class="h-auto max-h-48 overflow-y-auto py-2 text-sm text-gray-700 dark:text-gray-200"
                      :aria-labelledby="tableName + 'Button1'">
                    <li v-for="data in filters">
                      <a @click='clicked(tableName ,data)' type="button"
                         class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">
                        {{ data.lable }}
                      </a>
                    </li>
                  </ul>
                </div>
                <input type="text" v-model="forms[tableName].searchQuery" @input="filterTable(tableName)"
                       class="block rounded-lg border border-gray-300 bg-gray-50 p-2 pl-10 text-sm text-gray-900 w-md focus:ring-primary-500 focus:border-primary-500 dark:placeholder-gray-400 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                       placeholder="Search" required="">
              </div>

            </caption>
            <thead class="bg-green-500 text-xs uppercase text-gray-100 dark:bg-gray-700 dark:text-gray-400">
            <tr>
              <template v-for="(column ,k) in val.fields">
                <template v-if="column !='id'">
                  <th scope="col" class="px-2 py-3" @click="sortTable(tableName, column)">
                    {{ column }}
                  </th>
                </template>
              </template>
            </tr>
            </thead>
            <tbody>
            <template v-for="(v, index) in val.data">
              <tr class="truncate border-b bg-white hover:bg-green-50 dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-600">
                <template v-for="(field ,k) in val.fields">
                  <template v-if="field !='id'">
                    <td class="w-4 p-4">
                      <template v-if="(tableName === 'sales' || tableName === 'purchases') && (field === 'total_price' || field === 'unit_price' || field === 'price_per_kg' || field === 'net_weight')">
                        {{ v[field]?.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") }}
                      </template>
                      <template v-else>
                        {{ v[field] }}
                      </template>
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

</template>
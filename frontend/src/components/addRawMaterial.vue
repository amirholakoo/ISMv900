<script>
import { initFlowbite } from 'flowbite'
import Card from './Card'
import Alert from "@/components/Alert.vue";
import modal from "@/components/Modal.vue";

export default {
   name: "addRawMaterial",
  components: {
    modal, Alert,
    Card
  },
  data(){
    return{
      supplier_name: '',
      material_type: '',
      material_name: '',
      comment: '',
      username: '',
      success: false,
      error: false,
      errors: [],
      supplier_names: '',
      material_types: ''
    }
  },
  methods: {
    async addSupplier() {
      const params = {
        "supplier_name": this.supplier_name,
        "material_type": this.material_type,
        "material_name": this.material_name,
        "username": this.username,
        "comments": this.comment
      };
      const response = await this.axios.post('/myapp/addRawMaterial/', {}, {params: params})
      console.log(response.data); // Access response data
      if (response.data['status'] == 'success'){
        this.success = true
      }else {
        this.error = true
        this.errors = response.data['errors']
      }
    },
    supplier_clicked(name){
      this.supplier_name = name
    },
    matrial_clicked(name){
      this.material_name = name
    },
  },
  mounted() {
    initFlowbite();
    this.axios.get('/myapp/api/getSupplierNames').then((response) => {
      if (response.data['status'] == 'success') {
        this.supplier_names = response.data['supplier_names']
      }
    }).catch((error) => {
      console.error('Error fetching supplier names:', error);
    });
    this.axios.get('/myapp/api/getMaterialTypes').then((response) => {
      console.log(response.data)
      if (response.data['status'] == 'success') {
        this.material_types = response.data['material_names']
      }
    }).catch((error) => {
      console.error('Error fetching material names:', error);
    });
  },
}
</script>

<template>
  <Card title="اضافه کردن مواد خام جدید" bgTitle="bg-blue-600">
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

      <button id="supplierNameButton" data-dropdown-toggle="supplierNameDropdown"
              class="w-44 justify-between text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">
        اسم تامین کننده
        <svg class="w-2.5 h-2.5 ms-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
        </svg>
      </button>

      <!-- supplier Dropdown menu -->
      <div id="supplierNameDropdown" class="z-50 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700">
          <ul class="py-2 overflow-y-auto h-48 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="supplierNameButton">
            <li v-for="name in supplier_names" @click="supplier_clicked(name)">
              <a type="button" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">
                {{ name }}
              </a>
            </li>
          </ul>
      </div>

      <button id="material_typeButton"
              data-dropdown-toggle="material_typeDropdown"
              class="justify-between w-44 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">
        نوع مواد
        <svg class="w-2.5 h-2.5 ms-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
        </svg>
      </button>
      <!--matrila type names Dropdown menu -->
      <div id="material_typeDropdown" class="z-50 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700">
          <ul class="overflow-y-auto h-48 py-2 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="material_typeButton">
            <li v-for="name in material_types" @click="matrial_clicked(name)">
              <a type="button" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">
                {{ name }}
              </a>
            </li>
          </ul>
      </div>

      <div class="relative">
        <input v-model="material_name" type="text" id="material_name" class="block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder="" />
        <label for="material_name" class="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">اسم ماده</label>
      </div>
      <div class="relative">
        <input v-model="comment" type="text" id="comment" class="block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder="" />
        <label for="comment" class="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">کامنت</label>
      </div>
      <div class="relative">
        <input v-model="username" type="text" id="username" class="block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder="" />
        <label for="username" class="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">اسم یوزر</label>
      </div>
      <modal type="confirm">
          <template v-slot:button>اضافه کردن</template>
          <template v-slot:text>
            <div class="flex flex-col gap-2 font-bold">
              <p>اسم تامین کننده: {{ supplier_name }}</p>
              <p>نوع مواد: {{ material_type }}</p>
              <p>اسم مواد : {{ material_name }}</p>
              <p>کامنت: {{ comment }}</p>
              <p>نام کاربری: {{ username }}</p>
            </div>
          </template>
          <template v-slot:btns>
            <div>
              <button data-modal-hide="popup-modal" aria-label="Close" @click="addCustomer" type="button" class="inline-flex justify-center w-full px-2 py-1.5 text-xs font-medium text-center text-white bg-blue-600 rounded-lg hover:bg-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-500 dark:hover:bg-blue-600 dark:focus:ring-blue-800">درسته</button>
            </div>
          </template>
      </modal>
      <Alert v-if="success" type="Success">
        <template v-slot:SuccessContent>
          ماده حام  {{material_name}} - {{ material_type }} با موفقیت به دیتابیس اضافه شد.
        </template>
      </Alert>
    </form>
  </Card>
</template>

<script>
import { initFlowbite } from 'flowbite'
import Card from './Card'
import Alert from "@/components/Alert.vue";
import modal from "@/components/Modal.vue";

export default {
  name: "addCustomer",
  components: {
    modal, Alert,
    Card
  },
  mounted() {
    initFlowbite();
  },
  data(){
    return{
      customer_name: '',
      address: '',
      phone: '',
      comment: '',
      username: '',
      success: false,
      error: false,
      errors: [],
    }
  },
  methods: {
    async addCustomer() {
      const params = {
        "customer_name": this.customer_name,
        "address": this.address,
        "phone": this.phone,
        "username": this.username,
        "comments": this.comment,
      };
      const response = await this.axios.post('/myapp/addCustomer/', {}, {params: params})
      console.log(response.data); // Access response data
      if (response.data['status'] == 'success'){
        this.success = true
      }else {
        this.error = true
        this.errors = response.data['errors']
      }
    }
  },
}
</script>

<template>
  <Card title="اضافه کردن مشتری جدید" bgTitle="bg-orange-200">
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
      <input v-model="customer_name" type="text" id="supplier_name" class="block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder="" />
      <label for="supplier_name" class="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">اسم مشتری</label>
    </div>
    <div class="relative">
      <input v-model="address" type="text" id="address" class="block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder="" />
      <label for="address" class="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">آدرس</label>
    </div>
    <div class="relative">
      <input v-model="phone" type="text" id="phone_number" class="block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder="" />
      <label for="phone_number" class="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">شماره همراه</label>
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
            <p>اسم تامین کننده: {{ customer_name }}</p>
            <p>آدرس: {{ address }}</p>
            <p>شماره همراه: {{ phone }}</p>
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
        مشتری جدید با نام {{ customer_name }} با موفقیت به دیتابیس اضافه شد.
      </template>
    </Alert>
  </form>
  </Card>
</template>

<script>
import { initFlowbite } from 'flowbite'
import Card from './Card'
import modal from "@/components/Modal.vue";
import Alert from "@/components/Alert.vue";

export default {
  name: "addSupplier",
  components: {
    Alert,
    modal,
    Card
  },
  mounted() {
    initFlowbite();
  },
  data(){
    return{
      supplier_name: {error: false, val:''},
      address: {error: false, val:''},
      phone: {error: false, val:''},
      comment: {error: false, val:''},
      username: {error: false, val:''},
      success: false,
      error: false,
      errors: [],
      message: ''
    }
  },
  methods: {
    async addSupplier() {
      const params = {
        "supplier_name": this.supplier_name.val,
        "address": this.address.val,
        "phone": this.phone.val,
        "username": this.username.val,
        "comments": this.comment.val,
      };
      const response = await this.axios.post('/myapp/addSupplier/', {}, {params: params})
      console.log(response.data); // Access response data
      if (response.data['status'] == 'success'){
        this.success = true
      }else {
        this.error = true
        this.errors = response.data['errors']
      }
      // this.message=JSON.parse(response.data['message'])
    }
  },
  watch:{
    "supplier_name.val"(c ,p){
      const farsiRange = /[\u0600-\u06FF]/;
      if (farsiRange.test(c)){
        this.supplier_name.error = false
      } else {
        this.supplier_name.error = true
      }
    },
    "address.val"(c ,p){
      const farsiRange = /[\u0600-\u06FF]/;
      if (farsiRange.test(c)){
        this.address.error = false
      } else {
        this.address.error = true
      }
    },
    "phone.val"(c ,p){
      const isPhone = /^09\d{9}$/;
      if (isPhone.test(c)){
        this.phone.error = false
      } else {
        this.phone.error = true
      }
    },
    // "username.val"(c ,p){
    //   const farsiRange = /[a-z]/;
    //   if (farsiRange.test(c)){
    //     this.username.error = false
    //   } else {
    //     this.username.error = true
    //   }
    // },
  }
}
</script>

<template>
  <Card title="اضافه کردن تامین کننده جدید" bgTitle="bg-rose-200">
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
      <div>
        <div class="relative">
          <input v-model="supplier_name.val" type="text" id="supplier_name" :class="[supplier_name.error ? 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 appearance-none dark:text-white dark:border-red-500 border-red-600 dark:focus:border-red-500 focus:outline-none focus:ring-0 focus:border-red-600 peer':'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer']" placeholder="" />
          <label for="supplier_name" :class="[supplier_name.error ? 'absolute text-sm text-red-600 dark:text-red-500 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 start-1 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto':'absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1']">اسم تامین کننده</label>
        </div>
        <p v-if="supplier_name.error" class="mt-2 text-xs text-red-600 dark:text-red-400"><span class="font-medium">Oh, snapp!</span> Some error message.</p>
      </div>
      <div>
        <div class="relative">
          <input v-model="address.val" type="text" id="address" :class="[supplier_name.error ? 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 appearance-none dark:text-white dark:border-red-500 border-red-600 dark:focus:border-red-500 focus:outline-none focus:ring-0 focus:border-red-600 peer':'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer']" placeholder="" />
          <label for="address" :class="[address.error ? 'absolute text-sm text-red-600 dark:text-red-500 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 start-1 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto':'absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1']">آدرس تامین کننده را وارد کنید</label>
        </div>
        <p v-if="address.error" class="mt-2 text-xs text-red-600 dark:text-red-400">آدرس تامین کننده را وارد کنید</p>
      </div>
      <div>
        <div class="relative">
          <input v-model="phone.val" type="text" id="phone" :class="[supplier_name.error ? 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 appearance-none dark:text-white dark:border-red-500 border-red-600 dark:focus:border-red-500 focus:outline-none focus:ring-0 focus:border-red-600 peer':'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer']" placeholder="" />
          <label for="phone" :class="[phone.error ? 'absolute text-sm text-red-600 dark:text-red-500 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 start-1 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto':'absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1']">شماره همراه را وارد کنید</label>
        </div>
        <p v-if="phone.error" class="mt-2 text-xs text-red-600 dark:text-red-400">شماره همراه را وارد کنید</p>
      </div>
      <div>
        <div class="relative">
          <input v-model="username.val" type="text" id="username" :class="[supplier_name.error ? 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 appearance-none dark:text-white dark:border-red-500 border-red-600 dark:focus:border-red-500 focus:outline-none focus:ring-0 focus:border-red-600 peer':'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer']" placeholder="" />
          <label for="username" :class="[username.error ? 'absolute text-sm text-red-600 dark:text-red-500 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 start-1 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto':'absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1']">نام کاربری</label>
        </div>
        <p v-if="username.error" class="mt-2 text-xs text-red-600 dark:text-red-400">نام کاربری را وارد کنید</p>
      </div>
      <div>
        <div class="relative">
          <input v-model="comment.val" type="text" id="comment" :class="[supplier_name.error ? 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 appearance-none dark:text-white dark:border-red-500 border-red-600 dark:focus:border-red-500 focus:outline-none focus:ring-0 focus:border-red-600 peer':'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer']" placeholder="" />
          <label for="comment" :class="[comment.error ? 'absolute text-sm text-red-600 dark:text-red-500 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 start-1 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto':'absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1']">کامنت</label>
        </div>
        <p v-if="comment.error" class="mt-2 text-xs text-red-600 dark:text-red-400">یک کامنت بنویسید</p>
      </div>
      <modal type="confirm">
        <template v-slot:button>اضافه کردن</template>
        <template v-slot:text>
          <div class="flex flex-col gap-2 font-bold">
            <p>اسم تامین کننده: {{ supplier_name.val }}</p>
            <p>آدرس: {{ address.val }}</p>
            <p>شماره همراه: {{ phone.val }}</p>
            <p>کامنت: {{ comment.val }}</p>
            <p>نام کاربری: {{ username.val }}</p>
          </div>
        </template>
        <template v-slot:btns>
          <div>
            <button data-modal-hide="popup-modal" aria-label="Close" @click="addSupplier" type="button" class="inline-flex justify-center w-full px-2 py-1.5 text-xs font-medium text-center text-white bg-blue-600 rounded-lg hover:bg-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-500 dark:hover:bg-blue-600 dark:focus:ring-blue-800">درسته</button>
          </div>
        </template>
      </modal>
      <Alert v-if="success" type="Success">
        <template v-slot:SuccessContent>
          تامین کننده جدید با نام {{ supplier_name.val }} با موفقیت به دیتابیس اضافه شد.
        </template>
      </Alert>
    </form>
  </Card>

</template>

<script>
import { initFlowbite } from 'flowbite'
import Card from './Card'

export default {
  name: "addTruck",
  components: {
    Card
  },
  mounted() {
    initFlowbite();
  },
  data(){
    return {
      license_code1: {val: 12, error: false, class: 'bg-red-50 border border-red-500 text-red-900 placeholder-red-700 text-sm rounded-lg focus:ring-red-500 dark:bg-gray-700 focus:border-red-500 block w-full p-2.5 dark:text-red-500 dark:placeholder-red-500 dark:border-red-500'},
      license_code2: {val: 'ب', error: false, class: 'bg-red-50 border border-red-500 text-red-900 placeholder-red-700 text-sm rounded-lg focus:ring-red-500 dark:bg-gray-700 focus:border-red-500 block w-full p-2.5 dark:text-red-500 dark:placeholder-red-500 dark:border-red-500'},
      license_code3: {val: 365, error: false, class: 'bg-red-50 border border-red-500 text-red-900 placeholder-red-700 text-sm rounded-lg focus:ring-red-500 dark:bg-gray-700 focus:border-red-500 block w-full p-2.5 dark:text-red-500 dark:placeholder-red-500 dark:border-red-500'},
      license_code4: {val: 11, error: false, class: 'bg-red-50 border border-red-500 text-red-900 placeholder-red-700 text-sm rounded-lg focus:ring-red-500 dark:bg-gray-700 focus:border-red-500 block w-full p-2.5 dark:text-red-500 dark:placeholder-red-500 dark:border-red-500'},
      form: true,
      driver_name: '',
      driver_doc: '',
      phone: 0,
      username: ''
    }
  },
  methods: {
    async addTruck() {
      const params = {
        "license_number": this.license_code1.val + this.license_code2.val + this.license_code3.val + this.license_code4.val,
        "driver_name": this.driver_name,
        "driver_doc": this.driver_doc,
        "phone": this.phone,
        "username": this.username,
        "comments": ''
      };
      const response = await this.axios.post('/myapp/addTruck/', {}, {params: params})
      console.log(response.data); // Access response data

    }
  },
  watch: {
    "license_code2.val"(c, p){
      const farsiRange = /[\u0600-\u06FF]/;
      if (farsiRange.test(c)){
        this.license_code2.error = false
      } else {
        this.license_code2.error = true
      }
    },
    "license_code4.val"(c, p){
      if ( Number.isInteger(parseInt(c)) ){
        console.log('bingo')
        this.license_code4.val = parseInt(c)
      }else {
        this.license_code4.val = parseInt(p)
      }
    }
  },
}
</script>

<template>

<Card title="برسی و اضافه کردن کامیون" bgTitle="bg-blue-200">
  <!--   license-->
  <div class="flex flex-row justify-center">
      <div class="rounded-lg bg-white shadow-lg max-w-sm">
      <div class="flex rounded-lg border-4 border-black shadow">
        <label class="flex flex-none flex-col items-center px-4 border-e-4 border-black font-bold">
          ایران
          <p class="place-self-center text-4xl">{{ license_code4.val }}</p>
        </label>
        <label class="flex-grow flex flex-row justify-center p-4 font-mono text-5xl font-bold">{{ license_code3.val }}-{{ license_code2.val }}-{{ license_code1.val }}</label>
        <label class="flex flex-none flex-col items-end justify-between px-1 py-2 bg-blue-700 border-s-4 border-black font-bold text-sm text-white">
          <img src="@/assets/Flag_of_Iran.svg.png" class="h-5">
          <span class="flex flex-col items-end">
            <h>IR</h>
            <h>IRAN</h>
          </span>
        </label>
      </div>
    </div>
  </div>
  <!-- license form-->
  <form v-if="form" class="flex flex-col items-center mt-5 gap-4">
    <div class="flex space-x-2 rtl:space-x-reverse">
        <div>
            <label for="code-1" class="sr-only">First code</label>
            <input v-model="license_code4.val" :placeholder="license_code4.val" type="text" maxlength="2" data-focus-input-init data-focus-input-next="code-2" id="code-1" :class="[license_code4.error ? 'appearance-none bg-red-50 border border-red-500 text-red-900 placeholder-red-700 text-sm rounded-lg focus:ring-red-500 dark:bg-gray-700 focus:border-red-500 dark:text-red-500 dark:placeholder-red-500 dark:border-red-500' : 'text-gray-900 bg-white border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500']" class="block w-12 h-9 py-3 text-sm font-extrabold text-center" required />
        </div>
        <div>
            <label for="code-3" class="sr-only">Third code</label>
            <input v-model="license_code3.val" :placeholder="license_code3.val" type="text" maxlength="3" data-focus-input-init data-focus-input-prev="code-2" data-focus-input-next="code-4" id="code-3" :class="[license_code3.error ? 'bg-red-50 border border-red-500 text-red-900 placeholder-red-700 text-sm rounded-lg focus:ring-red-500 dark:bg-gray-700 focus:border-red-500 dark:text-red-500 dark:placeholder-red-500 dark:border-red-500' : 'text-gray-900 bg-white border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500']" class="block w-14 h-9 py-3 text-sm font-extrabold text-center" required />
        </div>
        <div>
            <label for="code-2" class="sr-only">Second code</label>
            <input v-model="license_code2.val" :placeholder="license_code2.val" type="text" maxlength="1" data-focus-input-init data-focus-input-prev="code-1" data-focus-input-next="code-3" id="code-2" :class="[license_code2.error ? 'bg-red-50 border border-red-500 text-red-900 placeholder-red-700 text-sm rounded-lg focus:ring-red-500 dark:bg-gray-700 focus:border-red-500 dark:text-red-500 dark:placeholder-red-500 dark:border-red-500' : 'text-gray-900 bg-white border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500']" class="block w-9 h-9 py-3 text-sm font-extrabold text-center " required />
        </div>
        <div>
            <label for="code-4" class="sr-only">Fourth code</label>
            <input v-model="license_code1.val" :placeholder="license_code1.val" type="text" maxlength="2" data-focus-input-init data-focus-input-prev="code-3" data-focus-input-next="code-5" id="code-4" :class="[license_code1.error ? 'bg-red-50 border border-red-500 text-red-900 placeholder-red-700 text-sm rounded-lg focus:ring-red-500 dark:bg-gray-700 focus:border-red-500 dark:text-red-500 dark:placeholder-red-500 dark:border-red-500' : 'text-gray-900 bg-white border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500']" class="block w-12 h-9 py-3 text-sm font-extrabold text-center" required />
        </div>
    </div>
    <p v-if="license_code2.error" class="mt-2 text-sm text-red-600 dark:text-red-500"><span class="font-medium">خطا! </span>لطفا از حروف فارسی استفاده کنید</p>
    <p id="helper-text-explanation" class="text-sm text-gray-500 dark:text-gray-400">لطفا پلاک مورد نطر را وارد کرده و سپس بر روی دکمه چک کردن کلیک کنید.</p>
    <button @click="form = !form" class="block text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="submit"> چک کردن </button>
  </form>
  <form v-else class="flex flex-col items-center mt-5 gap-4">
    <div class="relative ">
      <input v-model="driver_name" type="text" id="driver_name" class="block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder="" />
      <label for="driver_name" class="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">اسم راننده</label>
    </div>
    <div class="relative">
      <input v-model="driver_doc" type="text" id="driver_doc" class="block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder="" />
      <label for="driver_doc" class="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">شماره گواهی نامه</label>
    </div>
    <div class="relative">
      <input v-model="phone" type="text" id="phone_number" class="block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder="" />
      <label for="phone_number" class="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">شماره همراه</label>
    </div>
    <div class="relative">
      <input v-model="username" type="text" id="username" class="block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder="" />
      <label for="username" class="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">اسم یوزر</label>
    </div>
    <button @click="addTruck" class="block text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">اضافه کردن کامیون جدید</button>
  </form>
</Card>
</template>

<style scoped>

</style>
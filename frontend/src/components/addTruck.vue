<script>
import { initFlowbite } from 'flowbite'
import Card from './Card'
import modal from "@/components/Modal.vue";
import Alert from "@/components/Alert.vue";
import Lic_numer from "@/components/lic_numer.vue";
import {LicenseNumberParser} from "@/components/lic_num_split";

export default {
  name: "addTruck",
  components: {
    Lic_numer,
    Card,
    modal,
    Alert
  },
  mounted() {
    initFlowbite();
  },
  data(){
    return {
      first: {val: 12, error: false,},
      letter: {val: 'ب', error: false, alphabets:['الف', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی']},
      second: {val: 365, error: false,},
      year: {val: 11, error: false,},
      isExists: false,
      form: true,
      driver_name: '',
      driver_doc: '',
      phone: 0,
      username: '',
      forms: {
        driver_name: {type: 'input', name: 'اسم راننده',title: 'راننده', data: '', value: ''},
        driver_doc: {type: 'input', name: 'شماره گواهی نامه',title: 'شماره گواهی نامه', data: '', value: ''},
        phone: {type: 'input', name: 'شماره همراه',title: 'شماره همراه', data: '', value: ''},
        username: {type: 'input', name: 'نام کاربر',title: 'نام کاربر', data: '', value: ''},
      },
      success: false,
      error: false,
      errors: [],
    }
  },
  methods: {
    clicked(k, name){
      console.log(k, name)
      if (k == 'letter'){
        this.letter.val = name
      }
    },
    async check_license_number() {
      if (this.error!=false){
        const params = {
          "license_number": this.first.val + this.letter.val + this.second.val +"ایران"+ this.year.val,
        };
        const response = await this.axios.post('/  myapp/api/checkLicenseNumber', {}, {params: params})
        console.log(response.data); // Access response data
        console.log(JSON.parse(response.data['isExists'])); // Access response data
        this.form = JSON.parse(response.data['isExists'])
        if (JSON.parse(response.data['isExists'])){
          this.isExists = true
        }
      }
    },
    async addTruck() {
      this.forms[key].error = false

      const params = {
        "license_number": this.first.val + this.letter.val + this.second.val +"ایران"+ this.year.val,
        "driver_name": this.forms.driver_name.value,
        "driver_doc": this.forms.driver_doc.value,
        "phone": this.forms.phone.value,
        "username": this.forms.username.value,
      };
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
        const response = await this.axios.post('/myapp/addTruck/', {}, {params: params})
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
      // console.log(LicenseNumberParser(params.license_number))
      // const response = await this.axios.post('/myapp/addTruck/', {}, {params: params})
      // console.log(response.data); // Access response data
      // this.success = JSON.parse(response.data['success'])
    },
  },
  watch: {
    success(c, p){
      if (c == true) {
        setTimeout(() => {
          this.success = false
          location.reload();
        }, 5000)
      }
    },
    // "letter.val"(c, p){
  //   // const farsiRange = /[\u0600-\u06FF]/;
  //   // if (farsiRange.test(c)){
  //   //   this.letter.error = false
  //   // } else {
  //   //   this.letter.error = true
  //   // }
  // },
    "first.val"(c, p, n){
      if ( Number.isInteger(parseInt(c))){
        this.first.val = parseInt(c)
        console.log('adad', c, p, n)
        if (this.first.error){
          this.first.error = false
          console.log('letter', c, p, n)
          console.log(this.first)
        }
      }else {
        this.first.val = parseInt(p)
        this.first.error = true
      }
      let f = this.first.val.toString()
      console.log(f, typeof f,f.length === 2,f[1] == '0',f.length === 2 && f[1] == '0')
      if (f.length === 2 && f[1] == '0'){
            this.first.error = true
            this.error = true
            // this.errors.push({'message': 'eror'})
      }
    },
  "second.val"(c, p){
    if ( Number.isInteger(parseInt(c)) ){
      this.second.val = parseInt(c)
      if (this.second.error){
        this.second.error = false
      }
    }else {
      this.second.val = parseInt(p)
      this.second.error = true
    }

    let f = this.second.val.toString()
    console.log(f, typeof f,f.length === 2,f[1] == '0',f.length === 2 && f[1] == '0')
    if (f.length === 2 && f[1] == '0' || f[2] == '0'){
          this.second.error = true
          this.error = true
          // this.errors.push({'message': 'eror'})
    }
  },
  "year.val"(c, p){
    if ( Number.isInteger(parseInt(c)) ){
      this.year.val = parseInt(c)
      if (this.year.error){
        this.year.error = false
      }
    }else {
      this.year.val = parseInt(p)
      this.year.error = true
    }

    let f = this.year.val.toString()
    console.log(f, typeof f,f.length === 2,f[1] == '0',f.length === 2 && f[1] == '0')
    if (f.length === 2 && f[1] == '0'){
          this.year.error = true
          this.error = true
          // this.errors.push({'message': 'eror'})
    }
  }
 }
}
</script>

<template>

<Card title="برسی و اضافه کردن کامیون">

  <!--   license-->
  <div class="flex flex-row justify-center">
      <div class="rounded-lg bg-white shadow-lg max-w-sm">
      <div class="flex rounded-lg border-4 border-black shadow">
        <label class="flex flex-none flex-col items-center px-4 border-e-4 border-black font-bold">
          ایران
          <p class="place-self-center text-4xl">{{ year.val }}</p>
        </label>
        <label class="flex-grow flex flex-row gap-4 justify-center p-4 font-mono text-5xl font-bold">
          <h>{{ second.val }}</h>
          <h>{{ letter.val }}</h>
          <h>{{ first.val }}</h>
        </label>
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
            <input v-model="year.val" :placeholder="year.val" type="text" maxlength="2" data-focus-input-init data-focus-input-next="code-2" id="code-1" :class="[year.error ? 'appearance-none bg-red-50 border border-red-500 text-red-900 placeholder-red-700 text-sm rounded-lg focus:ring-red-500 dark:bg-gray-700 focus:border-red-500 dark:text-red-500 dark:placeholder-red-500 dark:border-red-500' : 'text-gray-900 bg-white border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500']" class="block w-12 h-9 py-3 text-sm font-extrabold text-center" required />
        </div>
        <div>
            <label for="code-3" class="sr-only">Third code</label>
            <input v-model="second.val" :placeholder="second.val" type="text" maxlength="3" data-focus-input-init data-focus-input-prev="code-2" data-focus-input-next="code-4" id="code-3" :class="[second.error ? 'bg-red-50 border border-red-500 text-red-900 placeholder-red-700 text-sm rounded-lg focus:ring-red-500 dark:bg-gray-700 focus:border-red-500 dark:text-red-500 dark:placeholder-red-500 dark:border-red-500' : 'text-gray-900 bg-white border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500']" class="block w-14 h-9 py-3 text-sm font-extrabold text-center" required />
        </div>
        <button id="letterButton" data-dropdown-toggle="letterdropdown" :class="[letter.error ? 'bg-red-50 border border-red-500 text-red-900 placeholder-red-700 text-sm rounded-lg focus:ring-red-500 dark:bg-gray-700 focus:border-red-500 dark:text-red-500 dark:placeholder-red-500 dark:border-red-500' : 'text-gray-900 bg-white border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500']" class="block w-9 h-9 text-sm font-extrabold rounded-lg" type="button">
          {{ letter.val }}
        </button>
        <!-- Dropdown menu -->
        <div id="letterdropdown" class="z-50 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-14 dark:bg-gray-700">
          <ul class="overflow-y-auto h-auto max-h-48 py-2 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="letterButtonButton">
            <li v-for="l in letter.alphabets">
              <a @click="clicked('letter', l)" type="button" class="block text-center px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">
                {{ l }}
              </a>
            </li>
<!--            <li v-for="data in val.data">-->
<!--              <a @click='clicked(form_name ,data)' type="button" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">-->
<!--                {{ data }}-->
<!--              </a>-->
<!--            </li>-->
          </ul>
      </div>
        <div>
            <label for="code-4" class="sr-only">Fourth code</label>
            <input v-model="first.val" :placeholder="first.val" type="text" maxlength="2" data-focus-input-init data-focus-input-prev="code-3" data-focus-input-next="code-5" id="code-4" :class="[first.error ? 'bg-red-50 border border-red-500 text-red-900 placeholder-red-700 text-sm rounded-lg focus:ring-red-500 dark:bg-gray-700 focus:border-red-500 dark:text-red-500 dark:placeholder-red-500 dark:border-red-500' : 'text-gray-900 bg-white border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500']" class="block w-12 h-9 py-3 text-sm font-extrabold text-center" required />
        </div>
    </div>

    <template v-if="isExists">
      <div class="mt-2 flex flex-row items-center gap-1">
        <p class="text-red-600">درحال حاضر پلاک </p>
        <lic_numer :lic="{
                first: this.first.val,
                letter: this.letter.val,
                second: this.second.val,
                country: 'ایران',
                year: this.year.val
            }"></lic_numer>
        <p class="text-red-600"> در سیستم وجود دارد.</p>
      </div>
    </template>
    <p id="helper-text-explanation" class="text-sm text-gray-500 dark:text-gray-400">لطفا پلاک مورد نطر را وارد کرده و سپس بر روی دکمه چک کردن کلیک کنید.</p>
<!--    <button @click="form = !form" class="block text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="submit"> چک کردن </button>-->
    <button @click="check_license_number" class="block text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button"> چک کردن </button>
  </form>
  <form v-else class="flex flex-col items-center mt-5 gap-4">
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
      <div>
        <div class="mt-2 flex flex-row items-center gap-1">
          <svg class="flex-shrink-0 inline w-4 h-4 me-3 mt-[2px]" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
            <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/>
          </svg>
          <p class="font-medium">پلاک جدید </p>
          <lic_numer :lic="{
                  first: this.first.val,
                  letter: this.letter.val,
                  second: this.second.val,
                  country: 'ایران',
                  year: this.year.val
              }"></lic_numer>
          <p class="font-medium"> با موفقیت به سیستم اضافه شد.</p>
        </div>
      </div>
    </div>
    <template v-for="(val, form_name) in forms">
      <template v-if="val.type=='input'">
        <div class="relative">
          <input v-model="val.value" type="text" :id="form_name" :class="[val.error ? 'text-red-900 border-red-500 focus:border-red-500' : 'text-gray-900 focus:border-green-500 border-gray-300']" class="block px-2.5 pb-2.5 pt-4 w-full text-sm  bg-transparent rounded-lg border-1 appearance-none focus:outline-none focus:ring-0 peer" placeholder="" />
          <label :for="form_name" :class="[val.error ? 'peer-focus:text-red-500 text-red-500' : 'peer-focus:text-green-500 text-gray-500']" class="absolute text-sm dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2  peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">
            {{val.name}}
          </label>
        </div>
      </template>
      <template v-if="val.type=='dropdown'">
        <button :id="form_name + 'Button'" :data-dropdown-toggle="form_name+'dropdown'" class="justify-between w-44 text-white bg-green-500 hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">
          {{val.name}}
          <svg class="w-2.5 h-2.5 ms-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
          </svg>
        </button>
        <!-- Dropdown menu -->
        <div :id="form_name+'dropdown'" class="z-50 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700">
          <ul class="overflow-y-auto h-auto max-h-48 py-2 text-sm text-gray-700 dark:text-gray-200" :aria-labelledby="form_name + 'Button'">
            <li v-for="data in val.data">
              <a @click='clicked(form_name ,data)' type="button" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">
                {{ data }}
              </a>
            </li>
          </ul>
      </div>
      </template>
    </template>
    <modal type="confirm">
      <template v-slot:button>اضافه کردن</template>
      <template v-slot:text>
        <div class="flex flex-col gap-2 font-bold">
          <div class="mt-2 flex flex-row items-center gap-1">
            <p>پلاک :</p>
            <lic_numer :lic="{
                    first: this.first.val,
                    letter: this.letter.val,
                    second: this.second.val,
                    country: 'ایران',
                    year: this.year.val
                }"></lic_numer>
          </div>
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
<!--          <button data-modal-hide="popup-modal" aria-label="Close" @click="addTruck" type="button" class="inline-flex justify-center w-full px-2 py-1.5 text-xs font-medium text-center text-white bg-blue-600 rounded-lg hover:bg-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-500 dark:hover:bg-blue-600 dark:focus:ring-blue-800">درسته</button>-->
          <button data-modal-hide="popup-modal" aria-label="Close" @click="addTruck" type="button" class="inline-flex justify-center w-full px-2 py-1.5 text-xs font-medium text-center text-white        bg-green-500 hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-green-300  rounded-lg dark:bg-blue-500 dark:hover:bg-blue-600 dark:focus:ring-blue-800">درسته</button>
        </div>
      </template>
    </modal>
  </form>
</Card>
</template>

<script>
import {initFlowbite} from "flowbite";
import modal from "@/components/Modal.vue";
import Alert from "@/components/Alert.vue";
import Card from "@/components/Card.vue";
import ModalButton from "@/components/custom/ModalButton.vue";
import Input from "@/components/custom/Input.vue";
import Dropdown from "@/components/custom/Dropdown.vue";

export default {
  name: "used",
  components: {Dropdown, Input, ModalButton, Card, Alert, modal},
  data(){
    return {
      forms: {
        unloading_location: {type: 'dropdown', name: 'انبار مورد نظر',title: 'انبار مورد نظر', data: '', value: ''},
        supplier_name: {type: 'dropdown', name: 'اسم تامین کننده',title: 'اسم تامین کننده', data: '', value: ''},
        material_name: {type: 'dropdown', name: 'اسم ماده',title: 'اسم ماده', data: '', value: ''},
        unit: {type: 'dropdown', name: 'واحد',title: 'واحد', data: '', value: ''},
        Quantity: {type:'input', name: 'مقدار',title: 'مقدار', value: '', lable:'number'},
        forklift_driver: {type:'input', name: 'اسم راننده لیفت تراک',title: 'اسم راننده لیفت تراک', value: ''},
      },
      success: false,
      error: false,
      errors: [],
    }
  },
  mounted() {
    initFlowbite();
    this.axios.get('/myapp/api/getAnbarTableNames').then((response) => {
      console.log(response.data)
      this.forms.unloading_location.data = response.data['data']
    })
  },
  methods:{
    clicked(k, name){
      console.log(k, name)
      if (k == 'unloading_location'){
        this.forms.unloading_location.name = name
        this.forms.unloading_location.value = name
        const params = {
          'anbar_location': this.forms.unloading_location.value,
        }
        this.axios.get('/myapp/api/getSupplierNamesBasedAndbar', {params:params}).then((response) => {
          console.log(response.data)
          this.forms.supplier_name.data = response.data['supplier_names']
          // this.forms.material_name.data = response.data['material_names']
          // this.forms.unit.data = response.data['units']
        })
      }
      if (k == 'supplier_name'){
        this.forms.supplier_name.name = name
        this.forms.supplier_name.value = name
      //   request for geing materila name and unit name based on supplirt name each anbar

        const params = {
          'anbar_location': this.forms.unloading_location.value,
          'supplier_name': name,
        }
        this.axios.get('/myapp/api/getUnitAndMaterialNameBasedSupplierNmaeAndbar', {params:params}).then((response) => {
          console.log(response.data)
          this.forms.material_name.data = response.data['material_names']
          this.forms.unit.data = response.data['units']
        })
      }
      if (k == 'material_name'){
        this.forms.material_name.name = name
        this.forms.material_name.value = name
      }
      if (k == 'unit'){
        this.forms.unit.name = name
        this.forms.unit.value = name
      }
    },
    async used() {
      const params = {
        "unloading_location": this.forms.unloading_location.value,
        "supplier_name": this.forms.supplier_name.value,
        "material_name": this.forms.material_name.value,
        "unit": this.forms.unit.value,
        "quantity": this.forms.Quantity.value,
        "forklift_driver": this.forms.forklift_driver.value
      };
      const response = await this.axios.post('/myapp/api/used', {}, {params: params})
      console.log(response.data); // Access response data
      if (response.data['status'] == 'success'){
        this.success = true
      }else {
        this.error = true
        this.errors = response.data['errors']
      }
    },
  },
  watch:{
    success(c, p){
      if (c == true) {
        setTimeout(() => {
          this.success = false
          location.reload();
        }, 5000)
      }
    },
  },
}
</script>

<template>
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
      <div v-if="success" class="flex p-4 mb-4 text-sm text-green-800 rounded-lg bg-green-50 dark:bg-gray-800 dark:text-green-400" role="alert">
        <svg class="flex-shrink-0 inline w-4 h-4 me-3 mt-[2px]" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
          <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/>
        </svg>
        <div>
          <span class="font-medium">
             با موفقیت به سیستم اضافه شد.
            <template v-for="(val, key) in forms">
                <p v-if="key=='reel_numbers'">شماره رول:</p>
                <ul v-if="key=='reel_numbers'">
                  <li v-for="item in val.value" :key="item">{{ item }}</li>
                </ul>
                <p v-else>{{val.title}}: {{val.value}}</p>
            </template>
          </span>
        </div>
      </div>
      <template v-for="(val, form_name) in forms">
<!--        <template v-if="val.type=='input'">-->
<!--          <div class="relative">-->
<!--            <input v-model="val.value" type="text" :id="form_name" :class="[val.error ? 'text-red-900 border-red-500 focus:border-red-500' : 'text-gray-900 focus:border-green-500 border-gray-300']" class="block px-2.5 pb-2.5 pt-4 w-full text-sm  bg-transparent rounded-lg border-1 appearance-none focus:outline-none focus:ring-0 peer" placeholder="" />-->
<!--            <label :for="form_name" :class="[val.error ? 'peer-focus:text-red-500 text-red-500' : 'peer-focus:text-green-500 text-gray-500']" class="absolute text-sm dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2  peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">-->
<!--              {{val.name}}-->
<!--            </label>-->
<!--          </div>-->
<!--        </template>-->
<!--        <template v-if="val.type=='dropdown'">-->
<!--          <button :id="form_name + 'Button'" :data-dropdown-toggle="form_name+'dropdown'" class="justify-between w-44 text-white bg-green-500 hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">-->
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
        <template v-if="val.type=='input'">
            <Input
              :formName="form_name"
              :label="val.name"
              :type="val.lable"
              :disabled="val.disabled"
              @update="val.value = $event"
              :value="val.value"
              @InputError="error = $event"
            />
        </template>
        <template v-if="val.type=='dropdown'">
          <Dropdown :formName="form_name">
            <template v-slot:btnName>
              {{val.name}}
            </template>
            <template v-slot:list>
              <li v-for="(data, index) in val.data" :key="index">
                <a @click="clicked(form_name, data)" type="button" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">
                  {{ data }}
                </a>
              </li>
            </template>
          </Dropdown>
        </template>

      </template>
      <modal type="confirm" :disabled="error">
        <template v-slot:button>اضافه کردن</template>
        <template v-slot:text>
          <div class="flex flex-col gap-2 font-bold">
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
<!--            <button data-modal-hide="popup-modal" aria-label="Close" @click="used" type="button" class="inline-flex justify-center w-full px-2 py-1.5 text-xs font-medium text-center text-white        bg-green-500 hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-green-300  rounded-lg dark:bg-blue-500 dark:hover:bg-blue-600 dark:focus:ring-blue-800">درسته</button>-->
            <ModalButton @close="used"/>
          </div>
        </template>
      </modal>
    </form>
</template>
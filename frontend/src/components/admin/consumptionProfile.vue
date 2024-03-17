<script>
import {initFlowbite} from "flowbite";
import modal from "@/components/Modal.vue";
import Alert from "@/components/Alert.vue";
import Card from "@/components/Card.vue";

export default {
  name: "consumptionProfile",
  components: {Card, Alert, modal},
  data(){
    return {
      forms: {
        supplier_name: {type: 'dropdown', name: 'اسم فروشنده',title: 'اسم فروشنده', data: '', value: ''},
        material_name: {type: 'dropdown', name: 'اسم ماده',title: 'اسم ماده', data: '', value: ''},
        unit: {type: 'dropdown', name: 'واحد',title: 'واحد', data: '', value: ''},
        quantity: {type: 'input', name: 'مقدار',title: 'مقدار', data: '', value: ''},
        btn: {type:'btn'},
        consumption_list: {type:'list', name: 'لیست مصرف',title: 'لیست مصرف', value: []},
        profile_name: {type:'input', name: 'اسم پروفایل',title: 'اسم پروفایل', value: ''},
        username: {type:'input', name: 'نام کاربر',title: 'نام کاربر', value: ''},
      },
      success: false,
      error: false,
      errors: [],
    }
  },
  mounted() {
    initFlowbite();
    this.axios.get('/myapp/api/getSupplierNames').then((response) => {
      console.log(response.data)
      this.forms.supplier_name.data = response.data['supplier_names']
    })
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
  methods:{
    add(){
      const profile = {
        'supplier_name': this.forms.supplier_name.value,
        'material_name': this.forms.material_name.value,
        'unit': this.forms.unit.value,
        'quantity': this.forms.quantity.value,
      }
      if (this.forms.consumption_list.value.length <=9){
       this.forms.consumption_list.value.push(profile)
      }
    },
    remove(index){
      this.forms.consumption_list.value.splice(index, 1)
    },
    clicked(k, name){
      console.log(k, name)
      if (k == 'supplier_name'){
        this.forms.supplier_name.name = name
        this.forms.supplier_name.value = name
        const params = {
          'supplier_name': this.forms.supplier_name.value
        }
        this.axios.get('/myapp/api/getMaterialNames', {params:params}).then((response) => {
          console.log(response.data)
          this.forms.material_name.data = response.data['material_names']
        })
        this.axios.get('/myapp/api/getUnitNamesBasedOnSupplier', {params:params}).then((response) => {
          console.log(response.data)
          this.forms.unit.data = response.data['unit_names']
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
    async addSupplier() {
      const params = {
        'supplier_name': this.forms.supplier_name.value,
        'material_name': this.forms.material_name.value,
        'unit': this.forms.unit.value,
        'quantity': this.forms.quantity.value,
        'consumption_list': JSON.stringify(this.forms.consumption_list.value),
        'profile_name': this.forms.profile_name.value,
        'username': this.forms.username.value,
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
        const response = await this.axios.post('/myapp/addConsumptionProfile/', {}, {params: params})
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

    },
  }
}
</script>

<template>
  <Card title="اضافه کردن پروفایل مصرف جدید">
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
            مشتری جدید با نام {{ forms.customer_name.value }} با موفقیت به سیستم اضافه شد.
          </span>
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
        <template v-if="val.type=='btn'">
          <button @click="add" class="w-44 block text-white bg-green-500 hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">
            اضافه کردن به پروفایل
          </button>
        </template>
        <template v-if="val.type=='list'">
          <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
            <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                <thead class="text-md text-gray-100 uppercase bg-green-500 dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                        <th scope="col" class="px-6 py-3">
                            اسم فروشنده
                        </th>
                        <th scope="col" class="px-6 py-3">
                            اسم ماده
                        </th>
                        <th scope="col" class="px-6 py-3">
                            واحد
                        </th>
                        <th scope="col" class="px-6 py-3">
                            مقدار
                        </th>
                        <th scope="col" class="px-6 py-3">
                            <span class="sr-only">حذف</span>
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <template v-for="(obj, index) in forms.consumption_list.value">
                       <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-green-50 dark:hover:bg-gray-600">
                         <template v-for="profile in obj">
                            <td class="px-6 py-4">
                              {{ profile }}
                            </td>
                         </template>
                            <td class="px-6 py-4 text-right">
                                <button @click='remove(index)' type="button" class="font-medium text-blue-600 dark:text-blue-500">حدف</button>
                            </td>
                       </tr>
                    </template>
                </tbody>
            </table>
          </div>
        </template>
      </template>
      <modal type="confirm">
      <template v-slot:button>اضافه کردن</template>
      <template v-slot:text>
        <div class="flex flex-col gap-2 font-bold max-w-xs">
          <div class="max-w-xs overflow-x-auto shadow-md sm:rounded-lg">
                    <table class="max-w-xs text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                        <thead class="text-md text-gray-100 uppercase bg-green-500 dark:bg-gray-700 dark:text-gray-400">
                            <tr>
                                <th scope="col" class="px-2 py-1">
                                    اسم فروشنده
                                </th>
                                <th scope="col" class="px-2 py-1">
                                    اسم ماده
                                </th>
                                <th scope="col" class="px-2 py-1">
                                    واحد
                                </th>
                                <th scope="col" class="px-2 py-1">
                                    مقدار
                                </th>
                                <th scope="col" class="px-2 py-1">
                                    <span class="sr-only">حذف</span>
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <template v-for="(obj, index) in forms.consumption_list.value">
                               <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-green-50 dark:hover:bg-gray-600">
                                 <template v-for="profile in obj">
                                    <td class="px-2 py-1">
                                      {{ profile }}
                                    </td>
                                 </template>
                                    <td class="px-2 py-1 text-right">
                                        <button @click='remove(index)' type="button" class="font-medium text-blue-600 dark:text-blue-500">حدف</button>
                                    </td>
                               </tr>
                            </template>
                        </tbody>
                    </table>
                  </div>
        </div>
      </template>
      <template v-slot:btns>
        <div>
          <button data-modal-hide="popup-modal" aria-label="Close" @click="addSupplier" type="button" class="inline-flex justify-center w-full px-2 py-1.5 text-xs font-medium text-center text-white        bg-green-500 hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-green-300  rounded-lg dark:bg-blue-500 dark:hover:bg-blue-600 dark:focus:ring-blue-800">درسته</button>
        </div>
      </template>
  </modal>
    </form>
  </Card>
</template>

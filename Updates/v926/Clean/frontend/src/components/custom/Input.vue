<script>
export default {
  name: "Input",
  props: {
    formName: {
      type: String,
      required: true,
    },
    label: {
      type: String,
      required: true,
    },
    value: {
      type: String,
      default: '',
    },
    type: {
      type: String,
      default: 'text',
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    hidden:{
      type: Boolean,
      default: false,
   },
  },
  data(){
    return {
      error: false,
      message: '',
      inputValue: this.value
    }
  },
  methods: {
    formatNumber(value) {
      return value.replace(/\D/g, "");
    },
    updateValue(newValue) {
      // if (this.type == 'text'){
      //   let pattern = /^[\u0600-\u06FF\s]*$/
      //   if (pattern.test(newValue) == false){
      //     this.error = true;
      //     this.message = 'لطفا از حروف فارسی استفاده کنید.'
      //   } else {
      //     this.error = false
      //     this.message = ''
      //   }
      // }
      if (this.type == 'number'){
        if (!Number.isInteger(parseInt(newValue))){
          this.error = true;
          this.message = 'لطفا فقط از اعداد استفاده کنید.'
        } else {
          this.error = false
          this.message = ''
        }
        newValue = this.formatNumber(newValue)
        this.inputValue = newValue
      }
      // if (this.type == 'phone'){
      //   let pattern =  /^((0?9)|(\+?989))\d{9}$/g
      //
      //   if (pattern.test(newValue) == false){
      //     this.error = true;
      //     this.message = 'فرمت شماره وارد شده صحیح نیست'
      //   } else {
      //     this.error = false
      //     this.message = ''
      //   }
      // }
      // if (this.type == 'comment'){
      //   let pattern =  /^(?!.*,)[\u0600-\u06FF\s]*$/;
      //   if (pattern.test(newValue) == false){
      //     this.error = true;
      //     this.message = 'لطفا از حروف فارسی بدون کاما استفاده کنید.'
      //   } else {
      //     this.error = false
      //     this.message = ''
      //   }
      // }
      this.$emit('update', newValue);
      this.$emit('InputError', this.error);
    },
  },
  watch: {
     value(newVal) {
        this.inputValue = newVal;
        // console.log(newVal, this.value, this.inputValue, this.type)
     }
  }
};
</script>

<template>
 <div class="relative" :class="[hidden ? 'hidden':'']">
    <input
      v-model="inputValue"
      @input="updateValue($event.target.value)"
      type="text"
      :id="formName"
      :disabled="disabled"
      :class="[
        error ? 'text-red-900 border-red-500 focus:border-red-500' : 'text-gray-900 focus:border-green-500 border-gray-300'
      ]"
      class="block px-2.5 pb-2.5 pt-4 w-full text-sm bg-transparent rounded-lg border-1 appearance-none focus:outline-none focus:ring-0 peer"
      placeholder=""
    />
    <label
      :for="formName"
      :class="[
        error ? 'peer-focus:text-red-500 text-red-500' : 'peer-focus:text-green-500 text-gray-500'
      ]"
      class="absolute text-sm dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1"
    >
      {{ label }}
    </label>
    <p v-if="error" class="mt-2 text-xs text-red-600 dark:text-red-400">{{message}}</p>
 </div>
</template>

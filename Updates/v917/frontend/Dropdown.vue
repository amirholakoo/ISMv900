<script>
export default {
  name: "Dropdown",
   props: {
      formName: {
        type: String,
        required: true
      },
     btnclass:{
        type: String,
        required: false
     },
      hidden:{
        type: Boolean,
        default: false,
     },
   },
   methods: {
     handleSelect() {
       // Close dropdown after selection
       const dropdownEl = document.getElementById(this.formName + 'dropdown1');
       if (dropdownEl) {
         dropdownEl.classList.add('hidden');
       }
     }
   }
};
</script>

<template>
  <div :class="[hidden ? 'hidden':'']">
    <button
        :id="formName + 'Button1'"
        :data-dropdown-toggle="formName+'dropdown1'"
        :class="btnclass"
        class="justify-between w-44 text-white bg-green-500 hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
        type="button"
    >
      <slot name="btnName"></slot>
      <svg class="w-2.5 h-2.5 ms-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
      </svg>
    </button>
    <!-- Dropdown menu -->
    <div :id="formName+'dropdown1'" class="z-50 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700" data-dropdown-toggle="false">
        <ul @click="handleSelect" class="overflow-y-auto h-auto max-h-48 py-2 text-sm text-gray-700 dark:text-gray-200" :aria-labelledby="formName + 'Button1'">
            <slot name="list"></slot>
        </ul>
    </div>
 </div>
</template>

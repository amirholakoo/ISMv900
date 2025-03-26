<script>
export default {
   name: "ModalButton",
   methods: {
      closeModal() {
        this.$emit('close');
      }
   }
};
</script>

<template>
 <button
    data-modal-hide="popup-modal"
    aria-label="Close"
    @click="closeModal"
    type="button"
    class="inline-flex justify-center w-full px-2 py-1.5 text-xs font-medium text-center text-white bg-green-500 hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-green-300 rounded-lg dark:bg-blue-500 dark:hover:bg-blue-600 dark:focus:ring-blue-800"
 >
    درسته
 </button>
</template>

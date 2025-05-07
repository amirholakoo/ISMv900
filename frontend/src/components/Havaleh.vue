<!-- havaleh.vue -->
<template>
  <div class="p-4 max-w-xl mx-auto">
    <h2 class="text-xl font-bold mb-4 text-center">فرم صدور حواله خروج</h2>

    <form @submit.prevent="submitForm">
      <div class="mb-2">
        <label>تاریخ:</label>
        <input v-model="form.date" class="border p-1 w-full" type="text">
      </div>
      <div class="mb-2">
        <label>شماره سریال:</label>
        <input v-model="form.serial" class="border p-1 w-full" type="text">
      </div>
      <div class="mb-2">
        <label>نام خریدار:</label>
        <input v-model="form.customer" class="border p-1 w-full" type="text">
      </div>
      <div class="mb-2">
        <label>آدرس:</label>
        <input v-model="form.address" class="border p-1 w-full" type="text">
      </div>

      <h3 class="mt-4 font-semibold">اقلام:</h3>
      <div v-for="(item, index) in form.items" :key="index" class="grid grid-cols-4 gap-2 mb-2">
        <input v-model="item.width" class="border p-1" placeholder="عرض">
        <input v-model="item.grammage" class="border p-1" placeholder="گرماژ">
        <input v-model="item.quantity" class="border p-1" placeholder="تعداد">
        <input v-model="item.weight" class="border p-1" placeholder="وزن">
      </div>

      <button type="button" class="bg-gray-200 px-3 py-1 rounded mb-3" @click="addItem">افزودن سطر</button>

      <div class="mb-2">
        <label>ملاحظات:</label>
        <input v-model="form.note" class="border p-1 w-full" type="text">
      </div>

      <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded">تولید PDF</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      form: {
        date: '',
        serial: '',
        customer: '',
        address: '',
        note: '',
        items: [
          { width: '', grammage: '', quantity: '', weight: '' }
        ]
      }
    };
  },
  methods: {
    addItem() {
      this.form.items.push({ width: '', grammage: '', quantity: '', weight: '' });
    },
    async submitForm() {
      try {
        console.log('Form data being sent:', this.form);
        const response = await axios.post('/myapp/api/havaleh-pdf/', this.form, {
          responseType: 'blob'
        });
        const blob = new Blob([response.data], { type: 'application/pdf' });
        const link = document.createElement('a');
        link.href = window.URL.createObjectURL(blob);
        link.download = 'havaleh.pdf';
        link.click();
      } catch (error) {
        console.error("خطا در تولید PDF:", error.response || error.message);
      }
    }
  }
};
</script>

<style scoped>
input {
  text-align: right;
}
</style>

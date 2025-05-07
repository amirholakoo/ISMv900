<template>
<div>
<!-- Invoice Header -->
<h1 class="text-center text-2xl font-bold mb-4">خرید</h1>

<!-- Invoice Form -->
<form @submit.prevent="generatePDF">
<div class="grid grid-cols-2 gap-4">
<div>
<label>ردیف</label>
<input type="text" v-model="invoice.row" class="border p-2 w-full" />
</div>
<div>
<label>نام کالا و مشخصات کالا</label>
<input type="text" v-model="invoice.product_name" class="border p-2 w-full" />
</div>
<div>
<label>گرماژ</label>
<input type="text" v-model="invoice.grammage" class="border p-2 w-full" />
</div>
<div>
<label>عرض کاغذ</label>
<input type="text" v-model="invoice.paper_width" class="border p-2 w-full" />
</div>
<div>
<label>نام خریدار</label>
<input type="text" v-model="invoice.buyer_name" class="border p-2 w-full" />
</div>
<div>
<label>تعداد/مقدار</label>
<input type="text" v-model="invoice.quantity" class="border p-2 w-full" />
</div>
<div>
<label>وزن کالا</label>
<input type="text" v-model="invoice.product_weight" class="border p-2 w-full" />
</div>
<div>
<label>ملاحظات</label>
<input type="text" v-model="invoice.notes" class="border p-2 w-full" />
</div>
<div>
<label>جمع</label>
<input type="text" v-model="invoice.total" class="border p-2 w-full" />
</div>
</div>

<!-- Signature Fields -->
<div class="mt-4">
<label>حسابداری</label>
<input type="text" v-model="invoice.accounting" class="border p-2 w-full" />
<label>انبارداری</label>
<input type="text" v-model="invoice.warehouse" class="border p-2 w-full" />
<label>مدیرفروش</label>
<input type="text" v-model="invoice.sales_manager" class="border p-2 w-full" />
<label>مدیریت کارخانه</label>
<input type="text" v-model="invoice.factory_manager" class="border p-2 w-full" />
<label>تحویل گیرنده</label>
<input type="text" v-model="invoice.receiver" class="border p-2 w-full" />
</div>

<div class="mt-4">
<label>بار صحیح و سالم تجویل اینجانب گردید</label>
<textarea v-model="invoice.end_statement" class="border p-2 w-full"></textarea>
</div>

<!-- Submit Button -->
<button type="submit" class="bg-blue-500 text-white px-4 py-2 mt-4">تولید PDF</button>
</form>

<!-- Invoice Preview -->
<div ref="pdfContent" class="mt-6 p-4 border">
<h2 class="text-center">Invoice Preview</h2>
<p><strong>ردیف:</strong> {{ invoice.row }}</p>
<p><strong>نام کالا و مشخصات کالا:</strong> {{ invoice.product_name }}</p>
<p><strong>گرماژ:</strong> {{ invoice.grammage }}</p>
<p><strong>عرض کاغذ:</strong> {{ invoice.paper_width }}</p>
<p><strong>نام خریدار:</strong> {{ invoice.buyer_name }}</p>
<p><strong>تعداد/مقدار:</strong> {{ invoice.quantity }}</p>
<p><strong>وزن کالا:</strong> {{ invoice.product_weight }}</p>
<p><strong>ملاحظات:</strong> {{ invoice.notes }}</p>
<p><strong>جمع:</strong> {{ invoice.total }}</p>
<p><strong>حسابداری:</strong> {{ invoice.accounting }}</p>
<p><strong>انبارداری:</strong> {{ invoice.warehouse }}</p>
<p><strong>مدیرفروش:</strong> {{ invoice.sales_manager }}</p>
<p><strong>مدیریت کارخانه:</strong> {{ invoice.factory_manager }}</p>
<p><strong>تحویل گیرنده:</strong> {{ invoice.receiver }}</p>
<p><strong>بار صحیح و سالم تجویل اینجانب:</strong> {{ invoice.end_statement }}</p>
</div>
</div>
</template>

<script>
import axios from 'axios';

export default {
data() {
return {
invoice: {
row: "",
product_name: "",
grammage: "",
paper_width: "",
buyer_name: "",
quantity: "",
product_weight: "",
notes: "",
total: "",
accounting: "",
warehouse: "",
sales_manager: "",
factory_manager: "",
receiver: "",
end_statement: ""
}
};
},
methods: {
async generatePDF() {
try {
const response = await axios.post('/myapp/api/generate-purchase-order-pdf/', this.invoice, {
responseType: 'blob'
});
const blob = new Blob([response.data], { type: 'application/pdf' });
const link = document.createElement('a');
link.href = window.URL.createObjectURL(blob);
link.download = 'purchase-order.pdf';
link.click();
} catch (error) {
console.error("خطا در تولید PDF:", error.response || error.message);
}
}
}
};
</script>

<style scoped>
form label {
display: block;
font-weight: bold;
margin-bottom: 0.5rem;
}
form input, form textarea {
margin-bottom: 1rem;
}
</style>

<template>
  <div class="sales-order-container">
    <!-- Form for user input -->
    <form @submit.prevent="submitForm">
      <div class="form-row">
        <label>شماره فاکتور:</label>
        <input v-model="form.serial" required />
        <label>تاریخ:</label>
        <input v-model="form.date" required />
      </div>
      <div class="form-row">
        <label>نام خریدار:</label>
        <input v-model="form.buyer_name" required />
        <label>شماره اقتصادی خریدار:</label>
        <input v-model="form.buyer_economic_code" />
      </div>
      <div class="form-row">
        <label>شماره ثبت خریدار:</label>
        <input v-model="form.buyer_reg" />
        <label>شماره پستی خریدار:</label>
        <input v-model="form.buyer_postcode" />
      </div>
      <div class="form-row">
        <label>مشخصات فروشنده:</label>
        <input v-model="form.seller_name" />
        <label>شماره اقتصادی فروشنده:</label>
        <input v-model="form.seller_economic_code" />
      </div>
      <div class="form-row">
        <label>شماره ثبت فروشنده:</label>
        <input v-model="form.seller_reg" />
        <label>شماره پستی فروشنده:</label>
        <input v-model="form.seller_postcode" />
      </div>
      <table class="input-table">
        <thead>
          <tr>
            <th>شرح کالا</th>
            <th>کد کالا</th>
            <th>تعداد</th>
            <th>واحد</th>
            <th>مبلغ واحد (ریال)</th>
            <th>مبلغ کل (ریال)</th>
            <th>ملاحظات</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, idx) in form.items" :key="idx">
            <td><input v-model="item.description" /></td>
            <td><input v-model="item.code" /></td>
            <td><input type="number" v-model.number="item.quantity" @input="updateTotal(item)" /></td>
            <td><input v-model="item.unit" /></td>
            <td><input type="number" v-model.number="item.price" @input="updateTotal(item)" /></td>
            <td>{{ formatNumber(item.total) }}</td>
            <td><input v-model="item.comment" /></td>
            <td><button type="button" @click="removeItem(idx)">-</button></td>
          </tr>
        </tbody>
      </table>
      <button type="button" @click="addItem">افزودن ردیف</button>
      <button type="submit" class="preview-btn">پیش نمایش</button>
    </form>

    <!-- Preview area for PDF/export -->
    <div ref="pdfPreview" v-if="showData" class="pdf-preview">
      <div class="invoice-main">
        <table class="invoice-table">
          <tr>
            <td class="cell-title" colspan="8">صورت حساب فروش کالا</td>
          </tr>
          <tr>
            <td colspan="2">شماره: {{ form.serial }}</td>
            <td colspan="2">تاریخ: {{ form.date }}</td>
            <td colspan="2">شماره ثبت فروشنده: {{ form.seller_reg }}</td>
            <td colspan="2">شماره اقتصادی فروشنده: {{ form.seller_economic_code }}</td>
          </tr>
          <tr>
            <td colspan="2">نام خریدار: {{ form.buyer_name }}</td>
            <td colspan="2">شماره اقتصادی خریدار: {{ form.buyer_economic_code }}</td>
            <td colspan="2">شماره ثبت خریدار: {{ form.buyer_reg }}</td>
            <td colspan="2">کد پستی خریدار: {{ form.buyer_postcode }}</td>
          </tr>
          <tr>
            <td colspan="2">نام فروشنده: {{ form.seller_name }}</td>
            <td colspan="2">کد پستی فروشنده: {{ form.seller_postcode }}</td>
            <td colspan="4">تلفن: 026-44388386</td>
          </tr>
          <tr class="header-row">
            <th>شرح کالا</th>
            <th>کد کالا</th>
            <th>تعداد</th>
            <th>واحد</th>
            <th>مبلغ واحد</th>
            <th>مبلغ کل</th>
            <th>ملاحظات</th>
          </tr>
          <tr v-for="item in form.items" :key="item.code + item.description">
            <td>{{ item.description }}</td>
            <td>{{ item.code }}</td>
            <td>{{ item.quantity }}</td>
            <td>{{ item.unit }}</td>
            <td>{{ formatNumber(item.price) }}</td>
            <td>{{ formatNumber(item.total) }}</td>
            <td>{{ item.comment }}</td>
          </tr>
          <tr>
            <td colspan="5" class="total-label">جمع کل</td>
            <td colspan="2" class="total-value">{{ formatNumber(totalAmount) }}</td>
          </tr>
        </table>
        <div class="footer-row">
          <div>مبلغ قابل پرداخت به حروف و عدد: ..........................................</div>
          <div>
            <span>امضا خریدار:</span> ....................................
            <span style="margin-right:40px;">امضا فروشنده:</span> ....................................
          </div>
        </div>
      </div>
    </div>
    <button type="button" @click="downloadPDF" v-if="showData">دریافت PDF</button>
  </div>
</template>

<script>

import html2pdf from "html2pdf.js";



export default {
  name: 'SalesOrder',
  data() {
    return {
      form: {
        serial: '',
        date: '',
        buyer_name: '',
        buyer_economic_code: '',
        buyer_reg: '',
        buyer_postcode: '',
        seller_name: '',
        seller_economic_code: '',
        seller_reg: '',
        seller_postcode: '',
        items: [
          { description: '', code: '', quantity: 1, unit: '', price: 0, total: 0, comment: '' }
        ]
      },
      showData: false
    }
  },
  computed: {
    totalAmount() {
      return this.form.items.reduce((sum, item) => sum + Number(item.total || 0), 0);
    }
  },
  methods: {
    updateTotal(item) {
      item.total = (parseFloat(item.quantity) || 0) * (parseFloat(item.price) || 0);
    },
    addItem() {
      this.form.items.push({ description: '', code: '', quantity: 1, unit: '', price: 0, total: 0, comment: '' });
    },
    removeItem(idx) {
      this.form.items.splice(idx, 1);
    },
    submitForm() {
    this.showData = true;
    // Don't generate the PDF here!
  },
  async downloadPDF() {
    // Wait for DOM update to finish before generating PDF
    await this.$nextTick();
    // Now generate the PDF
    html2pdf(this.$refs.pdfPreview, {
      margin: 0.2,
      filename: `sales_order_${this.form.serial}.pdf`,
      html2canvas: { scale: 2 },
      jsPDF: { orientation: "landscape", unit: "mm", format: "a4" }
    });
  },
    formatNumber(val) {
      if (val == null || val === '') return '';
      return Number(val).toLocaleString('en-US', { minimumFractionDigits: 0 });
    },
  }
}
</script>

<style scoped>
.sales-order-container {
  max-width: 1100px;
  margin: 0 auto;
  direction: rtl;
  font-family: Tahoma, Arial, sans-serif;
  background: #fafbfc;
}
.form-row {
  display: flex;
  gap: 1em;
  margin-bottom: 8px;
}
.input-table {
  width: 100%;
  border-collapse: collapse;
  margin: 1em 0;
}
.input-table th, .input-table td {
  border: 1px solid #aaa;
  padding: 0.3em;
  text-align: center;
}
.preview-btn {
  margin-top: 8px;
}
.pdf-preview {
  margin-top: 30px;
  background: #fff;
  padding: 24px;
  border-radius: 8px;
  box-shadow: 0 2px 8px #0001;
}
.invoice-main {
  width: 100%;
  margin: 0 auto;
  border: 2px solid #444;
  background: white;
  padding: 0;
}
.invoice-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 1em;
  margin-bottom: 16px;
}
.invoice-table th, .invoice-table td {
  border: 1.5px solid #444;
  padding: 6px 3px;
  text-align: center;
}
.invoice-table th {
  background: #ececec;
  font-weight: bold;
}
.cell-title {
  background: #e7e7e7;
  font-size: 1.3em;
  font-weight: bold;
  text-align: center;
}
.header-row th {
  background: #dedede;
}
.total-label {
  background: #e7e7e7;
  font-weight: bold;
}
.total-value {
  background: #ededed;
  font-weight: bold;
  font-size: 1.1em;
}
.footer-row {
  padding: 12px 10px;
  font-size: 1em;
  text-align: right;
  line-height: 2;
}
@media print {
  .sales-order-container {
    background: white !important;
  }
  .invoice-main {
    page-break-after: always;
  }
}
</style>
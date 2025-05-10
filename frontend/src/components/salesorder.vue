<template>
  <div class="sales-order-container">
    <!-- Form section (unchanged) -->
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
        <label>شماره ثبت خریدار:</label>
        <input v-model="form.buyer_reg" />
        <label>کد پستی خریدار:</label>
        <input v-model="form.buyer_postcode" />
        <label>تلفن خریدار:</label>
        <input v-model="form.buyer_phone" />
      </div>
      <div class="form-row">
        <label>نام فروشنده:</label>
        <input v-model="form.seller_name" />
        <label>شماره اقتصادی فروشنده:</label>
        <input v-model="form.seller_economic_code" />
        <label>شماره ثبت فروشنده:</label>
        <input v-model="form.seller_reg" />
        <label>کد پستی فروشنده:</label>
        <input v-model="form.seller_postcode" />
        <label>تلفن فروشنده:</label>
        <input v-model="form.seller_phone" />
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

    <!-- Invoice Preview for PDF -->
    <div ref="pdfPreview" v-if="showData" class="pdf-preview">
      <div class="invoice-main">
        <div class="invoice-title">صورت حساب فروش کالا</div>
        <table class="invoice-details-table">
          <tr>
            <td class="detail-title">مشخصات فروشنده</td>
            <td>نام فروشنده: {{ form.seller_name }}</td>
            <td>شماره اقتصادی: {{ form.seller_economic_code }}</td>
            <td>شماره ثبت: {{ form.seller_reg }}</td>
            <td>کد پستی: {{ form.seller_postcode }}</td>
            <td>تلفن: {{ form.seller_phone }}</td>
          </tr>
          <tr>
            <td class="detail-title">مشخصات خریدار</td>
            <td>نام خریدار: {{ form.buyer_name }}</td>
            <td>شماره اقتصادی: {{ form.buyer_economic_code }}</td>
            <td>شماره ثبت: {{ form.buyer_reg }}</td>
            <td>کد پستی: {{ form.buyer_postcode }}</td>
            <td>تلفن: {{ form.buyer_phone }}</td>
          </tr>
          <tr>
            <td class="detail-title">شماره فاکتور</td>
            <td colspan="2">{{ form.serial }}</td>
            <td class="detail-title">تاریخ</td>
            <td colspan="2">{{ form.date }}</td>
          </tr>
        </table>
        <table class="invoice-table">
          <thead>
            <tr>
              <th>شرح کالا</th>
              <th>کد کالا</th>
              <th>تعداد</th>
              <th>واحد</th>
              <th>مبلغ واحد</th>
              <th>مبلغ کل</th>
              <th>ملاحظات</th>
            </tr>
          </thead>
          <tbody>
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
          </tbody>
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
        buyer_phone: '',
        seller_name: '',
        seller_economic_code: '',
        seller_reg: '',
        seller_postcode: '',
        seller_phone: '',
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
    },
    formatNumber(val) {
      if (val == null || val === '') return '';
      return Number(val).toLocaleString('en-US', { minimumFractionDigits: 0 });
    },
    async downloadPDF() {
      await this.$nextTick();
      html2pdf(this.$refs.pdfPreview, {
        margin: 0.2,
        filename: `sales_order_${this.form.serial}.pdf`,
        html2canvas: { scale: 2 },
        jsPDF: { orientation: "landscape", unit: "mm", format: "a4" }
      });
    }
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
  flex-wrap: wrap;
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
.invoice-title {
  text-align: center;
  font-size: 1.6em;
  font-weight: bold;
  margin: 30px 0 18px 0;
  letter-spacing: 1px;
}
.invoice-details-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 16px;
  font-size: 1em;
}
.invoice-details-table td {
  border: 1px solid #888;
  padding: 6px 10px;
  text-align: right;
  background: #f6f6f6;
}
.invoice-details-table .detail-title {
  background: #e7e7e7;
  font-weight: bold;
  text-align: center;
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
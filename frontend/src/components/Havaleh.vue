<template>
  <div class="havaleh-form">
    <h2>حواله خروج از انبار</h2>
    <div class="form-header">
      <div class="form-group">
        <label>تاریخ ارسال:</label>
        <input type="text" v-model="formData.date" readonly />
      </div>
      <div class="form-group">
        <label>شماره سریال:</label>
        <input type="text" v-model="formData.serial" />
      </div>
    </div>

    <!-- Items Table -->
    <div class="items-table">
      <table>
        <thead>
          <tr>
            <th>ردیف</th>
            <th>نام کالا و مشخصات کالا</th>
            <th>گرماژ</th>
            <th>عرض کاغذ</th>
            <th>نام خریدار</th>
            <th>تعداد / مقدار</th>
            <th>وزن کالا</th>
            <th>عملیات</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in formData.items" :key="index">
            <td>{{ index + 1 }}</td>
            <td>
              <input type="text" v-model="item.name" />
            </td>
            <td>
              <input type="text" v-model="item.gsm" />
            </td>
            <td>
              <input type="text" v-model="item.width" />
            </td>
            <td>
              <input type="text" v-model="item.buyer" />
            </td>
            <td>
              <input type="number" v-model="item.quantity" />
            </td>
            <td>
              <input type="number" v-model="item.weight" />
            </td>
            <td>
              <button @click="removeItem(index)" class="remove-btn">حذف</button>
            </td>
          </tr>
        </tbody>
      </table>
      <button @click="addItem" class="add-btn">افزودن ردیف جدید</button>
    </div>

    <div class="form-footer">
      <div class="form-group">
        <label>ملاحظات:</label>
        <textarea v-model="formData.note"></textarea>
      </div>
      <div class="total-weight">
        <strong>جمع کل وزن:</strong> {{ calculateTotalWeight() }}
      </div>
      <button @click="generatePDF" class="generate-btn">تولید PDF</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Havaleh',
  data() {
    return {
      formData: {
        date: this.getCurrentDate(), // Initialize date here
        serial: '',
        items: [],
        note: ''
      }
    }
  },
  created() {
    // If you want to update the date when component is created
    this.formData.date = this.getCurrentDate();
  },
  methods: {
    getCurrentDate() {
      // Convert to Iranian date format
      const today = new Date();
      // Format: YYYY/MM/DD
      const year = today.getFullYear();
      const month = String(today.getMonth() + 1).padStart(2, '0');
      const day = String(today.getDate()).padStart(2, '0');
      return `${year}/${month}/${day}`;
    },
    addItem() {
      this.formData.items.push({
        name: '',
        gsm: '',
        width: '',
        buyer: '',
        quantity: '',
        weight: ''
      });
    },
    removeItem(index) {
      this.formData.items.splice(index, 1);
    },
    calculateTotalWeight() {
      return this.formData.items.reduce((total, item) => {
        return total + (parseFloat(item.weight) || 0);
      }, 0).toLocaleString();
    },
    async generatePDF() {
      try {
        const requestData = {
          date: this.formData.date,
          serial: this.formData.serial,
          items: this.formData.items,
          note: this.formData.note
        };

        console.log('Form data being sent:', requestData);

        const response = await fetch('/myapp/api/havaleh-pdf/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': this.getCookie('csrftoken'),
          },
          body: JSON.stringify(requestData),
          credentials: 'include'
        });

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.error || 'Error generating PDF');
        }

        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `havaleh_${this.formData.serial}.pdf`;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);

      } catch (error) {
        console.error('خطا در تولید PDF:', error);
        alert('خطا در تولید PDF: ' + error.message);
      }
    },
    getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }
  }
}
</script>

<style scoped>
/* ... Your existing styles ... */
</style>
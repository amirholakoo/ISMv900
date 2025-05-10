<template>
  <div>
    <router-link to="/myapp/invoice/havaleh" class="btn btn-primary">havaleh</router-link>
    <router-link to="/myapp/invoice/sales-order" class="btn btn-secondary">sales order</router-link>
    <router-link to="/myapp/invoice/purchaseorder" class="btn btn-danger">purchases</router-link>
  </div>
</template>

<script>
export default {
  name: 'Invoice',
}
</script>

<style scoped>
.btn {
  margin: 5px;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  display: inline-block;
}
.btn-primary {
  background-color: #007bff;
  color: white;
}
.btn-secondary {
  background-color: #6c757d;
  color: white;
}
.btn-danger {
  background-color: #dc3545;
  color: white;
}
</style>

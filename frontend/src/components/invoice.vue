<script>
import HomeView from "@/views/HomeView.vue";
import addTruck from "@/components/addTruck.vue";
import addSupplier from "@/components/addSupplier.vue";
import addCustomer from "@/components/addCustomer.vue";
import addRawMaterial from "@/components/addRawMaterial.vue";
import addNewReel from "@/components/addNewReel.vue";
import forkliftPanel from "@/components/forkliftPanel.vue";
import createShipment from "@/components/createShipment.vue";
import sales from "@/components/weightStation/sales.vue";
import purchase from "@/components/weightStation/purchase.vue";
import weight1 from "@/components/weightStation/weight1.vue";
import weight2 from "@/components/weightStation/weight2.vue";
import weightStationPanel from "@/components/weightStation/weightStationPanel.vue";
import addNewAnbar from "@/components/admin/addNewAnbar.vue";
import addNewUnit from "@/components/admin/addNewUnit.vue";
import addNewMatrialType from "@/components/admin/addNewMatrialType.vue";
import consumptionProfile from "@/components/admin/consumptionProfile.vue";
import cancel from "@/components/admin/cancel.vue";
import reportPage from "@/components/admin/reportPage.vue";
import Card from "@/components/Card.vue";

export default {
  name: "AllPages",
  components: { Card },
  data() {
    return {
      routes: [
        { path: '/myapp/addTruck/', name: 'addTruck' },
        { path: '/myapp/addSupplier/', name: 'addSupplier' },
        { path: '/myapp/addCustomer/', name: 'addCustomer' },
        { path: '/myapp/addRawMaterial/', name: 'addRawMaterial' },
        { path: '/myapp/addNewReel/', name: 'addNewReel' },
        { path: '/myapp/forkliftPanel/', name: 'forkliftPanel' },
        { path: '/myapp/addShipment/', name: 'addShipment' },
        { path: '/myapp/createSalesOrder/', name: 'createSalesOrder' },
        { path: '/myapp/createPurchaseOrder/', name: 'createPurchaseOrder' },
        { path: '/myapp/weightStationPanel/', name: 'weightStationPanel' },
        { path: '/myapp/addNewAnbar/', name: 'addNewAnbar' },
        { path: '/myapp/addUnit/', name: 'addNewUnit' },
        { path: '/myapp/addMaterialType/', name: 'addNewMatrialType' },
        { path: '/myapp/addConsumptionProfile/', name: 'addConsumptionProfile' },
        { path: '/myapp/cancel/', name: 'cancel' },
        { path: '/myapp/report/', name: 'report' },
        { path: '/myapp/ProductsPage/', name: 'ProductsPage' },
        { path: '/myapp/invoice/', name: 'Invoice' } // Added the Invoice button
      ]
    }
  }
}
</script>

<template>
  <Card title="All Pages">
    <div class="flex flex-col gap-2 justify-center items-center">
      <template v-for="route in routes" :key="route.name">
        <router-link
          :to="route.path"
          type="button"
          class="w-44 block text-white bg-green-500 hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
        >
          {{ route.name }}
        </router-link>
      </template>
    </div>
  </Card>
</template>

<style scoped>
</style>
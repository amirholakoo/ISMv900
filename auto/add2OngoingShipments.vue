<template>
  <Card title="Ongoing Shipments">
    <Alert v-if="error" type="error" :messages="errors"></Alert>
    <div v-if="shipments.length > 0">
      <table class="min-w-full divide-y divide-gray-200">
        <thead class="bg-gray-50">
          <tr>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
              Shipment ID
            </th>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
              Type
            </th>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
              Status
            </th>
            <!-- Add more headers based on the data you want to display -->
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="shipment in shipments" :key="shipment.id">
            <td class="px-6 py-4 whitespace-nowrap">
              {{ shipment.id }}
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              {{ shipment.shipment_type }}
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              {{ shipment.status }}
            </td>
            <!-- Add more data cells based on the data you want to display -->
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else>
      <p>No ongoing shipments found.</p>
    </div>
  </Card>
</template>

<script>
import Card from './Card'
import Alert from "@/components/Alert.vue";

export default {
  name: "OngoingShipments",
  components: {
    Card, Alert
  },
  data() {
    return {
      shipments: [],
      error: false,
      errors: [],
    }
  },
  created() {
    this.fetchOngoingShipments();
  },
  methods: {
    async fetchOngoingShipments() {
      try {
        const response = await this.axios.get('/myapp/fetch_ongoing_shipments/');
        if (response.data.status === 'success') {
          this.shipments = response.data.shipments;
        } else {
          this.error = true;
          this.errors = response.data.errors;
        }
      } catch (e) {
        this.error = true;
        this.errors.push({ message: "An error occurred while fetching the data." });
      }
    },
  },
}
</script>

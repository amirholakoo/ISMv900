<script>
import modal from "@/components/Modal.vue";
import Alert from "@/components/Alert.vue";
import Card from "@/components/Card.vue";
import {initFlowbite} from "flowbite";
import Weight1 from "@/components/weightStation/weight1.vue";
import Weight2 from "@/components/weightStation/weight2.vue";

export default {
  name: "weightStationPanel",
  components: {
    Weight2,
    Weight1,
    modal,
    Alert,
    Card,
  },
  data(){
    return {
      btnPanel: true,
      btns: [
          {
            name: 'وزن اولیه',
            isActive: false
          },
          {
            name: 'وزن ثانویه',
            isActive: false
          },
      ]
    }
  },
  methods:{
    activePanel(panel){
      for (let i = 0; i < this.btns.length; i++) {
          if (panel.name == this.btns[i].name){
            this.btns[i].isActive = true
            this.btnPanel = false
          } else {
            this.btns[i].isActive = false
          }
      }
    },
    backToPanel(){
      for (let i = 0; i < this.btns.length; i++) {
          if (this.btns[i].isActive) {
            this.btns[i].isActive = false
            this.btnPanel = true
          }
      }
    },
  },
  mounted() {
    initFlowbite();
  }
}
</script>

<template>
  <Card v-if="btnPanel" title="پنل ایستگاه وزن کشی">
    <div class="flex flex-col gap-2 justify-center items-center">
      <button v-for="btn in btns" @click="activePanel(btn)" type="button" class="inline-flex justify-center w-48 px-2 py-1.5 text-sm font-medium text-center rounded-lg text-white   bg-green-500 hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-green-300">
        {{btn.name}}
      </button>
    </div>
  </Card>
  <template v-else>
    <template v-for="panel in btns">
      <template v-if="panel.isActive==true">
        <Card :title="panel.name" v-if="panel.name=='وزن اولیه'">
          <div class="flex flex-col gap-2 justify-center items-center">
            <weight1></weight1>
            <button @click="backToPanel" type="button" class="inline-flex justify-center w-48 px-2 py-1.5 text-sm font-medium text-center text-white bg-rose-600 rounded-lg hover:bg-rose-700 focus:ring-4 focus:outline-none focus:ring-rose-300 dark:bg-rose-500 dark:hover:bg-rose-600 dark:focus:ring-rose-800">
              بازگشت به پنل
            </button>
          </div>
        </Card>
        <Card :title="panel.name" v-if="panel.name=='وزن ثانویه'">
          <div class="flex flex-col gap-2 justify-center items-center">
            <weight2></weight2>
            <button @click="backToPanel" type="button" class="inline-flex justify-center w-48 px-2 py-1.5 text-sm font-medium text-center text-white bg-rose-600 rounded-lg hover:bg-rose-700 focus:ring-4 focus:outline-none focus:ring-rose-300 dark:bg-rose-500 dark:hover:bg-rose-600 dark:focus:ring-rose-800">
              بازگشت به پنل
            </button>
          </div>
        </Card>
      </template>
    </template>
  </template>
</template>

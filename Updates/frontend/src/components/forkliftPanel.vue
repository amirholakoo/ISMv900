<script>
import modal from "@/components/Modal.vue";
import Alert from "@/components/Alert.vue";
import Card from "@/components/Card.vue";
import {initFlowbite} from "flowbite";
import Unloaded from "@/components/forkliftPages/unloaded.vue";
import Loaded from "@/components/forkliftPages/loaded.vue";
import Returned from "@/components/forkliftPages/retrned.vue";
import Moved from "@/components/forkliftPages/moved.vue";
import Used from "@/components/forkliftPages/used.vue";

export default {
  name: "forkliftPanel",
  components: {
    Used,
    Moved,
    Returned,
    Loaded,
    Unloaded,
    modal,
    Alert,
    Card,
  },
  data(){
    return {
      btnPanel: true,
      btns: [
          {
            name: 'تخلیه شده',
            isActive: false
          },
          {
            name: 'بارگیری شده',
            isActive: false
          },
          {
            name: 'مصرف شده',
            isActive: false
          },
          {
            name: 'جا به جا شده',
            isActive: false
          },
          {
            name: 'برگشت داده شده',
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
  <Card v-if="btnPanel" title="پنل forklift">
    <div class="flex flex-col gap-2 justify-center items-center">
      <button v-for="btn in btns" @click="activePanel(btn)" type="button" class="w-44 block text-white bg-green-500 hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
        {{btn.name}}
      </button>
    </div>
  </Card>
  <template v-else>
    <template v-for="panel in btns">
      <template v-if="panel.isActive==true">
        <Card :title="panel.name" v-if="panel.name=='تخلیه شده'">
          <div class="flex flex-col gap-2 justify-center items-center">
            <unloaded></unloaded>
            <button @click="backToPanel" type="button" class="inline-flex justify-center w-48 px-2 py-1.5 text-sm font-medium text-center text-white bg-rose-600 rounded-lg hover:bg-rose-700 focus:ring-4 focus:outline-none focus:ring-rose-300 dark:bg-rose-500 dark:hover:bg-rose-600 dark:focus:ring-rose-800">
              بازگشت به پنل فرک لیفت
            </button>
          </div>
        </Card>
        <Card :title="panel.name" v-if="panel.name=='بارگیری شده'">
          <div class="flex flex-col gap-2 justify-center items-center">
            <loaded></loaded>
            <button @click="backToPanel" type="button" class="inline-flex justify-center w-48 px-2 py-1.5 text-sm font-medium text-center text-white bg-rose-600 rounded-lg hover:bg-rose-700 focus:ring-4 focus:outline-none focus:ring-rose-300 dark:bg-rose-500 dark:hover:bg-rose-600 dark:focus:ring-rose-800">
              بازگشت به پنل فرک لیفت
            </button>
          </div>
        </Card>
        <Card :title="panel.name" v-if="panel.name=='مصرف شده'">
          <div class="flex flex-col gap-2 justify-center items-center">
            <used></used>
            <button @click="backToPanel" type="button" class="inline-flex justify-center w-48 px-2 py-1.5 text-sm font-medium text-center text-white bg-rose-600 rounded-lg hover:bg-rose-700 focus:ring-4 focus:outline-none focus:ring-rose-300 dark:bg-rose-500 dark:hover:bg-rose-600 dark:focus:ring-rose-800">
              بازگشت به پنل فرک لیفت
            </button>
          </div>
        </Card>
        <Card :title="panel.name" v-if="panel.name=='جا به جا شده'">
          <div class="flex flex-col gap-2 justify-center items-center">
            <moved></moved>
            <button @click="backToPanel" type="button" class="inline-flex justify-center w-48 px-2 py-1.5 text-sm font-medium text-center text-white bg-rose-600 rounded-lg hover:bg-rose-700 focus:ring-4 focus:outline-none focus:ring-rose-300 dark:bg-rose-500 dark:hover:bg-rose-600 dark:focus:ring-rose-800">
              بازگشت به پنل فرک لیفت
            </button>
          </div>
        </Card>
        <Card :title="panel.name" v-if="panel.name=='برگشت داده شده'">
          <div class="flex flex-col gap-2 justify-center items-center">
            <returned></returned>
            <button @click="backToPanel" type="button" class="inline-flex justify-center w-48 px-2 py-1.5 text-sm font-medium text-center text-white bg-rose-600 rounded-lg hover:bg-rose-700 focus:ring-4 focus:outline-none focus:ring-rose-300 dark:bg-rose-500 dark:hover:bg-rose-600 dark:focus:ring-rose-800">
              بازگشت به پنل فرک لیفت
            </button>
          </div>
        </Card>
      </template>
    </template>
  </template>
</template>

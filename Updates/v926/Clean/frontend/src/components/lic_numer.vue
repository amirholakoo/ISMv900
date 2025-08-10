<script>
export default {
  name: "lic_numer",
  props: ['lic']
}
</script>

<template>
  <div class="flex flex-row justify-center">
      <div class="rounded-lg bg-white shadow-lg max-w-44">
      <div class="flex rounded-lg border-2 border-black shadow">
        <label class="flex flex-none flex-col items-center px-1 border-e-2 border-black font-bold text-sm">
          ایران
          <p class="place-self-center text-sm">{{ lic.year }}</p>
        </label>
        <label class="flex-grow flex flex-row gap-1 justify-center items-center p-1 font-mono text-md font-bold">
          <h>{{ lic.second }}</h>
          <h>{{ lic.letter }}</h>
          <h>{{ lic.first }}</h>
        </label>
        <label class="flex flex-none flex-col items-end justify-between p-1 bg-blue-700 border-s-2 border-black text-white text-sm text-bold">
          <img src="@/assets/Flag_of_Iran.svg.png" class="h-3">
          IR
<!--          <span class="flex flex-col items-end">-->
<!--            <p>IR</p>-->
<!--            <p>IRAN</p>-->
<!--          </span>-->
<!--          <p>ایران</p>-->
        </label>
      </div>
    </div>
  </div>
</template>


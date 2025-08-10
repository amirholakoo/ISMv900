<script>
export default {
  name: "Card",
  props: ['title', "bgTitle"],
}
</script>

<template>
<!--  card-->
<div class="flex flex-col items-center w-full h-full p-6 gap-4 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
  <header class="flex flex-none items-center self-start gap-2 text-gray-900 dark:text-gray-200">
    <div class="h-10 w-5 rounded rounded-md" :class="[bgTitle ? bgTitle : 'bg-green-500',]"></div>
    <strong>{{ title }}</strong>
  </header>
  <hr class="border-0 w-full h-px bg-gray-200 shadow">
  <main class="flex-grow w-full"><slot></slot></main>
  <footer class="w-full flex flex-row justify-center">
    <span class="flex w-16 h-3 bg-gray-200 dark:bg-gray-700 rounded-md"></span>
  </footer>
</div>
</template>

<style scoped>

</style>
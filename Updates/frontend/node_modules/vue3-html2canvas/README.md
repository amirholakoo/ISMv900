# Vue Html2Canvas
This project References from [vue-html2canvas](https://github.com/mycurelabs/vue-html2canvas) 

A [html2canvas](https://html2canvas.hertzen.com/) plugin for vue 3.x 


## Install

`yarn add vue3-html2canvas`

OR

`npm install vue3-html2canvas`

in `main.(js|ts)`

```js
import { createApp } from 'vue';
import { Html2CanvasPlugin } from 'vue3-html2canvas';
import App from './App.vue';

const app = createApp(App);
//...
app.use(Html2CanvasPlugin);
//...
app.mount('#app');
```

## Example

```vue
<script setup>
import { ref } from "vue";
import { useHtml2Canvas } from "vue3-html2canvas";

const html2canvas = useHtml2Canvas();
const canvasTarget = ref(null);
const containerShowCanvas = ref(null);
async function onGenHtmlToCanvas() {
  const canvas = await html2canvas(canvasTarget.value, { });
  containerShowCanvas.value.appendChild(canvas)
}
</script>

<template>
  <button @click="onGenHtmlToCanvas" ref="canvasTarget">Click here for download demo pdf</button>
  <div ref="containerShowCanvas" style="display: flex;justify-content: center;align-items: center;flex-direction: column;">
    <span>Result Of Canvas </span>
  </div>
</template>

<template>
  <button @click="onGenPDF">Click here for download demo pdf</button>
</template>
```

### Documentation

**Check [html2canvas Documentation](https://html2canvas.hertzen.com/documentation) for more explanations!**
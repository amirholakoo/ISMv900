"use strict";
/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(typeof self !== 'undefined' ? self : this)["webpackHotUpdatefrontend"]("app",{

/***/ "./node_modules/babel-loader/lib/index.js??clonedRuleSet-40.use[0]!./node_modules/vue-loader/dist/index.js??ruleSet[0].use[0]!./src/components/QRCodeComponent.vue?vue&type=script&lang=js":
/*!*************************************************************************************************************************************************************************************************!*\
  !*** ./node_modules/babel-loader/lib/index.js??clonedRuleSet-40.use[0]!./node_modules/vue-loader/dist/index.js??ruleSet[0].use[0]!./src/components/QRCodeComponent.vue?vue&type=script&lang=js ***!
  \*************************************************************************************************************************************************************************************************/
/***/ (function(__unused_webpack_module, __webpack_exports__, __webpack_require__) {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var qrcode__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! qrcode */ \"./node_modules/qrcode/lib/browser.js\");\n\n/* harmony default export */ __webpack_exports__[\"default\"] = ({\n  name: \"QRCodeComponent\",\n  data() {\n    return {\n      qrCodeData: 'Your data here' // Replace this with your actual data\n    };\n  },\n  mounted() {\n    this.generateQRCode();\n  },\n  methods: {\n    async generateQRCode() {\n      try {\n        await qrcode__WEBPACK_IMPORTED_MODULE_0__.toCanvas(this.$refs.qrCodeContainer, this.qrCodeData);\n      } catch (error) {\n        console.error(error);\n      }\n    },\n    async printQRCode() {\n      let qr = await qrcode__WEBPACK_IMPORTED_MODULE_0__.toDataURL(this.qrCodeData);\n      console.log(qr);\n      var printWin = window.open('', '');\n      printWin.document.open();\n      printWin.document.write(qr);\n      printWin.document.close();\n      printWin.focus();\n      printWin.print();\n      printWin.close();\n    }\n  }\n});//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9ub2RlX21vZHVsZXMvYmFiZWwtbG9hZGVyL2xpYi9pbmRleC5qcz8/Y2xvbmVkUnVsZVNldC00MC51c2VbMF0hLi9ub2RlX21vZHVsZXMvdnVlLWxvYWRlci9kaXN0L2luZGV4LmpzPz9ydWxlU2V0WzBdLnVzZVswXSEuL3NyYy9jb21wb25lbnRzL1FSQ29kZUNvbXBvbmVudC52dWU/dnVlJnR5cGU9c2NyaXB0Jmxhbmc9anMiLCJtYXBwaW5ncyI6Ijs7QUFDQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vZnJvbnRlbmQvLi9zcmMvY29tcG9uZW50cy9RUkNvZGVDb21wb25lbnQudnVlPzU2MjEiXSwic291cmNlc0NvbnRlbnQiOlsiPHNjcmlwdD5cclxuaW1wb3J0IFFSQ29kZSBmcm9tICdxcmNvZGUnO1xyXG5cclxuZXhwb3J0IGRlZmF1bHQge1xyXG4gIG5hbWU6IFwiUVJDb2RlQ29tcG9uZW50XCIsXHJcbiBkYXRhKCkge1xyXG4gICAgcmV0dXJuIHtcclxuICAgICAgcXJDb2RlRGF0YTogJ1lvdXIgZGF0YSBoZXJlJywgLy8gUmVwbGFjZSB0aGlzIHdpdGggeW91ciBhY3R1YWwgZGF0YVxyXG4gICAgfTtcclxuIH0sXHJcbiBtb3VudGVkKCkge1xyXG4gICAgdGhpcy5nZW5lcmF0ZVFSQ29kZSgpO1xyXG4gfSxcclxuIG1ldGhvZHM6IHtcclxuICAgIGFzeW5jIGdlbmVyYXRlUVJDb2RlKCkge1xyXG4gICAgICB0cnkge1xyXG4gICAgICAgIGF3YWl0IFFSQ29kZS50b0NhbnZhcyh0aGlzLiRyZWZzLnFyQ29kZUNvbnRhaW5lciwgdGhpcy5xckNvZGVEYXRhKTtcclxuICAgICAgfSBjYXRjaCAoZXJyb3IpIHtcclxuICAgICAgICBjb25zb2xlLmVycm9yKGVycm9yKTtcclxuICAgICAgfVxyXG4gICAgfSxcclxuICAgIGFzeW5jIHByaW50UVJDb2RlKCkge1xyXG4gICAgICBsZXQgcXIgPSBhd2FpdCBRUkNvZGUudG9EYXRhVVJMKHRoaXMucXJDb2RlRGF0YSlcclxuICAgICAgY29uc29sZS5sb2cocXIpXHJcbiAgICAgIHZhciBwcmludFdpbiA9IHdpbmRvdy5vcGVuKCcnLCcnKTtcclxuICAgICAgcHJpbnRXaW4uZG9jdW1lbnQub3BlbigpO1xyXG4gICAgICBwcmludFdpbi5kb2N1bWVudC53cml0ZShxcik7XHJcbiAgICAgIHByaW50V2luLmRvY3VtZW50LmNsb3NlKCk7XHJcbiAgICAgIHByaW50V2luLmZvY3VzKCk7XHJcbiAgICAgIHByaW50V2luLnByaW50KCk7XHJcbiAgICAgIHByaW50V2luLmNsb3NlKCk7XHJcbiAgICB9LFxyXG4gfSxcclxufTtcclxuPC9zY3JpcHQ+XHJcblxyXG48dGVtcGxhdGU+XHJcbiA8ZGl2PlxyXG4gICAgPGNhbnZhcyByZWY9XCJxckNvZGVDb250YWluZXJcIj48L2NhbnZhcz5cclxuICAgIDxidXR0b24gQGNsaWNrPVwicHJpbnRRUkNvZGVcIj5QcmludCBRUiBDb2RlPC9idXR0b24+XHJcbiA8L2Rpdj5cclxuPC90ZW1wbGF0ZT5cclxuXHJcbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///./node_modules/babel-loader/lib/index.js??clonedRuleSet-40.use[0]!./node_modules/vue-loader/dist/index.js??ruleSet[0].use[0]!./src/components/QRCodeComponent.vue?vue&type=script&lang=js\n");

/***/ }),

/***/ "./node_modules/babel-loader/lib/index.js??clonedRuleSet-40.use[0]!./node_modules/vue-loader/dist/templateLoader.js??ruleSet[1].rules[3]!./node_modules/vue-loader/dist/index.js??ruleSet[0].use[0]!./src/components/QRCodeComponent.vue?vue&type=template&id=6beabf8f":
/*!*****************************************************************************************************************************************************************************************************************************************************************************!*\
  !*** ./node_modules/babel-loader/lib/index.js??clonedRuleSet-40.use[0]!./node_modules/vue-loader/dist/templateLoader.js??ruleSet[1].rules[3]!./node_modules/vue-loader/dist/index.js??ruleSet[0].use[0]!./src/components/QRCodeComponent.vue?vue&type=template&id=6beabf8f ***!
  \*****************************************************************************************************************************************************************************************************************************************************************************/
/***/ (function(__unused_webpack_module, __webpack_exports__, __webpack_require__) {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   render: function() { return /* binding */ render; }\n/* harmony export */ });\n/* harmony import */ var vue__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! vue */ \"./node_modules/vue/dist/vue.runtime.esm-bundler.js\");\n\nconst _hoisted_1 = {\n  ref: \"qrCodeContainer\"\n};\nfunction render(_ctx, _cache, $props, $setup, $data, $options) {\n  return (0,vue__WEBPACK_IMPORTED_MODULE_0__.openBlock)(), (0,vue__WEBPACK_IMPORTED_MODULE_0__.createElementBlock)(\"div\", null, [(0,vue__WEBPACK_IMPORTED_MODULE_0__.createElementVNode)(\"canvas\", _hoisted_1, null, 512 /* NEED_PATCH */), (0,vue__WEBPACK_IMPORTED_MODULE_0__.createElementVNode)(\"button\", {\n    onClick: _cache[0] || (_cache[0] = (...args) => $options.printQRCode && $options.printQRCode(...args))\n  }, \"Print QR Code\")]);\n}//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9ub2RlX21vZHVsZXMvYmFiZWwtbG9hZGVyL2xpYi9pbmRleC5qcz8/Y2xvbmVkUnVsZVNldC00MC51c2VbMF0hLi9ub2RlX21vZHVsZXMvdnVlLWxvYWRlci9kaXN0L3RlbXBsYXRlTG9hZGVyLmpzPz9ydWxlU2V0WzFdLnJ1bGVzWzNdIS4vbm9kZV9tb2R1bGVzL3Z1ZS1sb2FkZXIvZGlzdC9pbmRleC5qcz8/cnVsZVNldFswXS51c2VbMF0hLi9zcmMvY29tcG9uZW50cy9RUkNvZGVDb21wb25lbnQudnVlP3Z1ZSZ0eXBlPXRlbXBsYXRlJmlkPTZiZWFiZjhmIiwibWFwcGluZ3MiOiI7Ozs7Ozs7QUFzQ0E7QUFBQTs7QUFEQTtBQUVBO0FBQUEiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9mcm9udGVuZC8uL3NyYy9jb21wb25lbnRzL1FSQ29kZUNvbXBvbmVudC52dWU/NTYyMSJdLCJzb3VyY2VzQ29udGVudCI6WyI8c2NyaXB0PlxyXG5pbXBvcnQgUVJDb2RlIGZyb20gJ3FyY29kZSc7XHJcblxyXG5leHBvcnQgZGVmYXVsdCB7XHJcbiAgbmFtZTogXCJRUkNvZGVDb21wb25lbnRcIixcclxuIGRhdGEoKSB7XHJcbiAgICByZXR1cm4ge1xyXG4gICAgICBxckNvZGVEYXRhOiAnWW91ciBkYXRhIGhlcmUnLCAvLyBSZXBsYWNlIHRoaXMgd2l0aCB5b3VyIGFjdHVhbCBkYXRhXHJcbiAgICB9O1xyXG4gfSxcclxuIG1vdW50ZWQoKSB7XHJcbiAgICB0aGlzLmdlbmVyYXRlUVJDb2RlKCk7XHJcbiB9LFxyXG4gbWV0aG9kczoge1xyXG4gICAgYXN5bmMgZ2VuZXJhdGVRUkNvZGUoKSB7XHJcbiAgICAgIHRyeSB7XHJcbiAgICAgICAgYXdhaXQgUVJDb2RlLnRvQ2FudmFzKHRoaXMuJHJlZnMucXJDb2RlQ29udGFpbmVyLCB0aGlzLnFyQ29kZURhdGEpO1xyXG4gICAgICB9IGNhdGNoIChlcnJvcikge1xyXG4gICAgICAgIGNvbnNvbGUuZXJyb3IoZXJyb3IpO1xyXG4gICAgICB9XHJcbiAgICB9LFxyXG4gICAgYXN5bmMgcHJpbnRRUkNvZGUoKSB7XHJcbiAgICAgIGxldCBxciA9IGF3YWl0IFFSQ29kZS50b0RhdGFVUkwodGhpcy5xckNvZGVEYXRhKVxyXG4gICAgICBjb25zb2xlLmxvZyhxcilcclxuICAgICAgdmFyIHByaW50V2luID0gd2luZG93Lm9wZW4oJycsJycpO1xyXG4gICAgICBwcmludFdpbi5kb2N1bWVudC5vcGVuKCk7XHJcbiAgICAgIHByaW50V2luLmRvY3VtZW50LndyaXRlKHFyKTtcclxuICAgICAgcHJpbnRXaW4uZG9jdW1lbnQuY2xvc2UoKTtcclxuICAgICAgcHJpbnRXaW4uZm9jdXMoKTtcclxuICAgICAgcHJpbnRXaW4ucHJpbnQoKTtcclxuICAgICAgcHJpbnRXaW4uY2xvc2UoKTtcclxuICAgIH0sXHJcbiB9LFxyXG59O1xyXG48L3NjcmlwdD5cclxuXHJcbjx0ZW1wbGF0ZT5cclxuIDxkaXY+XHJcbiAgICA8Y2FudmFzIHJlZj1cInFyQ29kZUNvbnRhaW5lclwiPjwvY2FudmFzPlxyXG4gICAgPGJ1dHRvbiBAY2xpY2s9XCJwcmludFFSQ29kZVwiPlByaW50IFFSIENvZGU8L2J1dHRvbj5cclxuIDwvZGl2PlxyXG48L3RlbXBsYXRlPlxyXG5cclxuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///./node_modules/babel-loader/lib/index.js??clonedRuleSet-40.use[0]!./node_modules/vue-loader/dist/templateLoader.js??ruleSet[1].rules[3]!./node_modules/vue-loader/dist/index.js??ruleSet[0].use[0]!./src/components/QRCodeComponent.vue?vue&type=template&id=6beabf8f\n");

/***/ })

},
/******/ function(__webpack_require__) { // webpackRuntimeModules
/******/ /* webpack/runtime/getFullHash */
/******/ !function() {
/******/ 	__webpack_require__.h = function() { return "ea871dfd4855333e"; }
/******/ }();
/******/ 
/******/ }
);
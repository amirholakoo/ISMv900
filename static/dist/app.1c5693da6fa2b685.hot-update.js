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

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var qrcode__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! qrcode */ \"./node_modules/qrcode/lib/browser.js\");\n\n/* harmony default export */ __webpack_exports__[\"default\"] = ({\n  name: \"QRCodeComponent\",\n  props: ['data'],\n  data() {\n    return {\n      qru: ''\n    };\n  },\n  mounted() {\n    this.generateQRCode();\n    console.log(this.data);\n  },\n  methods: {\n    async generateQRCode() {\n      try {\n        console.log(this.data);\n        await qrcode__WEBPACK_IMPORTED_MODULE_0__.toCanvas(this.$refs.qrCodeContainer, this.data, {\n          width: 256,\n          height: 256\n        });\n        this.qru = await qrcode__WEBPACK_IMPORTED_MODULE_0__.toDataURL(this.data, {\n          width: 256,\n          height: 256\n        });\n      } catch (error) {\n        console.error(error);\n      }\n    },\n    async printQRCode() {\n      let qr = await qrcode__WEBPACK_IMPORTED_MODULE_0__.toDataURL(this.qrCodeData);\n      console.log(qr);\n      const printWindow = window.open('', '_blank');\n      printWindow.document.write('<html><head><title>Print Canvas</title></head><body>');\n      printWindow.document.write('<img src=\"' + qr + '\" />');\n      printWindow.document.write('</body></html>');\n      printWindow.print();\n      printWindow.documents.close();\n    }\n  }\n});//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9ub2RlX21vZHVsZXMvYmFiZWwtbG9hZGVyL2xpYi9pbmRleC5qcz8/Y2xvbmVkUnVsZVNldC00MC51c2VbMF0hLi9ub2RlX21vZHVsZXMvdnVlLWxvYWRlci9kaXN0L2luZGV4LmpzPz9ydWxlU2V0WzBdLnVzZVswXSEuL3NyYy9jb21wb25lbnRzL1FSQ29kZUNvbXBvbmVudC52dWU/dnVlJnR5cGU9c2NyaXB0Jmxhbmc9anMiLCJtYXBwaW5ncyI6Ijs7QUFDQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vZnJvbnRlbmQvLi9zcmMvY29tcG9uZW50cy9RUkNvZGVDb21wb25lbnQudnVlPzU2MjEiXSwic291cmNlc0NvbnRlbnQiOlsiPHNjcmlwdD5cclxuaW1wb3J0IFFSQ29kZSBmcm9tICdxcmNvZGUnO1xyXG5cclxuZXhwb3J0IGRlZmF1bHQge1xyXG4gbmFtZTogXCJRUkNvZGVDb21wb25lbnRcIixcclxuIHByb3BzOiBbJ2RhdGEnXSxcclxuIGRhdGEoKSB7XHJcbiAgICByZXR1cm4ge1xyXG4gICAgICBxcnU6ICcnXHJcbiAgICB9O1xyXG4gfSxcclxuIG1vdW50ZWQoKSB7XHJcbiAgICB0aGlzLmdlbmVyYXRlUVJDb2RlKCk7XHJcbiAgICBjb25zb2xlLmxvZyh0aGlzLmRhdGEpXHJcbiB9LFxyXG4gbWV0aG9kczoge1xyXG4gICAgYXN5bmMgZ2VuZXJhdGVRUkNvZGUoKSB7XHJcbiAgICAgIHRyeSB7XHJcbiAgICAgICAgY29uc29sZS5sb2codGhpcy5kYXRhKVxyXG4gICAgICAgIGF3YWl0IFFSQ29kZS50b0NhbnZhcyh0aGlzLiRyZWZzLnFyQ29kZUNvbnRhaW5lciwgdGhpcy5kYXRhLCB7XHJcbiAgICAgICAgICB3aWR0aDogMjU2LFxyXG4gICAgICAgICAgaGVpZ2h0OiAyNTYsXHJcbiAgICAgICAgfSk7XHJcbiAgICAgICAgdGhpcy5xcnUgPSBhd2FpdCBRUkNvZGUudG9EYXRhVVJMKHRoaXMuZGF0YSwge1xyXG4gICAgICAgICAgd2lkdGg6IDI1NixcclxuICAgICAgICAgIGhlaWdodDogMjU2LFxyXG4gICAgICAgIH0pXHJcbiAgICAgIH0gY2F0Y2ggKGVycm9yKSB7XHJcbiAgICAgICAgY29uc29sZS5lcnJvcihlcnJvcik7XHJcbiAgICAgIH1cclxuICAgIH0sXHJcbiAgICBhc3luYyBwcmludFFSQ29kZSgpIHtcclxuICAgICAgbGV0IHFyID0gYXdhaXQgUVJDb2RlLnRvRGF0YVVSTCh0aGlzLnFyQ29kZURhdGEpXHJcbiAgICAgIGNvbnNvbGUubG9nKHFyKVxyXG5cclxuICAgICAgY29uc3QgcHJpbnRXaW5kb3cgPSB3aW5kb3cub3BlbignJywgJ19ibGFuaycpO1xyXG4gICAgICBwcmludFdpbmRvdy5kb2N1bWVudC53cml0ZSgnPGh0bWw+PGhlYWQ+PHRpdGxlPlByaW50IENhbnZhczwvdGl0bGU+PC9oZWFkPjxib2R5PicpO1xyXG4gICAgICBwcmludFdpbmRvdy5kb2N1bWVudC53cml0ZSgnPGltZyBzcmM9XCInICsgcXIgKyAnXCIgLz4nKTtcclxuICAgICAgcHJpbnRXaW5kb3cuZG9jdW1lbnQud3JpdGUoJzwvYm9keT48L2h0bWw+Jyk7XHJcbiAgICAgIHByaW50V2luZG93LnByaW50KCk7XHJcbiAgICAgIHByaW50V2luZG93LmRvY3VtZW50cy5jbG9zZSgpO1xyXG4gICAgfSxcclxuIH0sXHJcbn07XHJcbjwvc2NyaXB0PlxyXG5cclxuPHRlbXBsYXRlPlxyXG4gPGRpdj5cclxuICAgIDxpbWcgOnNyYz1cInFydVwiLz5cclxuICAgIDxjYW52YXMgcmVmPVwicXJDb2RlQ29udGFpbmVyXCI+PC9jYW52YXM+XHJcbiAgICA8YnV0dG9uIEBjbGljaz1cInByaW50UVJDb2RlXCI+UHJpbnQgUVIgQ29kZTwvYnV0dG9uPlxyXG4gPC9kaXY+XHJcbjwvdGVtcGxhdGU+XHJcblxyXG4iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///./node_modules/babel-loader/lib/index.js??clonedRuleSet-40.use[0]!./node_modules/vue-loader/dist/index.js??ruleSet[0].use[0]!./src/components/QRCodeComponent.vue?vue&type=script&lang=js\n");

/***/ }),

/***/ "./node_modules/babel-loader/lib/index.js??clonedRuleSet-40.use[0]!./node_modules/vue-loader/dist/templateLoader.js??ruleSet[1].rules[3]!./node_modules/vue-loader/dist/index.js??ruleSet[0].use[0]!./src/components/QRCodeComponent.vue?vue&type=template&id=6beabf8f":
/*!*****************************************************************************************************************************************************************************************************************************************************************************!*\
  !*** ./node_modules/babel-loader/lib/index.js??clonedRuleSet-40.use[0]!./node_modules/vue-loader/dist/templateLoader.js??ruleSet[1].rules[3]!./node_modules/vue-loader/dist/index.js??ruleSet[0].use[0]!./src/components/QRCodeComponent.vue?vue&type=template&id=6beabf8f ***!
  \*****************************************************************************************************************************************************************************************************************************************************************************/
/***/ (function(__unused_webpack_module, __webpack_exports__, __webpack_require__) {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   render: function() { return /* binding */ render; }\n/* harmony export */ });\n/* harmony import */ var vue__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! vue */ \"./node_modules/vue/dist/vue.runtime.esm-bundler.js\");\n\nconst _hoisted_1 = [\"src\"];\nconst _hoisted_2 = {\n  ref: \"qrCodeContainer\"\n};\nfunction render(_ctx, _cache, $props, $setup, $data, $options) {\n  return (0,vue__WEBPACK_IMPORTED_MODULE_0__.openBlock)(), (0,vue__WEBPACK_IMPORTED_MODULE_0__.createElementBlock)(\"div\", null, [(0,vue__WEBPACK_IMPORTED_MODULE_0__.createElementVNode)(\"img\", {\n    src: $data.qru\n  }, null, 8 /* PROPS */, _hoisted_1), (0,vue__WEBPACK_IMPORTED_MODULE_0__.createElementVNode)(\"canvas\", _hoisted_2, null, 512 /* NEED_PATCH */), (0,vue__WEBPACK_IMPORTED_MODULE_0__.createElementVNode)(\"button\", {\n    onClick: _cache[0] || (_cache[0] = (...args) => $options.printQRCode && $options.printQRCode(...args))\n  }, \"Print QR Code\")]);\n}//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9ub2RlX21vZHVsZXMvYmFiZWwtbG9hZGVyL2xpYi9pbmRleC5qcz8/Y2xvbmVkUnVsZVNldC00MC51c2VbMF0hLi9ub2RlX21vZHVsZXMvdnVlLWxvYWRlci9kaXN0L3RlbXBsYXRlTG9hZGVyLmpzPz9ydWxlU2V0WzFdLnJ1bGVzWzNdIS4vbm9kZV9tb2R1bGVzL3Z1ZS1sb2FkZXIvZGlzdC9pbmRleC5qcz8/cnVsZVNldFswXS51c2VbMF0hLi9zcmMvY29tcG9uZW50cy9RUkNvZGVDb21wb25lbnQudnVlP3Z1ZSZ0eXBlPXRlbXBsYXRlJmlkPTZiZWFiZjhmIiwibWFwcGluZ3MiOiI7Ozs7OztBQUFBOztBQWlEQTtBQUFBOztBQUZBO0FBQ0E7QUFBQTtBQUVBO0FBQUEiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9mcm9udGVuZC8uL3NyYy9jb21wb25lbnRzL1FSQ29kZUNvbXBvbmVudC52dWU/NTYyMSJdLCJzb3VyY2VzQ29udGVudCI6WyI8c2NyaXB0PlxyXG5pbXBvcnQgUVJDb2RlIGZyb20gJ3FyY29kZSc7XHJcblxyXG5leHBvcnQgZGVmYXVsdCB7XHJcbiBuYW1lOiBcIlFSQ29kZUNvbXBvbmVudFwiLFxyXG4gcHJvcHM6IFsnZGF0YSddLFxyXG4gZGF0YSgpIHtcclxuICAgIHJldHVybiB7XHJcbiAgICAgIHFydTogJydcclxuICAgIH07XHJcbiB9LFxyXG4gbW91bnRlZCgpIHtcclxuICAgIHRoaXMuZ2VuZXJhdGVRUkNvZGUoKTtcclxuICAgIGNvbnNvbGUubG9nKHRoaXMuZGF0YSlcclxuIH0sXHJcbiBtZXRob2RzOiB7XHJcbiAgICBhc3luYyBnZW5lcmF0ZVFSQ29kZSgpIHtcclxuICAgICAgdHJ5IHtcclxuICAgICAgICBjb25zb2xlLmxvZyh0aGlzLmRhdGEpXHJcbiAgICAgICAgYXdhaXQgUVJDb2RlLnRvQ2FudmFzKHRoaXMuJHJlZnMucXJDb2RlQ29udGFpbmVyLCB0aGlzLmRhdGEsIHtcclxuICAgICAgICAgIHdpZHRoOiAyNTYsXHJcbiAgICAgICAgICBoZWlnaHQ6IDI1NixcclxuICAgICAgICB9KTtcclxuICAgICAgICB0aGlzLnFydSA9IGF3YWl0IFFSQ29kZS50b0RhdGFVUkwodGhpcy5kYXRhLCB7XHJcbiAgICAgICAgICB3aWR0aDogMjU2LFxyXG4gICAgICAgICAgaGVpZ2h0OiAyNTYsXHJcbiAgICAgICAgfSlcclxuICAgICAgfSBjYXRjaCAoZXJyb3IpIHtcclxuICAgICAgICBjb25zb2xlLmVycm9yKGVycm9yKTtcclxuICAgICAgfVxyXG4gICAgfSxcclxuICAgIGFzeW5jIHByaW50UVJDb2RlKCkge1xyXG4gICAgICBsZXQgcXIgPSBhd2FpdCBRUkNvZGUudG9EYXRhVVJMKHRoaXMucXJDb2RlRGF0YSlcclxuICAgICAgY29uc29sZS5sb2cocXIpXHJcblxyXG4gICAgICBjb25zdCBwcmludFdpbmRvdyA9IHdpbmRvdy5vcGVuKCcnLCAnX2JsYW5rJyk7XHJcbiAgICAgIHByaW50V2luZG93LmRvY3VtZW50LndyaXRlKCc8aHRtbD48aGVhZD48dGl0bGU+UHJpbnQgQ2FudmFzPC90aXRsZT48L2hlYWQ+PGJvZHk+Jyk7XHJcbiAgICAgIHByaW50V2luZG93LmRvY3VtZW50LndyaXRlKCc8aW1nIHNyYz1cIicgKyBxciArICdcIiAvPicpO1xyXG4gICAgICBwcmludFdpbmRvdy5kb2N1bWVudC53cml0ZSgnPC9ib2R5PjwvaHRtbD4nKTtcclxuICAgICAgcHJpbnRXaW5kb3cucHJpbnQoKTtcclxuICAgICAgcHJpbnRXaW5kb3cuZG9jdW1lbnRzLmNsb3NlKCk7XHJcbiAgICB9LFxyXG4gfSxcclxufTtcclxuPC9zY3JpcHQ+XHJcblxyXG48dGVtcGxhdGU+XHJcbiA8ZGl2PlxyXG4gICAgPGltZyA6c3JjPVwicXJ1XCIvPlxyXG4gICAgPGNhbnZhcyByZWY9XCJxckNvZGVDb250YWluZXJcIj48L2NhbnZhcz5cclxuICAgIDxidXR0b24gQGNsaWNrPVwicHJpbnRRUkNvZGVcIj5QcmludCBRUiBDb2RlPC9idXR0b24+XHJcbiA8L2Rpdj5cclxuPC90ZW1wbGF0ZT5cclxuXHJcbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///./node_modules/babel-loader/lib/index.js??clonedRuleSet-40.use[0]!./node_modules/vue-loader/dist/templateLoader.js??ruleSet[1].rules[3]!./node_modules/vue-loader/dist/index.js??ruleSet[0].use[0]!./src/components/QRCodeComponent.vue?vue&type=template&id=6beabf8f\n");

/***/ })

},
/******/ function(__webpack_require__) { // webpackRuntimeModules
/******/ /* webpack/runtime/getFullHash */
/******/ !function() {
/******/ 	__webpack_require__.h = function() { return "fdceb6c3f700c2d3"; }
/******/ }();
/******/ 
/******/ }
);
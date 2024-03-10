/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(typeof self !== 'undefined' ? self : this)["webpackHotUpdatefrontend"]("app",{

/***/ "./src/router/index.js":
/*!*****************************!*\
  !*** ./src/router/index.js ***!
  \*****************************/
/***/ (function(__unused_webpack_module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var vue_router__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! vue-router */ \"./node_modules/vue-router/dist/vue-router.mjs\");\n/* harmony import */ var _views_HomeView_vue__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../views/HomeView.vue */ \"./src/views/HomeView.vue\");\n/* harmony import */ var _components_addTruck_vue__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @/components/addTruck.vue */ \"./src/components/addTruck.vue\");\n/* harmony import */ var _components_addSupplier_vue__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @/components/addSupplier.vue */ \"./src/components/addSupplier.vue\");\n/* harmony import */ var _components_addCustomer_vue__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @/components/addCustomer.vue */ \"./src/components/addCustomer.vue\");\n/* harmony import */ var _components_addRawMaterial_vue__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @/components/addRawMaterial.vue */ \"./src/components/addRawMaterial.vue\");\n/* harmony import */ var _components_addNewReel_vue__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @/components/addNewReel.vue */ \"./src/components/addNewReel.vue\");\n\n\n\n\n\n\n\nconst routes = [{\n  path: '/',\n  name: 'home',\n  component: _views_HomeView_vue__WEBPACK_IMPORTED_MODULE_0__[\"default\"]\n}, {\n  path: '/about',\n  name: 'about',\n  // route level code-splitting\n  // this generates a separate chunk (about.[hash].js) for this route\n  // which is lazy-loaded when the route is visited.\n  component: () => __webpack_require__.e(/*! import() | about */ \"about\").then(__webpack_require__.bind(__webpack_require__, /*! ../views/AboutView.vue */ \"./src/views/AboutView.vue\"))\n}, {\n  path: '/myapp/addTruck/',\n  name: 'addTruck',\n  component: _components_addTruck_vue__WEBPACK_IMPORTED_MODULE_1__[\"default\"]\n}, {\n  path: '/myapp/addSupplier/',\n  name: 'addSupplier',\n  component: _components_addSupplier_vue__WEBPACK_IMPORTED_MODULE_2__[\"default\"]\n}, {\n  path: '/myapp/addCustomer/',\n  name: 'addCustomer',\n  component: _components_addCustomer_vue__WEBPACK_IMPORTED_MODULE_3__[\"default\"]\n}, {\n  path: '/myapp/addRawMaterial/',\n  name: 'addRawMaterial',\n  component: _components_addRawMaterial_vue__WEBPACK_IMPORTED_MODULE_4__[\"default\"]\n}, {\n  path: '/myapp/addNewReel/',\n  name: 'addNewReel',\n  component: _components_addNewReel_vue__WEBPACK_IMPORTED_MODULE_5__[\"default\"]\n}];\nconst router = (0,vue_router__WEBPACK_IMPORTED_MODULE_6__.createRouter)({\n  // history: createWebHistory(process.env.BASE_URL),\n  history: (0,vue_router__WEBPACK_IMPORTED_MODULE_6__.createWebHistory)(),\n  routes\n});\n/* harmony default export */ __webpack_exports__[\"default\"] = (router);//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvcm91dGVyL2luZGV4LmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7O0FBQUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBR0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUVBIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vZnJvbnRlbmQvLi9zcmMvcm91dGVyL2luZGV4LmpzPzVhYTQiXSwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IHsgY3JlYXRlUm91dGVyLCBjcmVhdGVXZWJIaXN0b3J5IH0gZnJvbSAndnVlLXJvdXRlcidcclxuaW1wb3J0IEhvbWVWaWV3IGZyb20gJy4uL3ZpZXdzL0hvbWVWaWV3LnZ1ZSdcclxuaW1wb3J0IGFkZFRydWNrIGZyb20gXCJAL2NvbXBvbmVudHMvYWRkVHJ1Y2sudnVlXCI7XHJcbmltcG9ydCBhZGRTdXBwbGllciBmcm9tIFwiQC9jb21wb25lbnRzL2FkZFN1cHBsaWVyLnZ1ZVwiO1xyXG5pbXBvcnQgYWRkQ3VzdG9tZXIgZnJvbSBcIkAvY29tcG9uZW50cy9hZGRDdXN0b21lci52dWVcIjtcclxuaW1wb3J0IGFkZFJhd01hdGVyaWFsIGZyb20gXCJAL2NvbXBvbmVudHMvYWRkUmF3TWF0ZXJpYWwudnVlXCI7XHJcbmltcG9ydCBhZGROZXdSZWVsIGZyb20gXCJAL2NvbXBvbmVudHMvYWRkTmV3UmVlbC52dWVcIjtcclxuXHJcbmNvbnN0IHJvdXRlcyA9IFtcclxuICB7XHJcbiAgICBwYXRoOiAnLycsXHJcbiAgICBuYW1lOiAnaG9tZScsXHJcbiAgICBjb21wb25lbnQ6IEhvbWVWaWV3XHJcbiAgfSxcclxuICB7XHJcbiAgICBwYXRoOiAnL2Fib3V0JyxcclxuICAgIG5hbWU6ICdhYm91dCcsXHJcbiAgICAvLyByb3V0ZSBsZXZlbCBjb2RlLXNwbGl0dGluZ1xyXG4gICAgLy8gdGhpcyBnZW5lcmF0ZXMgYSBzZXBhcmF0ZSBjaHVuayAoYWJvdXQuW2hhc2hdLmpzKSBmb3IgdGhpcyByb3V0ZVxyXG4gICAgLy8gd2hpY2ggaXMgbGF6eS1sb2FkZWQgd2hlbiB0aGUgcm91dGUgaXMgdmlzaXRlZC5cclxuICAgIGNvbXBvbmVudDogKCkgPT4gaW1wb3J0KC8qIHdlYnBhY2tDaHVua05hbWU6IFwiYWJvdXRcIiAqLyAnLi4vdmlld3MvQWJvdXRWaWV3LnZ1ZScpXHJcbiAgfSxcclxuICB7XHJcbiAgICBwYXRoOiAnL215YXBwL2FkZFRydWNrLycsXHJcbiAgICBuYW1lOiAnYWRkVHJ1Y2snLFxyXG4gICAgY29tcG9uZW50OiBhZGRUcnVja1xyXG4gIH0sXHJcbiAge1xyXG4gICAgcGF0aDogJy9teWFwcC9hZGRTdXBwbGllci8nLFxyXG4gICAgbmFtZTogJ2FkZFN1cHBsaWVyJyxcclxuICAgIGNvbXBvbmVudDogYWRkU3VwcGxpZXJcclxuICB9LFxyXG4gIHtcclxuICAgIHBhdGg6ICcvbXlhcHAvYWRkQ3VzdG9tZXIvJyxcclxuICAgIG5hbWU6ICdhZGRDdXN0b21lcicsXHJcbiAgICBjb21wb25lbnQ6IGFkZEN1c3RvbWVyXHJcbiAgfSxcclxuICB7XHJcbiAgICBwYXRoOiAnL215YXBwL2FkZFJhd01hdGVyaWFsLycsXHJcbiAgICBuYW1lOiAnYWRkUmF3TWF0ZXJpYWwnLFxyXG4gICAgY29tcG9uZW50OiBhZGRSYXdNYXRlcmlhbFxyXG4gIH0sXHJcbiAge1xyXG4gICAgcGF0aDogJy9teWFwcC9hZGROZXdSZWVsLycsXHJcbiAgICBuYW1lOiAnYWRkTmV3UmVlbCcsXHJcbiAgICBjb21wb25lbnQ6IGFkZE5ld1JlZWxcclxuICB9LFxyXG5dXHJcblxyXG5jb25zdCByb3V0ZXIgPSBjcmVhdGVSb3V0ZXIoe1xyXG4gIC8vIGhpc3Rvcnk6IGNyZWF0ZVdlYkhpc3RvcnkocHJvY2Vzcy5lbnYuQkFTRV9VUkwpLFxyXG4gIGhpc3Rvcnk6IGNyZWF0ZVdlYkhpc3RvcnkoKSxcclxuICByb3V0ZXMsXHJcbn0pXHJcblxyXG5leHBvcnQgZGVmYXVsdCByb3V0ZXJcclxuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///./src/router/index.js\n");

/***/ }),

/***/ "./node_modules/babel-loader/lib/index.js??clonedRuleSet-40.use[0]!./tailwind.config.js?vue&type=script&lang=js&external":
/*!*******************************************************************************************************************************!*\
  !*** ./node_modules/babel-loader/lib/index.js??clonedRuleSet-40.use[0]!./tailwind.config.js?vue&type=script&lang=js&external ***!
  \*******************************************************************************************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("/** @type {import('tailwindcss').Config} */\nmodule.exports = {\n  content: ['./public/**/*.html', './src/**/*.{vue,js,ts,jsx,tsx}', \"./node_modules/flowbite/**/*.js\"],\n  theme: {\n    extend: {}\n  },\n  plugins: [__webpack_require__(/*! flowbite/plugin */ \"./node_modules/flowbite/plugin.js\")]\n};//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9ub2RlX21vZHVsZXMvYmFiZWwtbG9hZGVyL2xpYi9pbmRleC5qcz8/Y2xvbmVkUnVsZVNldC00MC51c2VbMF0hLi90YWlsd2luZC5jb25maWcuanM/dnVlJnR5cGU9c2NyaXB0Jmxhbmc9anMmZXh0ZXJuYWwiLCJtYXBwaW5ncyI6IkFBQUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFHQSIsInNvdXJjZXMiOlsid2VicGFjazovL2Zyb250ZW5kLy4vdGFpbHdpbmQuY29uZmlnLmpzP2JkMzciXSwic291cmNlc0NvbnRlbnQiOlsiLyoqIEB0eXBlIHtpbXBvcnQoJ3RhaWx3aW5kY3NzJykuQ29uZmlnfSAqL1xubW9kdWxlLmV4cG9ydHMgPSB7XG4gIGNvbnRlbnQ6IFsnLi9wdWJsaWMvKiovKi5odG1sJywgJy4vc3JjLyoqLyoue3Z1ZSxqcyx0cyxqc3gsdHN4fScsIFwiLi9ub2RlX21vZHVsZXMvZmxvd2JpdGUvKiovKi5qc1wiXSxcbiAgdGhlbWU6IHtcbiAgICBleHRlbmQ6IHt9LFxuICB9LFxuICBwbHVnaW5zOiBbXG4gICAgICByZXF1aXJlKCdmbG93Yml0ZS9wbHVnaW4nKVxuICBdLFxufVxuXG4iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///./node_modules/babel-loader/lib/index.js??clonedRuleSet-40.use[0]!./tailwind.config.js?vue&type=script&lang=js&external\n");

/***/ }),

/***/ "./src/components/addTruck.vue":
/*!*************************************!*\
  !*** ./src/components/addTruck.vue ***!
  \*************************************/
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _tailwind_config_js_vue_type_script_lang_js_external__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../../tailwind.config.js?vue&type=script&lang=js&external */ \"./tailwind.config.js?vue&type=script&lang=js&external\");\n/* harmony reexport (unknown) */ var __WEBPACK_REEXPORT_OBJECT__ = {};\n/* harmony reexport (unknown) */ for(var __WEBPACK_IMPORT_KEY__ in _tailwind_config_js_vue_type_script_lang_js_external__WEBPACK_IMPORTED_MODULE_0__) if(__WEBPACK_IMPORT_KEY__ !== \"default\") __WEBPACK_REEXPORT_OBJECT__[__WEBPACK_IMPORT_KEY__] = function(key) { return _tailwind_config_js_vue_type_script_lang_js_external__WEBPACK_IMPORTED_MODULE_0__[key]; }.bind(0, __WEBPACK_IMPORT_KEY__)\n/* harmony reexport (unknown) */ __webpack_require__.d(__webpack_exports__, __WEBPACK_REEXPORT_OBJECT__);\n/* harmony import */ var _node_modules_vue_loader_dist_exportHelper_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../node_modules/vue-loader/dist/exportHelper.js */ \"./node_modules/vue-loader/dist/exportHelper.js\");\n\n\n\n;\nconst __exports__ = /*#__PURE__*/(0,_node_modules_vue_loader_dist_exportHelper_js__WEBPACK_IMPORTED_MODULE_1__[\"default\"])(_tailwind_config_js_vue_type_script_lang_js_external__WEBPACK_IMPORTED_MODULE_0__[\"default\"], [['__file',\"src/components/addTruck.vue\"]])\n/* hot reload */\nif (true) {\n  __exports__.__hmrId = \"63498d4e\"\n  const api = __VUE_HMR_RUNTIME__\n  module.hot.accept()\n  if (!api.createRecord('63498d4e', __exports__)) {\n    api.reload('63498d4e', __exports__)\n  }\n  \n}\n\n\n/* harmony default export */ __webpack_exports__[\"default\"] = (__exports__);//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvY29tcG9uZW50cy9hZGRUcnVjay52dWUiLCJtYXBwaW5ncyI6Ijs7Ozs7O0FBQUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vZnJvbnRlbmQvLi9zcmMvY29tcG9uZW50cy9hZGRUcnVjay52dWU/MzUzNCJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgc2NyaXB0IGZyb20gXCIuLi8uLi90YWlsd2luZC5jb25maWcuanM/dnVlJnR5cGU9c2NyaXB0Jmxhbmc9anMmZXh0ZXJuYWxcIlxuZXhwb3J0ICogZnJvbSBcIi4uLy4uL3RhaWx3aW5kLmNvbmZpZy5qcz92dWUmdHlwZT1zY3JpcHQmbGFuZz1qcyZleHRlcm5hbFwiXG5cbmltcG9ydCBleHBvcnRDb21wb25lbnQgZnJvbSBcIi4uLy4uL25vZGVfbW9kdWxlcy92dWUtbG9hZGVyL2Rpc3QvZXhwb3J0SGVscGVyLmpzXCJcbmNvbnN0IF9fZXhwb3J0c19fID0gLyojX19QVVJFX18qL2V4cG9ydENvbXBvbmVudChzY3JpcHQsIFtbJ19fZmlsZScsXCJzcmMvY29tcG9uZW50cy9hZGRUcnVjay52dWVcIl1dKVxuLyogaG90IHJlbG9hZCAqL1xuaWYgKG1vZHVsZS5ob3QpIHtcbiAgX19leHBvcnRzX18uX19obXJJZCA9IFwiNjM0OThkNGVcIlxuICBjb25zdCBhcGkgPSBfX1ZVRV9ITVJfUlVOVElNRV9fXG4gIG1vZHVsZS5ob3QuYWNjZXB0KClcbiAgaWYgKCFhcGkuY3JlYXRlUmVjb3JkKCc2MzQ5OGQ0ZScsIF9fZXhwb3J0c19fKSkge1xuICAgIGFwaS5yZWxvYWQoJzYzNDk4ZDRlJywgX19leHBvcnRzX18pXG4gIH1cbiAgXG59XG5cblxuZXhwb3J0IGRlZmF1bHQgX19leHBvcnRzX18iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///./src/components/addTruck.vue\n");

/***/ }),

/***/ "./tailwind.config.js?vue&type=script&lang=js&external":
/*!*************************************************************!*\
  !*** ./tailwind.config.js?vue&type=script&lang=js&external ***!
  \*************************************************************/
/***/ (function(__unused_webpack_module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": function() { return /* reexport default from dynamic */ _node_modules_babel_loader_lib_index_js_clonedRuleSet_40_use_0_tailwind_config_js_vue_type_script_lang_js_external__WEBPACK_IMPORTED_MODULE_0___default.a; }\n/* harmony export */ });\n/* harmony import */ var _node_modules_babel_loader_lib_index_js_clonedRuleSet_40_use_0_tailwind_config_js_vue_type_script_lang_js_external__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! -!./node_modules/babel-loader/lib/index.js??clonedRuleSet-40.use[0]!./tailwind.config.js?vue&type=script&lang=js&external */ \"./node_modules/babel-loader/lib/index.js??clonedRuleSet-40.use[0]!./tailwind.config.js?vue&type=script&lang=js&external\");\n/* harmony import */ var _node_modules_babel_loader_lib_index_js_clonedRuleSet_40_use_0_tailwind_config_js_vue_type_script_lang_js_external__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_babel_loader_lib_index_js_clonedRuleSet_40_use_0_tailwind_config_js_vue_type_script_lang_js_external__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony reexport (unknown) */ var __WEBPACK_REEXPORT_OBJECT__ = {};\n/* harmony reexport (unknown) */ for(var __WEBPACK_IMPORT_KEY__ in _node_modules_babel_loader_lib_index_js_clonedRuleSet_40_use_0_tailwind_config_js_vue_type_script_lang_js_external__WEBPACK_IMPORTED_MODULE_0__) if(__WEBPACK_IMPORT_KEY__ !== \"default\") __WEBPACK_REEXPORT_OBJECT__[__WEBPACK_IMPORT_KEY__] = function(key) { return _node_modules_babel_loader_lib_index_js_clonedRuleSet_40_use_0_tailwind_config_js_vue_type_script_lang_js_external__WEBPACK_IMPORTED_MODULE_0__[key]; }.bind(0, __WEBPACK_IMPORT_KEY__)\n/* harmony reexport (unknown) */ __webpack_require__.d(__webpack_exports__, __WEBPACK_REEXPORT_OBJECT__);\n //# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi90YWlsd2luZC5jb25maWcuanM/dnVlJnR5cGU9c2NyaXB0Jmxhbmc9anMmZXh0ZXJuYWwiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7O0FBQUEiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9mcm9udGVuZC8uL3RhaWx3aW5kLmNvbmZpZy5qcz9jMzExIl0sInNvdXJjZXNDb250ZW50IjpbImV4cG9ydCB7IGRlZmF1bHQgfSBmcm9tIFwiLSEuL25vZGVfbW9kdWxlcy9iYWJlbC1sb2FkZXIvbGliL2luZGV4LmpzPz9jbG9uZWRSdWxlU2V0LTQwLnVzZVswXSEuL3RhaWx3aW5kLmNvbmZpZy5qcz92dWUmdHlwZT1zY3JpcHQmbGFuZz1qcyZleHRlcm5hbFwiOyBleHBvcnQgKiBmcm9tIFwiLSEuL25vZGVfbW9kdWxlcy9iYWJlbC1sb2FkZXIvbGliL2luZGV4LmpzPz9jbG9uZWRSdWxlU2V0LTQwLnVzZVswXSEuL3RhaWx3aW5kLmNvbmZpZy5qcz92dWUmdHlwZT1zY3JpcHQmbGFuZz1qcyZleHRlcm5hbFwiIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///./tailwind.config.js?vue&type=script&lang=js&external\n");

/***/ })

},
/******/ function(__webpack_require__) { // webpackRuntimeModules
/******/ /* webpack/runtime/getFullHash */
/******/ !function() {
/******/ 	__webpack_require__.h = function() { return "35cd0ca02c84a582"; }
/******/ }();
/******/ 
/******/ }
);
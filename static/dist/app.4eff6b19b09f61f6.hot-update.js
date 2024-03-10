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

/***/ "./src/router/index.js":
/*!*****************************!*\
  !*** ./src/router/index.js ***!
  \*****************************/
/***/ (function(__unused_webpack_module, __webpack_exports__, __webpack_require__) {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var vue_router__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! vue-router */ \"./node_modules/vue-router/dist/vue-router.mjs\");\n/* harmony import */ var _views_HomeView_vue__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../views/HomeView.vue */ \"./src/views/HomeView.vue\");\n/* harmony import */ var _components_addTruck_vue__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @/components/addTruck.vue */ \"./src/components/addTruck.vue\");\n/* harmony import */ var _components_addSupplier_vue__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @/components/addSupplier.vue */ \"./src/components/addSupplier.vue\");\n\n\n\n\nconst routes = [{\n  path: '/',\n  name: 'home',\n  component: _views_HomeView_vue__WEBPACK_IMPORTED_MODULE_0__[\"default\"]\n}, {\n  path: '/about',\n  name: 'about',\n  // route level code-splitting\n  // this generates a separate chunk (about.[hash].js) for this route\n  // which is lazy-loaded when the route is visited.\n  component: () => __webpack_require__.e(/*! import() | about */ \"about\").then(__webpack_require__.bind(__webpack_require__, /*! ../views/AboutView.vue */ \"./src/views/AboutView.vue\"))\n}, {\n  path: '/myapp/addTruck/',\n  name: 'addTruck',\n  component: _components_addTruck_vue__WEBPACK_IMPORTED_MODULE_1__[\"default\"]\n}, {\n  path: '/myapp/addSupplier/',\n  name: 'addSupplier',\n  component: _components_addSupplier_vue__WEBPACK_IMPORTED_MODULE_2__[\"default\"]\n}, {\n  path: '/myapp/addCustomer/',\n  name: 'addCustomer',\n  component: addCustomer\n}];\nconst router = (0,vue_router__WEBPACK_IMPORTED_MODULE_3__.createRouter)({\n  // history: createWebHistory(process.env.BASE_URL),\n  history: (0,vue_router__WEBPACK_IMPORTED_MODULE_3__.createWebHistory)(),\n  routes\n});\n/* harmony default export */ __webpack_exports__[\"default\"] = (router);//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvcm91dGVyL2luZGV4LmpzIiwibWFwcGluZ3MiOiI7Ozs7O0FBQUE7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFHQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBRUEiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9mcm9udGVuZC8uL3NyYy9yb3V0ZXIvaW5kZXguanM/NWFhNCJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgeyBjcmVhdGVSb3V0ZXIsIGNyZWF0ZVdlYkhpc3RvcnkgfSBmcm9tICd2dWUtcm91dGVyJ1xyXG5pbXBvcnQgSG9tZVZpZXcgZnJvbSAnLi4vdmlld3MvSG9tZVZpZXcudnVlJ1xyXG5pbXBvcnQgYWRkVHJ1Y2sgZnJvbSBcIkAvY29tcG9uZW50cy9hZGRUcnVjay52dWVcIjtcclxuaW1wb3J0IGFkZFN1cHBsaWVyIGZyb20gXCJAL2NvbXBvbmVudHMvYWRkU3VwcGxpZXIudnVlXCI7XHJcblxyXG5jb25zdCByb3V0ZXMgPSBbXHJcbiAge1xyXG4gICAgcGF0aDogJy8nLFxyXG4gICAgbmFtZTogJ2hvbWUnLFxyXG4gICAgY29tcG9uZW50OiBIb21lVmlld1xyXG4gIH0sXHJcbiAge1xyXG4gICAgcGF0aDogJy9hYm91dCcsXHJcbiAgICBuYW1lOiAnYWJvdXQnLFxyXG4gICAgLy8gcm91dGUgbGV2ZWwgY29kZS1zcGxpdHRpbmdcclxuICAgIC8vIHRoaXMgZ2VuZXJhdGVzIGEgc2VwYXJhdGUgY2h1bmsgKGFib3V0LltoYXNoXS5qcykgZm9yIHRoaXMgcm91dGVcclxuICAgIC8vIHdoaWNoIGlzIGxhenktbG9hZGVkIHdoZW4gdGhlIHJvdXRlIGlzIHZpc2l0ZWQuXHJcbiAgICBjb21wb25lbnQ6ICgpID0+IGltcG9ydCgvKiB3ZWJwYWNrQ2h1bmtOYW1lOiBcImFib3V0XCIgKi8gJy4uL3ZpZXdzL0Fib3V0Vmlldy52dWUnKVxyXG4gIH0sXHJcbiAge1xyXG4gICAgcGF0aDogJy9teWFwcC9hZGRUcnVjay8nLFxyXG4gICAgbmFtZTogJ2FkZFRydWNrJyxcclxuICAgIGNvbXBvbmVudDogYWRkVHJ1Y2tcclxuICB9LFxyXG4gIHtcclxuICAgIHBhdGg6ICcvbXlhcHAvYWRkU3VwcGxpZXIvJyxcclxuICAgIG5hbWU6ICdhZGRTdXBwbGllcicsXHJcbiAgICBjb21wb25lbnQ6IGFkZFN1cHBsaWVyXHJcbiAgfSxcclxuICB7XHJcbiAgICBwYXRoOiAnL215YXBwL2FkZEN1c3RvbWVyLycsXHJcbiAgICBuYW1lOiAnYWRkQ3VzdG9tZXInLFxyXG4gICAgY29tcG9uZW50OiBhZGRDdXN0b21lclxyXG4gIH0sXHJcbl1cclxuXHJcbmNvbnN0IHJvdXRlciA9IGNyZWF0ZVJvdXRlcih7XHJcbiAgLy8gaGlzdG9yeTogY3JlYXRlV2ViSGlzdG9yeShwcm9jZXNzLmVudi5CQVNFX1VSTCksXHJcbiAgaGlzdG9yeTogY3JlYXRlV2ViSGlzdG9yeSgpLFxyXG4gIHJvdXRlcyxcclxufSlcclxuXHJcbmV4cG9ydCBkZWZhdWx0IHJvdXRlclxyXG4iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///./src/router/index.js\n");

/***/ })

},
/******/ function(__webpack_require__) { // webpackRuntimeModules
/******/ /* webpack/runtime/getFullHash */
/******/ !function() {
/******/ 	__webpack_require__.h = function() { return "7633d4f33db6ce09"; }
/******/ }();
/******/ 
/******/ }
);
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
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var vue_router__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! vue-router */ \"./node_modules/vue-router/dist/vue-router.mjs\");\n/* harmony import */ var _views_HomeView_vue__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../views/HomeView.vue */ \"./src/views/HomeView.vue\");\n/* harmony import */ var _components_addTruck_vue__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @/components/addTruck.vue */ \"./src/components/addTruck.vue\");\n/* harmony import */ var _components_addTruck_vue__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_components_addTruck_vue__WEBPACK_IMPORTED_MODULE_1__);\n\n\n\nconst routes = [{\n  path: '/',\n  name: 'home',\n  component: _views_HomeView_vue__WEBPACK_IMPORTED_MODULE_0__[\"default\"]\n}, {\n  path: '/about',\n  name: 'about',\n  // route level code-splitting\n  // this generates a separate chunk (about.[hash].js) for this route\n  // which is lazy-loaded when the route is visited.\n  component: () => __webpack_require__.e(/*! import() | about */ \"about\").then(__webpack_require__.bind(__webpack_require__, /*! ../views/AboutView.vue */ \"./src/views/AboutView.vue\"))\n}, {\n  path: '/myapp/addTruck/',\n  name: 'addTruck',\n  component: (_components_addTruck_vue__WEBPACK_IMPORTED_MODULE_1___default())\n}];\nconst router = (0,vue_router__WEBPACK_IMPORTED_MODULE_2__.createRouter)({\n  // history: createWebHistory(process.env.BASE_URL),\n  history: (0,vue_router__WEBPACK_IMPORTED_MODULE_2__.createWebHistory)(),\n  routes\n});\n/* harmony default export */ __webpack_exports__[\"default\"] = (router);//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvcm91dGVyL2luZGV4LmpzIiwibWFwcGluZ3MiOiI7Ozs7O0FBQUE7QUFDQTtBQUNBO0FBRUE7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFHQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBRUEiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9mcm9udGVuZC8uL3NyYy9yb3V0ZXIvaW5kZXguanM/NWFhNCJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgeyBjcmVhdGVSb3V0ZXIsIGNyZWF0ZVdlYkhpc3RvcnkgfSBmcm9tICd2dWUtcm91dGVyJ1xyXG5pbXBvcnQgSG9tZVZpZXcgZnJvbSAnLi4vdmlld3MvSG9tZVZpZXcudnVlJ1xyXG5pbXBvcnQgYWRkVHJ1Y2sgZnJvbSBcIkAvY29tcG9uZW50cy9hZGRUcnVjay52dWVcIjtcclxuXHJcbmNvbnN0IHJvdXRlcyA9IFtcclxuICB7XHJcbiAgICBwYXRoOiAnLycsXHJcbiAgICBuYW1lOiAnaG9tZScsXHJcbiAgICBjb21wb25lbnQ6IEhvbWVWaWV3XHJcbiAgfSxcclxuICB7XHJcbiAgICBwYXRoOiAnL2Fib3V0JyxcclxuICAgIG5hbWU6ICdhYm91dCcsXHJcbiAgICAvLyByb3V0ZSBsZXZlbCBjb2RlLXNwbGl0dGluZ1xyXG4gICAgLy8gdGhpcyBnZW5lcmF0ZXMgYSBzZXBhcmF0ZSBjaHVuayAoYWJvdXQuW2hhc2hdLmpzKSBmb3IgdGhpcyByb3V0ZVxyXG4gICAgLy8gd2hpY2ggaXMgbGF6eS1sb2FkZWQgd2hlbiB0aGUgcm91dGUgaXMgdmlzaXRlZC5cclxuICAgIGNvbXBvbmVudDogKCkgPT4gaW1wb3J0KC8qIHdlYnBhY2tDaHVua05hbWU6IFwiYWJvdXRcIiAqLyAnLi4vdmlld3MvQWJvdXRWaWV3LnZ1ZScpXHJcbiAgfSxcclxuICB7XHJcbiAgICBwYXRoOiAnL215YXBwL2FkZFRydWNrLycsXHJcbiAgICBuYW1lOiAnYWRkVHJ1Y2snLFxyXG4gICAgY29tcG9uZW50OiBhZGRUcnVja1xyXG4gIH0sXHJcbl1cclxuXHJcbmNvbnN0IHJvdXRlciA9IGNyZWF0ZVJvdXRlcih7XHJcbiAgLy8gaGlzdG9yeTogY3JlYXRlV2ViSGlzdG9yeShwcm9jZXNzLmVudi5CQVNFX1VSTCksXHJcbiAgaGlzdG9yeTogY3JlYXRlV2ViSGlzdG9yeSgpLFxyXG4gIHJvdXRlcyxcclxufSlcclxuXHJcbmV4cG9ydCBkZWZhdWx0IHJvdXRlclxyXG4iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///./src/router/index.js\n");

/***/ }),

/***/ "./src/components/addTruck.vue":
/*!*************************************!*\
  !*** ./src/components/addTruck.vue ***!
  \*************************************/
/***/ (function() {



/***/ })

},
/******/ function(__webpack_require__) { // webpackRuntimeModules
/******/ /* webpack/runtime/getFullHash */
/******/ !function() {
/******/ 	__webpack_require__.h = function() { return "89abdd044bfc8f23"; }
/******/ }();
/******/ 
/******/ }
);
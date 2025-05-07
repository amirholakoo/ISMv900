const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  transpileDependencies: true,

  publicPath: process.env.NODE_ENV === 'production' ? '/static/' : 'http://localhost:8080',
  outputDir: '../static/',
  indexPath: '../templates/_base_vue.html',

  devServer: {
    port: 8080,
    headers: {
      'Access-Control-Allow-Origin': '*'
    },
    devMiddleware: {
      writeToDisk: true
    },
    client: {
      overlay: false
    }
  }
});

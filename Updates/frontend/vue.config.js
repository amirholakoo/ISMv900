const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  publicPath: process.env.NODE_ENV === 'production' ? '/static/' : 'http://localhost:8080',
  outputDir: '../static/',
  indexPath: '../templates/_base_vue.html',

  configureWebpack: {
    devServer: {
      devMiddleware: {
        writeToDisk: true // Only necessary if you need Django to serve these files in development
      }
    }
  }
})
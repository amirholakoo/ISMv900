/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./public/**/*.html', './src/**/*.{vue,js,ts,jsx,tsx}', "./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        mono: ['Fira Code', 'monospace'],
      },
      colors: {
        'main-bg': '#C3AF91',
         green: {
          '500': '#4CAF50',
          '600': '#3C9F40', // Example darker shade
          '300': '#66C160', // Example lighter shade
         },
      },
    },
  },
  plugins: [
      require('flowbite/plugin')
  ],
}


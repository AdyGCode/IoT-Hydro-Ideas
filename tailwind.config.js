/** @type {import('tailwindcss').Config} */

const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
    content: [
        "./app/templates/**/*.{html,js}",
        "./app/static/**/*.{html,js}",
        'node_modules/preline/dist/*.js',
    ],
    theme: {
        extend: {
            fontFamily: {
                sans: ['Inter var', ...defaultTheme.fontFamily.sans],
            },
        },
    },
    plugins: [
        require('preline/plugin'),
    ]
}


import globals from "globals";

export default [
    {
        files: ["**/*.js"],

        languageOptions: {
            ecmaVersion: 6,
            sourceType: "script",
            globals: {
                ...globals.browser,
                ...globals.amd,
                ...globals.jquery,
            },
        },

        rules: {
            indent: ["error", 4],

            "linebreak-style": ["error", "unix"],

            "no-unused-vars": [
                "error",
                { vars: "all", args: "none" },
            ],

            quotes: ["error", "single"],

            semi: ["error", "always"],

            "max-len": [
                "error",
                {
                    code: 80,
                    tabWidth: 4,
                    ignoreUrls: true,
                },
            ],

            "space-before-function-paren": ["error", "never"],
            "space-in-parens": ["error", "never"],
            "no-trailing-spaces": ["error"],
            "key-spacing": ["error", { beforeColon: false }],
            "func-call-spacing": ["error", "never"],
        },
    },
];

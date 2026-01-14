import globals from "globals";
import security from "eslint-plugin-security";

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

        plugins: {
            security,
        },

        rules: {
            // Base ESLint recommended rules
            ...security.configs.recommended.rules,

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

            // Security plugin rules (mirroring your overrides)
            "security/detect-buffer-noassert": "warn",
            "security/detect-child-process": "warn",
            "security/detect-disable-mustache-escape": "warn",
            "security/detect-eval-with-expression": "warn",
            "security/detect-new-buffer": "warn",
            "security/detect-no-csrf-before-method-override": "warn",
            "security/detect-non-literal-fs-filename": "warn",
            "security/detect-non-literal-regexp": "warn",
            "security/detect-non-literal-require": "off", // requirejs conflict
            "security/detect-object-injection": "off",   // false positives
            "security/detect-possible-timing-attacks": "warn",
            "security/detect-pseudoRandomBytes": "warn",
            "security/detect-unsafe-regex": "warn",
        },
    },
];

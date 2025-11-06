/* global requirejs: true */

requirejs.config({
    baseUrl: '../../media/js/',
    paths: {
        'domReady': 'lib/require/domReady',
    },
    urlArgs: 'bust=' + (new Date()).getTime()
});

define([
    'domReady',
    'src/utils'
], function(domReady, utils) {
    domReady(function() {
    });
});

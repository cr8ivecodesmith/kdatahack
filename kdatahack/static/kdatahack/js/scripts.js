/**
 * All your custom scripts go here.
 *
 * Requires: /static/assets/js/plugins.js
 *
 */


var getMasterItems = function () {
    return $.fn.restAPI({
        //urlname: 'masteritem',
        urlname: '/api/v1/masterlist/masteritem.json',
    });
};


/**
 * MAIN
 *
 */
$(document).ready(function () {
    // Start here
    getMasterItems().responseObj.done(function (data) {
        console.log(data);
    });

});

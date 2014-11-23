/**
 * All your custom scripts go here.
 *
 * Requires: /static/assets/js/plugins.js
 *
 */


var renderMasterItemDT = function (objId) {
    var args = {
        'aoColumns': [
            null, // id
            null, // item_name
            null, // item_description
            null, // uom
            null, // market_price
        ],
        'aoColumnDefs': [
            {'mRender': function (data, type, row) {
                anchor = '<a href="/item/' + row[0] + '" target="_blank">' + data + '</a>';
                return anchor;
            }, 'aTargets': [1]} // item_name
        ],
    };
    return $(objId).eztables({
        datasourceUrl: '/api/v1/masterlist/datatable',
        datatableArgs: args
    });
};

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
    renderMasterItemDT('#research-masteritem-dt-modal');
    getMasterItems().responseObj.done(function (data) {
        console.log(data);
    });

});

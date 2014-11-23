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
        urlname: '/api/v1/masterlist/masteritem.json',
    });
};


/**
 * MAIN
 *
 */
$(document).ready(function () {
    var masterItemDT = renderMasterItemDT('#research-masteritem-dt-modal');
    getMasterItems().responseObj.done(function (data) {
        console.log(data);
    });

    // Research modal datatable row highlighting
    $('#research-masteritem-dt-modal tbody').on('click', 'tr', function () {
        $(this).datatableHighlight({
            datatable: masterItemDT.datatable
        });
    });

    // Clear items
    $('#research-btn-clear-items').on('click', function () {
        $('#research-list-table').empty();
    });

    // Add items
    $('#research-btn-add-item').on('click', function() {
        var selRow = $('#research-masteritem-dt-modal tbody tr.row_selected td'),
            masterItemId = $(selRow[0]).text(),
            listRow = $('<tr></tr>');
        $.fn.restAPI({
            urlname: '/api/v1/masterlist/masteritem/' + masterItemId + '.json'
        }).responseObj.done(function (data) {
            listRow.append('<td>' + data.id + '</td>');
            listRow.append('<td>' + data.item_name + '</td>');
            listRow.append('<td>' + data.item_description + '</td>');
            listRow.append('<td>' + data.uom + '</td>');
            listRow.append('<td><input type="text" value="1" size="2"></td>');
            listRow.append('<td></td>');
            $('#research-list-table').append(listRow);
        });
    });

});

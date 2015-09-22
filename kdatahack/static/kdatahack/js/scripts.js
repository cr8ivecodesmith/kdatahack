/**
 * All your custom scripts go here.
 *
 * Requires: /static/assets/js/plugins.js
 *
 */


var renderMasterItemDT = function (objId) {
    var args = {
        //'processing': true,
        'serverSide': true,
        'ajax': '/api/v1/masterlist/datatable2',
    };
    $(objId).DataTable(args);

    /*
    return $(objId).eztables({
        datasourceUrl: '/api/v1/masterlist/datatable2',
        datatableArgs: args
    });
    */
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
    var args = {
        'processing': true,
        'serverSide': true,
        'ajax': '/api/v1/masterlist/datatable2',
    };
    var oTable = $('#research-masteritem-dt-modal').DataTable({
        'processing': true,
        'serverSide': true,
        'ajax': '/api/v1/masterlist/datatable2',
    });

    /*
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
            listRow.append('<td><a href="/item/' + data.id + '" target="_blank">' +
            data.item_name + '</a></td>');
            listRow.append('<td>' + data.item_description + '</td>');
            listRow.append('<td>' + data.uom + '</td>');
            listRow.append('<td><input type="text" value="1" size="2"></td>');
            listRow.append('<td>' + data.market_price + '</td>');
            listRow.append('<td></td>');
            $('#research-list-table').append(listRow);
        });
    });

    // Update item prices
    $('#research-btn-update-price').on('click', function () {
        var listRows = $('#research-list-table tr');
        $.each(listRows, function (i, v) {
            var cols = v.cells;
            // console.log($(cols[cols.length - 1]).text());
            // console.log($(cols[cols.length - 2]).text());
            // console.log($(cols[cols.length - 3]).text());
        });
    });
    */

});

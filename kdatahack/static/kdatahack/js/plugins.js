/**
 * All your custom plugins go here.
 */

/**
 * Django Ajax CSRF protection helpers
 * https://docs.djangoproject.com/en/1.4/ref/contrib/csrf/#ajax
 *
 */

var csrfSafeMethod = function (method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
};


var sameOrigin = function(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
};


/**
 * Generic Datatables jQuery plugin
 *
 * @param datasourceUrl - Django url name
 * @param datasourceArgs - Django url parameters
 *      list_model_id: <int>
 *
 */
;(function($, Django, window, document, undefined) {
    // Create the defaults
    var pluginName = 'eztables',
        defaults = {
            datasourceUrl: undefined,
            datasourceArgs: undefined,
            datatableArgs: {
                'bPaginate': true,
                'bProcessing': true,
                'bServerSide': true,
                'bDestroy': true,
            },
        };

    // Plugin constructor
    function Plugin(element, options) {
        this.element = element;
        this.options = $.extend(true, {}, defaults, options);
        this._defaults = defaults;
        this._name = pluginName;
        this.init();
        this.render();
    }

    /**
     * Plugin prototype code section
     * All plugin code goes here.
     */
    Plugin.prototype.init = function() {
        this.datasource = Django.url(this.options.datasourceUrl);
        if (this.options.datasourceArgs !== undefined) {
            this.options.datatableArgs['sAjaxSource'] = Django.url(this.options.datasourceUrl, this.options.datasourceArgs);
        }
        else {
            this.options.datatableArgs['sAjaxSource'] = Django.url(this.options.datasourceUrl);
        }
    };

    Plugin.prototype.render = function() {
        this.datatable = $(this.element).dataTable(this.options.datatableArgs);
    };

    Plugin.prototype.datatable = function() {
        return this.datatable;
    };

    /* End Plugin code section */

    $.fn[pluginName] = function(options) {
        return new Plugin(this, options);
    };
})(jQuery, Django, window, document);


/**
 * Restframework plugin for performing CRUD.
 *
 * @param urlname - Django url name
 * @param kwargs - Django url keyword arguments
 * @param data - Data for posting.
 * @param action - Type of supported request.
 *      'get'
 *      'post'
 *      'delete'
 *
 */
;(function($, Django, window, document, undefined) {
    // Create the defaults
    var pluginName = 'restAPI',
        defaults = {
            urlname: undefined,
            kwargs: {format: 'json'},
            data: undefined,
            action: 'get',
            ajaxSettings: {},
        };

    // Plugin constructor
    function Plugin(element, options) {
        this.element = element;
        this.options = $.extend(true, {}, defaults, options);
        this._defaults = defaults;
        this._name = pluginName;
        this.init();
    }

    /**
     * Plugin prototype code section
     * All plugin code goes here.
     */
    Plugin.prototype.init = function() {
        try {
            this.endpoint = Django.url(this.options.urlname, this.options.kwargs);
        }
        catch(e) {
            // We assume that its a regular URL
            this.endpoint = this.options.urlname;
        }

        switch (this.options.action) {
            case 'get':
                this.get();
                break;
            case 'post':
                this.post();
                break;
            case 'delete':
                this.delete();
                break;
            case 'update':
                this.update();
                break;
            default:
                return undefined;
        }
    };

    Plugin.prototype.get = function() {
        var defaults = {
            type: 'GET',
            url: this.endpoint,
        };
        var settings = $.extend(true, {}, defaults, this.options.ajaxSettings);
        this.responseObj = $.ajax(settings);
    };

    Plugin.prototype.post = function() {
        var defaults = {
            type: 'POST',
            url: this.endpoint,
            data: this.options.data,
        };
        var settings = $.extend(true, {}, defaults, this.options.ajaxSettings);
        this.responseObj = $.ajax(settings);
    };

    Plugin.prototype.delete = function() {
        var defaults = {
            type: 'DELETE',
            url: this.endpoint,
        };
        var settings = $.extend(true, {}, defaults, this.options.ajaxSettings);
        this.responseObj = $.ajax(settings);
    };

    Plugin.prototype.update = function() {
        var defaults = {
            type: 'PATCH',
            url: this.endpoint,
            data: this.options.data,
        };
        var settings = $.extend(true, {}, defaults, this.options.ajaxSettings);
        this.responseObj = $.ajax(settings);
    };

    Plugin.prototype.responseObj = function() {
        return this.responseObj;
    }

    /* End Plugin code section */

    $.fn[pluginName] = function(options) {
        return new Plugin(this, options);
    };
})(jQuery, Django, window, document);


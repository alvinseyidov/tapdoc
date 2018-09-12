/**
 * @param {{}} settings
 * @return {{}}
 */
var FastPreviewSearch = function (settings) {

    settings = $.extend({
        $form: $('form#searchForm'),
    }, settings);

    /**
     * @return {{}}
     */
    var getSearchFormParams = function () {
        var params = {};
        settings.$form.children('input').each(function (index, element) {
            var $element = $(element);
            params[$element.attr('name')] = $element.val();
        });

        return params;
    };

    /**
     * @returns {Promise<String>}
     */
    var preloadFormDoc = function () {
        var url = settings.$form.attr('action');
        url += '?pink-design=1';

        return $.post(url, getSearchFormParams()).promise();
    };

    /**
     * @param {jQuery} $card
     * @returns {{}}
     */
    var parseDoctor = function ($card) {
        var prof = $card.find('.doc__info .doc__prof').text().split('/');

        return {
            image: $card.find('img.photo_mask').attr('data-aload'),
            name: parseName($card),
            stage: parseStage($card),
            prof: prof[1] ? prof[1].split(',')[0].trim() : '',
            price: parseInt($card.find('.doc__price-value').text().trim()) || 0,
            rate: $card.find('.rate .rate__value').attr('style').match(/\d+/)[0],
            oldPrice: parseInt($card.find('.doc__price .doc__price-old').eq(0).text()) || 0,
            link: $card.find('a.doc__name').attr('href'),
        };
    };

    var parseStage = function ($card) {
        var prof = $card.find('.doc__info .doc__prof').text().split('/');
        var stage = prof[0] ? prof[0].match(/Cтаж \d+ (лет|года|год)/) : '';
        stage = stage ? stage[0] : 'Стаж -';

        return stage;
    };

    /**
     * @param {jQuery} $card
     * @return {string}
     */
    var parseName = function ($card) {
        var name = $card.find('.doc__info .doc__name').text().replace(/\s+/g, ' ').trim();
        name = name.split(' ');
        name = [name[0], name[1][0] + '.', name[2] ? name[2][0]  + '.' : ''].join(' ');

        return name;
    };

    /**
     * @param {String} html
     * @return {Object[]}
     */
    var parseDoctors = function (html) {
        var doctors = [];
        $('.result-card', html).each(function (i, card) {
            var $card = $(card);
            var isNoResult = $card.children().hasClass('noresult');

            if (isNoResult || i >= 3) {
                return false;
            }

            doctors.push(parseDoctor($card));
        });

        return doctors;
    };


    return {
        preloadFormDoc: preloadFormDoc,
        parseDoctors: parseDoctors,
        getSearchFormParams: getSearchFormParams
    };
};

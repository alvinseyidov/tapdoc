window.dataLayer = window.dataLayer || [];

(function ($, dataLayer) {
    var FirstScreen = function (fastPreview, specialistList, locationList) {
        var $document = $(document);
        var closestLocations = {};
        var formSubmitted = false;

        var specialists = specialistList.reduce(function (acc, spec) {
            acc[spec.id] = spec;
            return acc;
        }, {});

        var locations = locationList.reduce(function (acc, location) {
            var type = location.data && location.data === 'regCity' ? 'city' : 'station';
            if (!acc[type]) {
                acc[type] = {};
            }
            acc[type][location.id] = location;
            return acc;
        }, {});

        var onChangeForm = function (event) {
            var $form = $(event.target).closest('form');

            if ($form.find(':focus').length || formSubmitted) {
                return;
            }

            $document.trigger('fast-preview.reset');
            var params = fastPreview.getSearchFormParams();

            if (params.spec.length && params.stations.length) {
                if (params.isClinicList === '1') {
                    return;
                }

                $document.trigger('fast-preview.loading');

                Promise.all([getClosestStations(params.stations), fastPreview.preloadFormDoc()])
                    .then(function (results) {
                        var closestStations = results[0];
                        var html = results[1];

                        var doctors = fastPreview.parseDoctors(html);
                        var meta = {
                            spec: specialists[params.spec],
                            location: getStationById(params.stations)
                        };

                        $document.trigger('fast-preview.doctors', [doctors, meta, closestStations]);
                    })
            } else if (params.spec.length) {
                var spec = specialists[params.spec];
                $document.trigger('fast-preview.popular', [spec]);
            } else if (params.stations.length) {
                var location = getStationById(params.stations);
                $document.trigger('fast-preview.station', [location]);
            } else if (params.regcity.length) {
                var city = getCityById(params.regcity);
                $document.trigger('fast-preview.city', [city]);
            }
        };

        /**
         * @param {Number} id
         * @return {{}}
         */
        var getStationById = function (id) {
            return locations['station'][id];
        };

        /**
         * @param {Number} id
         * @return {{}}
         */
        var getCityById = function (id) {
            return locations['city'][id];
        };

        /**
         * @param {Number} stationId
         * @return {Promise}
         */
        var getClosestStations = function (stationId) {
            if (closestLocations[stationId]) {
                return Promise.resolve(closestLocations[stationId]);
            }

            return fetch('/station/closestById?id=' + stationId + '&limit=3')
                .then(function (response) {
                    return response.json();
                })
                .then(function (json) {
                    closestLocations[stationId] = json;
                    return closestLocations[stationId];
                });
        };

        var autoFocus = function (event) {
            if (formSubmitted) {
                return;
            }

            var focusOutInput = $(event.target);

            var $input1 = $('#searchForm input[name="specialist"]');
            var $input2 = $('#searchForm input[name="geo"]');

            if (focusOutInput.is($input1) && $input1.val() && !$input2.val()) {
                $input2.focus();
            } else if (focusOutInput.is($input2) && $input2.val() && !$input1.val()) {
                $input1.focus();
            }
        };

        var addToDataLayer = function (event) {
            var $element = $(event.currentTarget);

            dataLayer.push({
                elementType: 'selection',
                event: $element.data('layer-event'),
                cardType: $element.data('layer-card-type') || '-',
            });
        };

        var addToDataLayerNew = function (event) {
            var $element = $(event.currentTarget);

            dataLayer.push({
                label: 'doctor main',
                category: $element.data('category'),
                event: 'ddtrackdata',
                action: 'click',
            });
        };

        var onChangeFormHandler = $.debounce(200, onChangeForm);
        var autoFocusHandler = $.debounce(150, autoFocus);

        /**
         * Активировать обработчики событий
         */
        var on = function () {
            formSubmitted = false;
            window.addEventListener('beforeunload', off);

            $document.on('click', '.suggestions a', addToDataLayer);
            $('.suggestions-new a').on('click', addToDataLayerNew);
            $document.on('submit', '#searchForm', off);
            $document.on('blur focusout', '#searchForm input', onChangeFormHandler);
            $document.on('blur focusout', '#searchForm input', autoFocusHandler);
        };

        /**
         * Деактивировать обработчики событий
         */
        var off = function () {
            formSubmitted = true;
            window.removeEventListener('beforeunload', off);

            $document.off('click', '.suggestions a', addToDataLayer);
            $('.suggestions-new a').off('click', addToDataLayerNew);
            $document.off('submit', '#searchForm', off);
            $document.off('blur focusout', '#searchForm input', onChangeFormHandler);
            $document.off('blur focusout', '#searchForm input', autoFocusHandler);
        };

        return {
            on: on,
            off: off
        };
    };

    $(function () {
        var fs = new FirstScreen(new FastPreviewSearch, xmlDataSpeclist, xmlDataProvider);
        fs.on();

        var defaultSuggestions = $('.main__section_new_screen .suggestions').html();

        new Vue({
            el: '.main__section_new_screen .suggestions',
            template: '<fast-preview-search>' + defaultSuggestions + '</fast-preview-search>'
        });
    });
})(jQuery, window.dataLayer);

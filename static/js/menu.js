'use strict';

var $document   = $(document);
var $window     = $(window);
var $headings   = $('h3');
var $menuElems  = $('#chapter-menu').find('li');

var menu = $headings.map(function(index, el) {
    return {
        name: $(el).text(),
        $menuElem: $menuElems.eq(index),
        distanceFromTop: $(el).offset().top
    };
});

var i = 0;
var scrollDelta = 0;

var updateMenu = function(direction) {
    menu[i].$menuElem.toggleClass('highlight');
    i += direction;
    menu[i].$menuElem.toggleClass('highlight');
};

var scrollHandler = function(ev) {
    var nextIndex = i + 1; 
    var prevIndex = i - 1;
    var upperBound = menu.length;
    var lowerBound = -1;

    /* moving up the page, moving the highlighted menu index toward 0 */
    if ( nextIndex < upperBound && $window.scrollTop() > menu[nextIndex].distanceFromTop ) {
        updateMenu(+1);
    } 

    /* moving down the page, moving the highlighted menu index toward men.length */
    else if ( prevIndex > lowerBound && $window.scrollTop() < menu[prevIndex].distanceFromTop ) {
        updateMenu(-1);
    }
};


menu[i].$menuElem.toggleClass('highlight');
$document.on('scroll', scrollHandler);

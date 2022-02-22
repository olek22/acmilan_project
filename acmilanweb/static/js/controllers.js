var portfolioApp = angular.module('portfolioApp',[]);

portfolioApp.controller('GalleryListCtrl', function($scope)
{
    $scope.galleries = 
    [
        { 'title':'Ateny',
        'when':'Maj 2007',
        'thumbnailUrl':'img/2007.jpg'
        },
        { 'title':'Manchester',
        'when':'Maj 2003',
        'thumbnailUrl':'img/2003.jpg'
        },
        { 'title':'Ateny',
        'when':'Maj 1994',
        'thumbnailUrl':'img/1994.jpg'
        },
        { 'title':'Wieden',
        'when':'Maj 1990',
        'thumbnailUrl':'img/1990.jpg'
        },
        { 'title':'Barcelona',
        'when':'Maj 1989',
        'thumbnailUrl':'img/1989.jpg'
        },
        { 'title':'Madryt',
        'when':'Maj 1969',
        'thumbnailUrl':'img/1969.jpg'
        }
    ];
    $scope.sortList = 
    [
        {
            'label':'alfabetycznie',
            'value':'title'
        },
        {
            'label':'chronologicznie',
            'value':'when'
        },
        {
            'label':'od najnowszych',
            'value':'-when'
        },
    ];
    
});
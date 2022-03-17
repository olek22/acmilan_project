
var portfolioApp = angular.module('portfolioApp',[]);

portfolioApp.controller('GalleryListCtrl', function($scope)
{
    $scope.galleries = 
    [
        { 'title':'Athens',
        'when':'May 2007',
        'thumbnailUrl':'/media/img/2007.jpg'
        },
        { 'title':'Manchester',
        'when':'May 2003',
        'thumbnailUrl':'/media/img/2003.jpg'
        },
        { 'title':'Athens',
        'when':'Maj 1994',
        'thumbnailUrl':'/media/img/1994.jpg'
        },
        { 'title':'Vienna',
        'when':'May 1990',
        'thumbnailUrl':'/media/img/1990.jpg'
        },
        { 'title':'Barcelona',
        'when':'Maj 1989',
        'thumbnailUrl':'/media/img/1990.jpg'
        },
        { 'title':'Madrid',
        'when':'May 1969',
        'thumbnailUrl':'/media/img/1969.jpg'
        }
    ];
    $scope.sortList = 
    [
        {
            'label':'alphabetic',
            'value':'title'
        },
        {
            'label':'chronological',
            'value':'when'
        },
        {
            'label':'latest',
            'value':'-when'
        },
    ];
    
});
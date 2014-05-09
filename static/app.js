var app = angular.module("myApp", []);
app.controller("myCtrl", function($scope, $http){
    $scope.searchInput=null;
    $scope.submit = function(){
        $http.post('http://projfootball.web.engr.illinois.edu/410.py',{
            'search':$scope.searchInput
        })
        .success(function(data, status, headers, config){
        
        })
        .error(function(data, status, headers, config){
        
        });
    }
});
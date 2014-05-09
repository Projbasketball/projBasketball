var app = angular.module("myApp", []);
app.controller("myCtrl", function($scope, $http){
    $scope.searchInput=null;
    $scope.submit = function(){
        if($scope.searchInput!=null){
            $http.post('/search',{
                'search':$scope.searchInput
            })
            .success(function(data, status, headers, config){

            })
            .error(function(data, status, headers, config){

            });
        }
    }
});
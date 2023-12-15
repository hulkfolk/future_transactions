(function () 
{
  'use strict';

  angular.module('futureTransactions', [])

  // Setting up new interpolation delimiter which does not conflict with Jinja2
  .config(['$interpolateProvider', function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  }])

  .controller('transactionsCtrl', ['$scope', '$http', function($scope, $http) {
        $http.get("http://localhost:5000/v1/report/getData")
        .then(function (response) {
            $scope.items = response.data.items;
    });
  }])

}()
);
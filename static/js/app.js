/**
 * Created by Gabori Peter on 2017. 09. 14..
 */
var app = angular.module("restaurants", ["ui.router"]);
app.config(function ($stateProvider) {
    $stateProvider
        .state("/", {
            url: "",
            templateUrl: "/static/partials/home.html"
        })
        .state("/registration", {
            url: "/registration",
            templateUrl: "/static/partials/registration.html",
            controller: "userController"
        })
        .state("/restaurant", {
            url: "/restaurant",
            templateUrl: "/static/partials/restaurant.html",
            controller: "restaurantController"
        })
        .state("/list-meals", {
            url: "/list-meals/:restaurant_id",
            templateUrl: "/static/partials/list_meals.html",
            controller: "mealsController"
        })
});
app.controller("userController", function ($scope, $rootScope, $http, $state) {
    $scope.registration = function () {
        $http.post("/registration", $scope.user).then(
            function (response) {
                $scope.statusCode = response.status;
            },
            function (response) {
                $scope.statusCode = response.status;
            });
    };
});


app.controller("restaurantController", function ($scope, $rootScope, $http, $state, $stateParams) {
    $http.get("/restaurants").then(
        function (response) {
            $scope.restaurants = response.data;
        });
    $http.get("/users").then(
        function (response) {
            $scope.users = response.data;
        });
    $http.get("/orders").then(
        function (response) {
            $scope.orders = response.data;
        });
    $http.get("/cities").then(
        function (response) {
            $scope.cities = response.data;
        });
    $http.get("/payments").then(
        function (response) {
            $scope.payments = response.data;
        });

});

app.controller("mealsController", function ($scope, $rootScope, $http, $state, $stateParams) {
    $http.get("/meals", {params: {restaurant_id: $stateParams.restaurant_id}}).then(
        function (response) {
            $scope.meals = response.data;
        });
    if ($scope.cart === undefined) {
        $scope.cart = [];
    }
    $scope.amount = 0;
    $scope.addToCart = function (meal) {
        $scope.cart.push(meal);
        $scope.amount = $scope.amount + meal.meal_price;
        console.log($scope.cart);
    };

    $scope.checkout = function () {
        $http.post("/checkout", $scope.cart, $scope.amount).then(
            function (response) {
                $scope.statusCode = response.status;
            },
            function (response) {
                $scope.statusCode = response.status;
            }
        );
    }
});

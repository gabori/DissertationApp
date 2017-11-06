/**
 * Created by Gabori Peter on 2017. 09. 14..
 */
angular.module('Authentication', []);

var app = angular.module("restaurants", ["Authentication", "ngCookies", "ui.router"]).run(['$rootScope', '$location', '$cookieStore', '$http',
    function ($rootScope, $location, $cookieStore, $http) {
        // keep user logged in after page refresh
        $rootScope.globals = $cookieStore.get('globals') || {};
        if ($rootScope.globals.currentUser) {
            $http.defaults.headers.common['Authorization'] = 'Basic ' + $rootScope.globals.currentUser.username; // jshint ignore:line
        }

        $rootScope.$on('$locationChangeStart', function (event, next, current) {
            // redirect to login page if not logged in
            if ($location.path() !== '' && !$rootScope.globals.currentUser) {
                $location.path('');
            }
        });
    }]);
;
app.config(function ($stateProvider) {
    $stateProvider
        .state("/", {
            url: "",
            templateUrl: "/static/partials/home.html",
            controller: "loginController"
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
        .state("/addRestaurant", {
            url: "/addRestaurant",
            templateUrl: "/static/partials/add_restaurant.html",
            controller: "restaurantController"
        })
});

app.controller("mainController", function ($scope, $rootScope, $http, $stateParams) {
    $rootScope.loginUser = {};
});

app.controller("loginController", ['$scope', '$rootScope', '$location', 'AuthenticationService',
    function ($scope, $rootScope, $location, AuthenticationService) {
        // reset login status
        AuthenticationService.ClearCredentials();

        $scope.login = function () {
            $scope.dataLoading = true;
            AuthenticationService.Login($scope.username, $scope.password, function (response) {
                console.log(response)
                if (response.status == 200) {
                    $scope.user_role = response.data.user_role
                    AuthenticationService.SetCredentials($scope.username, $scope.password, $scope.user_role);
                    $location.path('/restaurant');
                } else {
                    $scope.error = response.message;
                    $scope.dataLoading = false;
                }
            });
        };
    }]);

app.controller("userController", function ($scope, $rootScope, $http, $state) {
    console.log($rootScope.user)

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
            console.log($scope.restaurants)
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

    $scope.addRestaurant = function () {
        $http.post("/addRestaurant", $scope.restaurant).then(
            function (response) {
                $scope.statusCode = response.status;
            },
            function (response) {
                $scope.statusCode = response.status;
            });
    };
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

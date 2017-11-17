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
        .state("/startpage", {
            url: "/startpage",
            templateUrl: "/static/partials/startpage.html"
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
        .state("/myRestaurant", {
            url: "/myRestaurant/:username",
            templateUrl: "/static/partials/my_restaurants.html",
            controller: "restaurantController"
        })
        .state("/list-meals", {
            url: "/list-meals/:restaurant_id",
            templateUrl: "/static/partials/list_meals.html",
            controller: "mealsController"
        })
        .state("/setting-meals", {
            url: "/setting-meals/:restaurant_id",
            templateUrl: "/static/partials/setting_meals.html",
            controller: "mealsSettingController"
        })
        .state("/add-meal", {
            url: "/add-meal",
            templateUrl: "/static/partials/add_meal.html",
            controller: "mealsAddController"
        })
        .state("/addRestaurant", {
            url: "/addRestaurant",
            templateUrl: "/static/partials/add_restaurant.html",
            controller: "restaurantController"
        })
        .state("/my-orders", {
            url: "/my-orders/:restaurant_id",
            templateUrl: "/static/partials/get_orders.html",
            controller: "ordersController"
        })
        .state("/my-profile", {
            url: "/my-profile",
            templateUrl: "/static/partials/my_profile.html",
            controller: "userProfileController"
        })

        .state("/edit-profile", {
            url: "/edit-profile/:user_id",
            templateUrl: "/static/partials/edit_password.html",
            controller: "userSettingsController"
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
                    $location.path('/startpage');
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

    $http.get("/myRestaurant", {params: {username: $stateParams.username}}).then(
        function (response) {
            $scope.my_restaurants = response.data;
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
    $scope.pay= undefined;
    $http.get("/payments").then(
        function (response) {
            $scope.payments = response.data;
        });

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
        var in_data = {'cart': $scope.cart, 'username': $rootScope.globals.currentUser.username, 'payment': $scope.pay};
        $http.post("/checkout", in_data).then(
            function (response) {
                $scope.statusCode = response.status;
            },
            function (response) {
                $scope.statusCode = response.status;
            }
        );
    }
});


app.controller("mealsSettingController", function ($scope, $rootScope, $http, $state, $stateParams) {
    $http.get("/meals", {params: {restaurant_id: $stateParams.restaurant_id}}).then(
        function (response) {
            $scope.meals = response.data;
        });
    $scope.removeMeal = function (meal) {
        $scope.meal = meal
        $http.post("/removeMeal", $scope.meal).then(
            function (response) {
                $state.reload();
                $scope.statusCode = response.status;
            },
            function (response) {
                $scope.statusCode = response.status;
            }
        );
    };
});

app.controller("mealsAddController", function ($scope, $rootScope, $http, $state) {
    console.log($scope.meal)
    $scope.user = $rootScope.globals.currentUser.username
    $scope.addMeal = function () {
        $http.post("/addMeal", $scope.meal, $scope.user).then(
            function (response) {
                $scope.statusCode = response.status;
            },
            function (response) {
                $scope.statusCode = response.status;
            }
        );
    };
});

app.controller("ordersController", function ($scope, $rootScope, $http, $stateParams) {
    $scope.username = $rootScope.globals.currentUser.username;
    $http.get("/myOrders", {params: {username: $scope.username, restaurant_id: $stateParams.restaurant_id}}).then(
        function (response) {
            $scope.orders = response.data;
            console.log($scope.orders)
        });
});

app.controller("userSettingsController", function ($scope, $rootScope, $http, $state) {
    $scope.current_user = $rootScope.globals.currentUser.username
    $http.get("/userData", {params: {username: $scope.current_user}}).then(
        function (response) {
            $scope.user = response.data;
            console.log($scope.user)
        });


    $scope.editUser = function () {
        var in_data = {'modified_user': $scope.modified_user, 'username': $rootScope.globals.currentUser.username};
        console.log($scope.modified_user)
        $http.post("/editUser", in_data).then(
            function (response) {
                $scope.statusCode = response.status;
            },
            function (response) {
                $scope.statusCode = response.status;
            },
            function (response) {
                $scope.statusCode = response.status;
            }
        );
    };
});

app.controller("userProfileController", function ($scope, $rootScope, $http, $state) {
    $scope.current_user = $rootScope.globals.currentUser.username
    $http.get("/userData", {params: {username: $scope.current_user}}).then(
        function (response) {
            $scope.user = response.data;
            console.log($scope.user)
        });
});

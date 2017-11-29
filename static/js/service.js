/**
 * Created by Gabori Peter on 2017. 11. 05..
 */
'use strict';

angular.module('Authentication')
    .factory('AuthenticationService',
        ['$http', '$cookieStore', '$rootScope',
            function ($http, $cookieStore, $rootScope) {
                var service = {};

                service.Login = function (username, password, callback) {
                    $http.post('/login', {username: username, password: password})
                        .then(function (response) {
                            if (response.status == 200) {
                                callback(response);
                            }
                            if (response.status == 202) {
                                callback(response);
                            }
                        });
                };

                service.SetCredentials = function (username, password, user_role, token) {
                    $rootScope.globals = {
                        currentUser: {
                            username: username,
                            user_role: user_role,
                            token: token
                        }
                    };
                    console.log($rootScope.globals);
                    $http.defaults.headers.common['Authorization'] = 'Basic ' + token; // jshint ignore:line
                    $cookieStore.put('globals', $rootScope.globals);
                };

                service.ClearCredentials = function () {
                    $rootScope.globals = {};
                    $cookieStore.remove('globals');
                    $http.defaults.headers.common.Authorization = 'Basic ';
                };

                return service;
            }]);

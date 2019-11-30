angular.module("heavyChallenge").factory("genericService", function($http, config){
	
	let _defaultErrorFunction = function(error){
		console.log(error);
	};

	let _defaultSuccessFunction = function(response){
		console.log("Success");
	};

	let _treatPromise = function(promise, success, error){
		if(success != undefined || error != undefined){
			if(success == undefined) success = _defaultSuccessFunction;
			if(error == undefined) error = _defaultErrorFunction;
			promise.then(success,error);
		}
	};

	let _get = function(urlComplement, parameters={}, success=undefined, error=undefined){
		let promise = $http.get(config.baseUrl+urlComplement, {params:parameters});
		_treatPromise(promise, success, error);
		return promise;
	};

	let _post = function(urlComplement, data, parameters={}, success=undefined, error=undefined){
		let promise = $http.post(config.baseUrl+urlComplement, data, {params:parameters});
		_treatPromise(promise, success, error);
		return promise;
	};

	return {
		get : _get,
		post : _post
	};
});

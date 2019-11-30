angular.module("heavyChallenge").service("userService", function(genericService){

	this.getUsers = function(success){
		genericService.get("users").then(success);
	};
	
});

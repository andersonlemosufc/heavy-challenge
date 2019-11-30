angular.module("heavyChallenge").service("reportService", function(genericService){

	this.getReports = function(success){
		return genericService.get("reports").then(success);
	};

});

angular.module("heavyChallenge").controller("heavyChallengeController", function($scope, reportService, userService){ 

	$scope.teste = "Anderson Lemos";
	$scope.users = [];
	$scope.reports = [];
	$scope.sortCriteria = "";
	$scope.selectedUser = undefined;

	$scope.filterReports = function(selectedUser){

		return function(report) {
			if(selectedUser == undefined) return true;
			if(report.author.id == selectedUser) return true;
			for(let supervisor of report.supervisors){
				if(supervisor.id == selectedUser) return true;
			}
			return false;
		};
	};

	$scope.orderBy = function(param){
		if($scope.sortCriteria==param) $scope.sortCriteria = '-'+param;
		else $scope.sortCriteria = param;
	};

	let loadData = function() {
		userService.getUsers(function(response){
			$scope.users = response.data;
		});

		reportService.getReports(function(response){
			$scope.reports = response.data;
			$scope.reportsToShow = angular.copy($scope.reports);
		});	
	};

	loadData();	
});

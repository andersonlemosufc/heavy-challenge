## About the test data

Initially, I was thinking of doing the test data randomly (the authors, supervisors, and responses). However, in testing, to make sure things are working correctly, it is better to use a pattern. So the data was created as follows:

- 20 users with primary keys from 1 to 20.
- 100 reports with primary keys from 1 to 100.
- 200 responses to reports.

Each report has:

- An author.
- Two supervisors.
- Two responses.

Since there are 100 reports and 20 users, each user is the author of 5 reports:

- Let k be the primary key of each user (i.e. k = 1, 2, ..., 20):
	- User k is the author of reports from 5k-4 to 5k
		- For example:
			- User 1 is the author of reports 1 to 5.
			- User 2 is the author of reports 6 to10.
			 ...
			- User 20 is the author of reports 96 to 100.

Each user is the supervisor of 10 reports and responds reports that are a supervisor (i.e. 10 responses). Since there are 20 users, we have 200 responses.
- Let k be the primary key of each user (i.e. pk = 1, 2, ..., 20):
	- User k is a supervisor and responds to reports from (5k% 100) +1 to ((5k + 9)% 100) +1 (assuming the range is circular, i.e. after report 100 we have report 1).
		- For example:
			- User 1 supervises and responds to reports 6 to 15.
			- User 2 supervises and responds to reports 11 to 20.
			...
			- User 18 oversees and responds to reports 91 to 100.
			- User 19 oversees and responds to reports 96 to 5.
			- User 20 oversees and responds to reports 1 to 10.
		- Thus no user supervises or responds to their report.


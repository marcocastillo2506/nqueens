requires sqlalchemy, postgres, and pytest.

Todo: <br>
add tests for all kinds of stuff.<br>
Dockerize<p>
Tests: https://travis-ci.org/seisvelas/nqueens <p>

<b>Original Text of Challenge</b><p>
Here's the programming problem: https://en.wikipedia.org/wiki/Eight_queens_puzzle<p>

These are the different aspect of the project you can work on (in order):<br>
1. determine all possible solutions for a given N where N ≥ 8 (within 10 mins on a laptop). Bonus points for a higher N where N is the size of the board / number of queens<br>
2. iterate over N and store the solutions in postgres using SQLAlchemy<br>
3. write basic tests that at least verify the number of solutions for a given N match what's online. I recommend using pytest<br>
4. Docker-ize the solution, so that I can run the code and tests without any assumption of my local setup (including running a postgres instance in docker-compose)<br>
5. setup Travis CI (or similar) for your public GitHub repo to run the tests automatically<p>

You don't need to go through all of the steps, but there should be instructions on how I can run the code. I mainly want to see how you approach a problem and your coding style. There are multiple steps so you have the option to show me different skills. It's up to you.<p>

Please commit everything in a public GitHub repo and use python3.

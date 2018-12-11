from ..nqueens import nqueens, psql_insert_queens, Solution
from .fixtures import sol_sizes


def test_nq():
    from_n = 9  # test nqueens/psql_insert_queens for n=1,n=2,...,n=from_n

    # Below we abuse a passing knowledge of functional programming to
    # convert what was once a few elegant, easily readible lines
    # of straightforward, Pythonic imperative code into a hideous
    # incomprehensible mess. Looking at the proceeding line reminds
    # me of why Haskell and Lisp not only will not, but do not deserve,
    # to ever become mainstream industrial programming languages.
    assert False not in map(lambda x: psql_insert_queens(x, nqueens(x)).query(Solution).filter_by.count() == sol_sizes[x-1])

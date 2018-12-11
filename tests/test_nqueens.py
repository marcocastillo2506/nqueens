from ..nqueens import nqueens, psqlize_queens, Solution
from .fixtures import sol_sizes


def test_nq():
    from_n = 9  # test nqueens/psql_insert_queens for n=1,n=2,...,n=from_n

    assert False not in map(
        lambda x: psqlize_queens(x, nqueens(x)).query(Solution).filter_by(n=x).count() == sol_sizes[x-1],
        range(1, from_n + 1))

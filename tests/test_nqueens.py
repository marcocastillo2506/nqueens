from ..nqueens import nqueens, psqlize_queens, Solution
from .fixtures import sol_sizes


def test_nq():
    from_n = 9  # test nqueens/psql_insert_queens for n=1,n=2,...,n=from_n

    # the old while loop version was better imma change it back in a sec
    assert filter(
        lambda n: psqlize_queens(n, nqueens(n)).query(Solution).filter_by(n=n).count() == sol_sizes[n],
        range(1, from_n + 1))

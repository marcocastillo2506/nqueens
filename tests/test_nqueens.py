from ..nqueens import nqueens, psql_insert_queens, Solution
from .fixtures import OEIS_solution_sizes


def test_nq():
    from_n = 9

    while from_n:
        queen_gen = nqueens(from_n)
        session = psql_insert_queens(from_n, queen_gen)
        assert session.query(Solution).filter_by(n=from_n).count() == OEIS_solution_sizes[from_n-1]
        from_n -= 1

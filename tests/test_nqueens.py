from ..nqueens import nqueens, psql_insert_queens, Solution
from .fixtures import OEIS_solution_sizes


def test_nq():
    from_n = 8

    while from_n:
        queen_gen = nqueens(from_n)
        session = psql_insert_queens(from_n, queen_gen)
        assert session.query(Solution).filter_by(n=8).count() == OEIS_solution_sizes[7]
        from_n -= 1

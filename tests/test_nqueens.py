import nqueens
from . import fixtures


def test_nq():
    from_n = 8

    while from_n:
        queen_gen = nqueens.nqueens(from_n)
        session = nqueens.psql_insert_queens(from_n, queen_gen)
        assert session.query(nqueens.Solution).filter_by(n=from_n).count == fixtures.OEIS_solution_sizes[from_n-1]
        from_n -= 1

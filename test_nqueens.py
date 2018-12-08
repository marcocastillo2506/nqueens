from nqueens import nqueens
from OEIS import OEIS_solution_sizes

def test_nq():
    from_n = 8

    nq = nqueens()
    while from_n:
        assert len(list(nq.solve(from_n))) == OEIS_solution_sizes[from_n-1]
        from_n -= 1

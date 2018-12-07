from sqlalchemy import *  ## Our poor, poor global namespace

## nqueens 'public' methods: solve(n=8), psql_commit(user, passw, db, port)
class nqueens:
    n = None
    
    def __init__(self, n=None):
        if n is not None:
            self.n = n
        
    def threatened(self, pos, past, n):
        for i in range(len(past)):
            if past[i] == pos or abs(pos - past[i]) == len(past) - i:
                return True
        return False

    def nqueens_gen(self, n, past=None):
        if past == None:
            for i in range(n):
                yield from self.nqueens_gen(n, [i+1])
        else:
            if len(past) == n:
                yield past[:]
            else:
                for pos in range(1,n+1):
                    if not self.threatened(pos, past, n):
                        yield from self.nqueens_gen(n,past + [pos])

    def solve(self, n=8):
        self.n = n
        self.nqg = self.nqueens_gen(n)
        return self.nqg

    def psql_commit(self, user="postgres", passw="", db="", port=5432):
        assert self.nqg is not None # must call self.solve() first.
        engine = create_engine('postgresql://%s:%s@localhost:%i/%s' %
                               (user, passw, port, db))

        ## Create solutions table if not exists
        
        meta = MetaData()
        solutions = Table("solutions", meta,
                        Column("n", Integer),
                        Column("sol", String(512)))
        
        if not engine.dialect.has_table(engine, "solutions"):
            solutions.create(engine)

        for solution in self.nqg:
            ins = solutions.insert().values(n=self.n, sol=",".join([str(i) for i in solution]))
            engine.execute(ins)            

nq = nqueens()

nq.solve(8) # returns a generator of solutions, also saves generator of n queens inside object
            # that can then be committed to db
            
nq.psql_commit("postgres", "fl33021", "queens")

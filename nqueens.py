from sqlalchemy import *  ## Our poor, poor global namespace
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine(os.environ['DB_URI'])

Base = declarative_base()

class Solution(Base):
    __tablename__ = 'solutions'

    n = Column(Integer)
    sol = Column(VARCHAR(512), primary_key=True)

    def __repr__(self):
        return "<User(n='%s', sol='%s')>" % (
                             self.n, self.sol)


def threatened(pos, past, n):
    for i in range(len(past)):
        if past[i] == pos or abs(pos - past[i]) == len(past) - i:
            return True
    return False


def nqueens(n, past=None):
    if past == None:
        for i in range(n):
            yield from nqueens(n, [i+1])
    else:
        if len(past) == n:
            yield past[:]
        else:
            for pos in range(1,n+1):
                if not threatened(pos, past, n):
                    yield from nqueens(n,past + [pos])


def psqlize_queens(n, queen_generator):
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    for sol in queen_generator:
        solution = Solution(n=n, sol=",".join(map(str, sol)))
        session.merge(solution)

    session.commit()

    return session

##
#### Example: Insert all 8 queens solutions into db:
## session.query(Solution).filter_by(n=12).count
##
## n = 8
## queen_gen = nqueens(n)
## psql_insert_queens(n, queen_gen)
##
##
##  Now, psql_insert_queens returns the session object (which is also creates, which is bad design, but anyway)
##  which is consequential, because it allows us to continue querying the db. This is useful for our tests!


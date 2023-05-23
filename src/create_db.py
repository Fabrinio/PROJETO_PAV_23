from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine('postgresql://postgres:#LFls1412@localhost:5432/PROJETO_PAV2023')
Base.metadata.create_all(engine)
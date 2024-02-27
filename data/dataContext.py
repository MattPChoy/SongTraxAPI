from sqlalchemy import create_engine
from sqlalchemy.sql.selectable import Select
from sqlalchemy.orm import Session

engine = create_engine('sqlite:///./database.db')

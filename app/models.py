from sqlalchemy import Column, Integer, String, Float
from .database import Base


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    rfc = Column(String, index=True)
    curp = Column(String, index=True)
    gender = Column(String, index=True)
    income = Column(Float)
    address_input = Column(String)

    status = Column(String)
    credit_score = Column(Integer)
    explanation = Column(String)



class Decision(Base):
    __tablename__ = "decisions"

    id = Column(Integer, primary_key=True)
    application_id = Column(Integer)
    rule_name = Column(String)
    result = Column(String)
    reason = Column(String)

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    application_id = Column(Integer)
    file_path = Column(String)
    extracted_name = Column(String)
    extracted_address = Column(String)
    extracted_date = Column(String)

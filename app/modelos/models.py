from datetime import datetime
from sqlalchemy import (Table, Column, Numeric, String, Integer, DateTime, ForeignKey, create_engine, desc)
from sqlalchemy.orm import Relationship, backref, sessionmaker
from app import db

class Person(db):
    __tablename__ = "persons"
    identificationNationalDocument = Column(Integer(), primary_key=True)
    firstName = Column(String(30))
    lastName = Column(String(30))
    workIndentifitionID = Relationship("EmployeeAssistance", backref="persons")

    def __repr__(self):
        return f'{self.identificationNationalDocument} - {self.firstName} {self.lastName} '
    



class EmployeeAssistance(db):
    __tablename__ = "employeeAssistances"

    workIndentifition = Column(Integer(), ForeignKey("person.identificationNationalDocument"))
    passing = Column(String(datetime.now().strftime('%H:%M')))
    date = Column(DateTime(), datetime.now().strftime('%Y-%m-%d'))



class WorkHours(db):
    __tablename__ = "workingHours"

    date = Column(DateTime(), datetime.now().strftime('%Y-%m-%d'))
    hours = Column(Integer())
    employee = Relationship("EmployeeAssistance", backref="persons")


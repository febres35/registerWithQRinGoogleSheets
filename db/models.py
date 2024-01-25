from datetime import datetime
from sqlalchemy import ( Column, String, Integer, DateTime, ForeignKey)
from sqlalchemy.orm import relationship, backref
from db.db import BASE, session

class Employee(BASE): 
    __tablename__ = "employees"
    workIndentifition = Column(Integer(), primary_key=True)
    identificationNationalDocument = Column(Integer())
    firstName = Column(String(30))
    lastName = Column(String(30))
    assistance = relationship("EmployeeAssistance")
    hours = relationship("WorkHours")
    def __repr__(self):
        return f'{self.identificationNationalDocument} - {self.firstName} {self.lastName} '
    
    @classmethod
    def insert(cls, dni, fn, ln):
        p1 = Employee(identificationNationalDocument = dni, firstName=fn, lastName=ln)
        session.add(p1)
        session.commit()

class EmployeeAssistance(BASE):
    __tablename__ = "employeeAssistances"
    
    id = Column(Integer(), primary_key=True)
    weId = Column(Integer(), ForeignKey("employees.workIndentifition"))
    passing = Column(String(12), default=datetime.now().strftime('%H:%M'))
    date = Column(DateTime(), default=datetime.now().strftime('%Y-%m-%d'))



class WorkHours(BASE):
    __tablename__ = "workingHours"

    date = Column(DateTime(), default=datetime.now())   
    hours = Column(Integer())
    employee = Column(Integer(), ForeignKey("employees.workIndentifition"), primary_key=True)



import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship ,sessionmaker


DATABASE = 'postgres+psycopg2://postgres:@localhost:2341/MyData'
engine = create_engine(DATABASE)
Session = sessionmaker(bind=engine)

Base = declarative_base()

student_teacher = Table('student_teacher',Base.metadata,Column('student_teacher',String,ForeignKey('student.student_data')),Column('class_id',String,ForeignKey('teacher.class_id')))

class Student(Base):
    __tablename__ = 'student'
    student_data = Column(String,primary_key = True)
    direction=Column(String,ForeignKey('success.direction'))
    m_class = Column(String)
    receipt_date = Column(String)
    teachers = relationship("Teacher",secondary = student_teacher)
    def __init__(self,student_data,direction,m_class,receipt_date):
        self.student_data = student_data
        self.direction = direction
        self.m_class = m_class
        self.receipt_date = receipt_date

class Teacher(Base):
    __tablename__ = 'teacher'
    class_id = Column(String,primary_key = True)
    lesson_count = Count(Integer)
    def  __init__(self,class_id,lesson_count):
        self.class_id=class_id
        self.lesson_count = lesson_count

class Success(Base):
    __tablename__ = 'success'
    direction = Column(String)
    score = Column(Integer)
    semester = Column(Integer)
    subject = Column(String)
    def  __init__(self,direction,score,semester,subject):
        self.direction=direction
        self.score=score
        self.semester=semester
        self.subject=subject

class School_class(Base):
    __tablename__ = 'school_class'
    class_id = Column(String,primary_key = True)
    class_count = Column(Integer)
    class_number =Column(Integer)
    def __init__(self,class_id,class_count,class_number):
        self.class_id = class_id
        self.class_count = class_count
        self.class_number=class_number

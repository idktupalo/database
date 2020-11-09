import psycopg2
from psycopg2 import errors
from model import * 
from view import *


def connect():
    user_command=input('Enter the request number >>> ')
    if user_command =='5':
        try:
            search()
            sys.exit()
        except psycopg2.Error as err:
            print(err.pgcode)
            print(f'Error {err}')

    table=input('Enter table name >>> ')
    if((table =='student')or(table=='success')):
        print('Student and Success connection 1:N , changes in the "direction" column , touch both tables >>>')
        print(f'Student column >>> {student_m}')
        print(f'Success column >>> {success_m}')
        try:
            if(user_command=='1'):
                update(table)
            elif(user_command=='2'):
                add(table)
            elif(user_command=='3'):
                delete(table)
            elif(user_command=='4'):
                rand_row(table)
            else:
                print("Error:wrong command")
                sys.exit()
        except psycopg2.Error as err:
            print(err.pgcode)
            print(f'Error {err}')
    if((table=='class')or(table=='teacher')):
        print('Teacher and Class connection 1:N , changes in the "id_class" column , touch both tables >>>')
        print(f'Teacher column >>> {teacher_m}')
        print(f'Class column >>> {class_m}')
        try:
            if(user_command=='1'):
                update(table)
            elif(user_command=="2"):
                add(table)
            elif(user_command=='3'):
                delete(table)
            elif(user_command=='4'):
                rand_row(table)
            else:
                print("Error:wrong command")
                sys.exit()
        except psycopg2.Error as err:
            print(err.pgcode)
            print(f'Error {err}')
    else:
        print("WRONG TABLE NAME")

def main():
   	table()
   	connect()

if __name__ == '__main__':
    main()

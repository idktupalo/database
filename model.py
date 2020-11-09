import psycopg2
from psycopg2 import errors
import time
import sys

student_m = ['student_data','direction','class','receipt_date']
class_m = ['id_class','class_count','class_number']
success_m = ['direction','score','semester','subject']
teacher_m = ['class_id','lesson_count']

def column_info(table_name,column_name):
	connec_t = psycopg2.connect(dbname='MyData' ,user='postgres',password='',host='localhost',port=5432)
	connec_t.set_session(autocommit=True)
	curso_r=connec_t.cursor()
    curso_r.execute(f"SELECT {column_name} FROM {table_name}")
    k=curso_r.fetchall()
    print(k)
    curso_r.close()
	connec_t.close()

def double_update(name1,name2,column):
	connec_t = psycopg2.connect(dbname='MyData' ,user='postgres',password='',host='localhost',port=5432)
	connec_t.set_session(autocommit=True)
	curso_r=connec_t.cursor()
    old_name=input('Enter old name >>> ')
    new_name = input('Enter new name >>> ')
    global column2
    if(name1=='class'):
        try:
            column2='class_id'
            insert_command = "WITH " + name1 + " AS (UPDATE " + name1 + " SET " + column + " = '" + new_name + "' WHERE " + column + " = '"+ old_name + "')" + " UPDATE " + name2 + " SET " + column2 + " = '" + new_name + "' WHERE " + column2 + " = '"+ old_name + "'"
            curso_r.execute(insert_command)
        except psycopg2.Error as err:
            print(err.pgcode)
            print(f'Error {err}')
    elif(name1=='teacher'):
        try:
            column2='id_class'
            insert_command = "WITH " + name1 + " AS (UPDATE " + name1 + " SET " + column + " = '" + new_name + "' WHERE " + column + " = '"+ old_name + "')" + " UPDATE " + name2 + " SET " + column2 + " = '" + new_name + "' WHERE " + column2 + " = '"+ old_name + "'"
            curso_r.execute(insert_command)
        except psycopg2.Error as err:
            print(err.pgcode)
            print(f'Error {err}')
    else:
        try:
            insert_command = "WITH " + name1 + " AS (UPDATE " + name1 + " SET " + column + " = '" + new_name + "' WHERE " + column + " = '"+ old_name + "')" + " UPDATE " + name2 + " SET " + column + " = '" + new_name + "' WHERE " + column + " = '"+ old_name + "'"
            curso_r.execute(insert_command)
        except psycopg2.Error as err:
            print(err.pgcode)
            print(f'Error {err}')
    curso_r.close()
	connec_t.close()

def solo_update(name1,column):
	connec_t = psycopg2.connect(dbname='MyData' ,user='postgres',password='',host='localhost',port=5432)
	connec_t.set_session(autocommit=True)
	curso_r=connec_t.cursor()
    old_name=input('Enter old name >>> ')
    new_name = input('Enter new name >>> ')
    insert_command = "UPDATE " + name1 + " SET " + column + " =  '" + new_name + "' WHERE " + column + " = '"+ old_name + "'"
    curso_r.execute(insert_command)
    curso_r.close()
	connec_t.close()

def update(table_name):
	connec_t = psycopg2.connect(dbname='MyData' ,user='postgres',password='',host='localhost',port=5432)
	connec_t.set_session(autocommit=True)
	curso_r=connec_t.cursor()
    column_name=input('Enter column name >>> ')
    column_info(table_name,column_name)
    if(((table_name=='student')or(table_name=='success'))and(column_name=='direction')):
        try:
            double_update('student','success','direction')
        except psycopg2.errors.ForeignKeyViolation:
            print(f'Error')
    elif((table_name=='class')or(table_name=='teacher')):
        try:
            if(column_name=='id_class'):
                double_update('class','teacher','id_class')
            elif(column_name=='class_id'):
                double_update('teacher','class','class_id')
        except psycopg2.Error as err:
            print(err.pgcode)
            print(f'Error {err}')
    else:
        try:
            solo_update(table_name,column_name)
        except psycopg2.Error as err:
            print(err.pgcode)
            print(f'Error {err}')
    curso_r.close()
	connec_t.close()

def add(table_name):
	connec_t = psycopg2.connect(dbname='MyData' ,user='postgres',password='',host='localhost',port=5432)
	connec_t.set_session(autocommit=True)
	curso_r=connec_t.cursor()
    i=0
    mass=[]
    if(table_name=='student'):
        print("Enter 4 value >>> ")
        while(i<4):
            key=input()
            mass.append(key)
            i+=1
        table_name2 = 'success'
        insert_command = "WITH " + table_name + " AS " + "( INSERT INTO " + table_name + " VALUES ('" + mass[0] + "','" + mass[1] + "','" + mass[2] + "','" + mass[3] + "'))"+ "INSERT INTO " + table_name2 + " VALUES ('" + mass[1] + "')"
        curso_r.execute(insert_command)
    elif(table_name=='success'):
        print("Enter 4 value >>> ")
        while(i<4):
            key=input()
            mass.append(key)
            i+=1
        table_name2='student'
        null_value='[null]'
        insert_command = "WITH " + table_name + " AS " + "( INSERT INTO " + table_name + " VALUES ('" + mass[0] + "','" + mass[1] + "','" + mass[2] + "','" + mass[3] + "'))"+ "INSERT INTO " + table_name2 + " VALUES ('" + null_value + "','" + mass[0] + "','" + null_value + "','" + null_value + "')"
        curso_r.execute(insert_command)

    elif(table_name=='class'):
        print("Enter 3 value >>>")
        while(i<3):
            key=input()
            mass.append(key)
            i+=1
        table_name2 = 'teacher'
        insert_command = "WITH " + table_name + " AS " + "( INSERT INTO " + table_name + " VALUES ('" + mass[0] + "','" + mass[1] + "','" + mass[2] + "'))"+ "INSERT INTO " + table_name2 + " VALUES ('" + mass[0] + "')"
        curso_r.execute(insert_command)
        
    else:
        while(i<2):
            key.input()
            mass.append(key)
            i+=1
        table_name2='class'
        insert_command=insert_command = "WITH " + table_name + " AS " + "( INSERT INTO " + table_name + " VALUES ('" + mass[0] + "','" + mass[1] + "'))"+ "INSERT INTO " + table_name2 + " VALUES ('" + mass[0] + "')"
        curso_r.execute(insert_command)
    curso_r.close()
	connec_t.close()


def delete(table_name):
	connec_t = psycopg2.connect(dbname='MyData' ,user='postgres',password='',host='localhost',port=5432)
	connec_t.set_session(autocommit=True)
	curso_r=connec_t.cursor()
    column=input('Enter column >>> ')
    column_info(table_name,column)
    row=input('Enter row >>> ')
    if(table_name=='student'):
        column_info('success','direction')
        dir_col=input("Enter direction column value >>> ")
        insert_command = "WITH student AS(DELETE FROM student WHERE " + column + " = '"+ row + "')DELETE FROM success WHERE direction = '"+ dir_col + "'"
        curso_r.execute(insert_command)
    elif(table_name=='success'):
        column_info('student','direction')
        dir_col=input("Enter direction column value >>> ")
        insert_command = "WITH success AS(DELETE FROM success WHERE " + column + " = '"+ row + "')DELETE FROM student WHERE direction = '"+ dir_col + "'"
        curso_r.execute(insert_command)
    elif(table_name=='teacher'):
        column_info('class','id_class')
        id_col=input("Enter id_class column value >>> ")
        insert_command = "WITH teacher AS(DELETE FROM teacher WHERE " + column + " = '"+ row + "')DELETE FROM class WHERE id_class = '"+ id_col + "'"
        curso_r.execute(insert_command)
    else:
        column_info('teacher','class_id')
        id_col=input("Enter class_id column value >>> ")
        insert_command = "WITH class AS(DELETE FROM class WHERE " + column + " = '"+ row + "')DELETE FROM teacher WHERE class_id = '"+ id_col + "'"
        curso_r.execute(insert_command)
    curso_r.close()
	connec_t.close()


def rand_row(table_name):
	connec_t = psycopg2.connect(dbname='MyData' ,user='postgres',password='',host='localhost',port=5432)
	connec_t.set_session(autocommit=True)
	curso_r=connec_t.cursor()
    count=input("Input random size >>> ")
    if(table_name=='student'):
        curso_r.execute(f"WITH test AS(INSERT INTO student SELECT chr(trunc(65+random()*30000)::int), chr(trunc(65 + random()*30000)::int),chr(trunc(65 + random()*30000)::int),chr(trunc(65 + random()*30000)::int) FROM generate_series(1,{count}) RETURNING direction)INSERT INTO success SELECT direction FROM test")
    elif(table_name=='success'):
        curso_r.execute(f"WITH test AS(INSERT INTO success SELECT chr(trunc(65+random()*30000)::int), (trunc(65 + random()*30000)::int),(trunc(65 + random()*30000)::int),chr(trunc(65 + random()*30000)::int) FROM generate_series(1,{count}) RETURNING direction)INSERT INTO student SELECT direction FROM test")
    elif(table_name=='teacher'):
        curso_r.execute(f"WITH test AS(INSERT INTO teacher SELECT chr(trunc(65+random()*30000)::int), (trunc(65 + random()*30000)::int) FROM generate_series(1,{count}) RETURNING class_id)INSERT INTO class SELECT id_class FROM test")
    else:
        curso_r.execute(f"WITH test AS(INSERT INTO class SELECT chr(trunc(65+random()*30000)::int), (trunc(65 + random()*30000)::int),(trunc(65 + random()*30000)::int) FROM generate_series(1,{count}) RETURNING id_class)INSERT INTO teacher SELECT class_id FROM test")
    curso_r.close()
	connec_t.close()

def search():
	connec_t = psycopg2.connect(dbname='MyData' ,user='postgres',password='',host='localhost',port=5432)
	connec_t.set_session(autocommit=True)
	curso_r=connec_t.cursor()
    n = input("Input quantity of attributes to search by >>> ")
    n = int(n)
    column=[]
    for h in range(0,n):
        column.append(str(input(f"Input name of the attribute number {h+1} to search by >>> ")))
    print(column)
    tables = []
    types = []
    if n == 2:
        curso_names_str = f"SELECT table_name FROM INFORMATION_SCHEMA.COLUMNS WHERE information_schema.columns.column_name LIKE '{column[0]}' INTERSECT ALL SELECT table_name FROM information_schema.columns WHERE information_schema.columns.column_name LIKE '{column[1]}'"
    else:
        curso_names_str = "SELECT table_name FROM INFORMATION_SCHEMA.COLUMNS WHERE information_schema.columns.column_name LIKE '{}'".format(column[0])
    print("\ncol_names_str:", curso_names_str)
    curso_r.execute(curso_names_str)
    curso_names = (curso_r.fetchall())
    for tup in curso_names:
        tables += [tup[0]]
    if 'student_teacher' in tables:
        tables.remove('student_teacher')
        print(tables)
    for s in range(0,len(column)):
        for k in range(0,len(tables)):
            curso_r.execute(f"SELECT data_type FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name='{tables[k]}' AND column_name ='{column[s]}'")
            type=(curso_r.fetchall())
            for j in type:
                types+=[j[0]]
    print(types)
    if n == 1:
        if len(tables) == 1:
            if types[0] == 'character varying':
                i_char = input(f"Input string for {column[0]} to search by >>> ")
                start_time=time.time()
                curso_r.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]} LIKE '{i_char}'")
                print(curso_r.fetchall())
                print("Time:%s seconds"%(time.time()-start_time))
            elif types[0] == 'integer':
                left_limits = input("Enter left limit")
                right_limits = input("Enter right limit")
                start_time=time.time()
                curso_r.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]}>='{left_limits}' AND {column[0]}<'{right_limits}'")
                print(curso_r.fetchall())
                print("Time:%s seconds"%(time.time()-start_time))
        elif len(tables) == 2:
            if types[0] == 'character varying':
                i_char = input(f"Input string for {column[0]} to search by >>> ")
                start_time = time.time()
                curso_r.execute(f"SELECT {column[0]} FROM {tables[0]} WHERE {column[0]} LIKE '{i_char}' UNION ALL SELECT {column[0]} FROM {tables[1]} WHERE {column[0]} LIKE '{i_char}'")
                print(curso_r.fetchall())
                print("Time:%s seconds" % (time.time() - start_time))
            elif types[0] == 'integer':
                left_limits = input("Enter left limit")
                right_limits = input("Enter right limit")
                start_time = time.time()
                curso_r.execute(f"SELECT {column[0]} FROM {tables[0]} WHERE {column[0]}>='{left_limits}' AND {column[0]}<'{right_limits}' UNION ALL SELECT {column[0]} FROM {tables[1]} WHERE {column[0]}>='{left_limits}' AND {column[0]}<'{right_limits}' ")
                print(curso_r.fetchall())
                print("Time:%s seconds" % (time.time() - start_time))

    elif n == 2:
        if len(tables) == 1:
            if types[0] == 'character varying' and types[1] == 'character varying':
                i_char = input(f"Input string for {column[0]} to search by >>> ")
                o_char = input(f"Input string for {column[1]} to search by >>> ")
                start_time = time.time()
                curso_r.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]} LIKE '{i_char}' AND {column[1]} LIKE '{o_char}' ")
                print(curso_r.fetchall())
                print("Time:%s seconds" % (time.time() - start_time))
            elif types[0] == 'character varying' and types[1] == 'integer':
                i_char = input(f"Input string for {column[0]} to search by >>> ")
                left_limits = input(f"Enter left limit for {column[1]}")
                right_limits = input(f"Enter right limit for {column[1]}")
                start_time = time.time()
                curso_r.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]} LIKE '{i_char}' AND {column[1]}>='{left_limits}' AND {column[1]}<'{right_limits}'")
                print(curso_r.fetchall())
                print("Time:%s seconds" % (time.time() - start_time))
            elif types[0] == 'integer' and types[1] == 'character varying':
                left_limits = input(f"Enter left limit for {column[0]}")
                right_limits = input(f"Enter right limit for {column[0]}")
                i_char = input(f"Input string for {column[1]} to search by >>> ")
                start_time = time.time()
                curso_r.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]}>='{left_limits}' AND {column[0]}<'{right_limits}' AND {column[1]} LIKE '{i_char}'")
                print(curso_r.fetchall())
                print("Time:%s seconds" % (time.time() - start_time))
            elif types[0] == 'integer' and types[1] == 'integer':
                i_left_limits = input(f"Enter left limit for {column[0]}")
                i_right_limits = input(f"Enter right limit for {column[0]}")
                o_left_limits = input(f"Enter left limit for {column[1]}")
                o_right_limits = input(f"Enter right limit for {column[1]}")
                start_time = time.time()
                curso_r.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]}>='{i_left_limits}' AND {column[0]}<'{i_right_limits}' AND {column[1]}>='{o_left_limits}' AND {column[1]}<'{o_right_limits}' ")
                print(curso_r.fetchall())
                print("Time:%s seconds" % (time.time() - start_time))
    curso_r.close()
	connec_t.close()


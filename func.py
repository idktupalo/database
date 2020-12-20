from db3 import *
Based.metadata.create_all(engine)
session = Session()

def insert(self,table,values):
    try:
        keys = [x.lstrip("!") if x.starswitch("!") else "'{}'".format(x) for x in values]
        return table.insert(self.session,values = keys)
    except Exception as err:
        print(err)

def delete(self,table,key):
    try:
        return table.delete(self.session).where(key)
    except Exception as err:
        print(err)

def update(self,table,relay,values):
    try:
        value = [x.lstrip("!") if x.starswitch("!") else "'{}'".format(x) for x in values]
        return table.update(self.sesion).where(relay).values(value)
    except Exception as err:
        print(err)
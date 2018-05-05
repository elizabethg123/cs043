import os

class Simpledb:
    def __init__(self, filename):
        self.filename = filename
    
    def __repr__(self):
        return ("<" + self.__class__.__name__ +
            " file='" + str(self.filename) +
            "'>")

    def insert(self, key, value):
        f = open(self.filename, 'a')
        f.write(key + '\t' + value + '\n')
        f.close()
    
    def select_one(self, key):
        f = open(self.filename, 'r')
        for row in f:
            (k, v) = row.split('\t', 1)
            if k == key:
                return v[:-1]
        f.close()

    def delete(self, key):
        f = open(self.filename, 'r')
        result = open('result.txt', 'w')
        for (row) in f:
            (k, v) = row.split('\t', 1)
            if k != key:
                result.write(row)
        f.close()
        result.close()
        os.replace('result.txt', self.filename)

    def modify(self, key, value):
        f = open(self.filename, 'r')
        open('result.txt', 'w')
        result = open('result.txt', 'w')
        for (row) in f:
            (k, v) = row.split('\t', 1)
            if k == key:
                    result.write(key + '\t' + value + '\n')
            else:
                    result.write(row)
        f.close()
        result.close()
        os.replace('result.txt', self.filename)


###class Tester:
   # db = Simpledb('recipes.txt')
   # db.insert('relish', 'Pickled cucumber and sugar')
   # db.insert('pesto', 'Basil and olive oil')
   # db.select_one('pesto')
  #  db.delete('pesto')
   # db.modify('relish', 'Pickled cucumber and sugar AND OREGANO')
   # print(db)


    


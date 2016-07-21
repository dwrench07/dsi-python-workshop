from collections import defaultdict

def test_function(*args):
    print args[1]
    for entry in args:
        print entry

class SparseMatrix(object):
    def __init__(self, n, m, default=0):
        self.n = n
        self.m = m
        self.mat = defaultdict(dict)
        self.default = default

    def __str__(self):
        mat = []
        for i in range(self.n):
            row = []
            for j in range(self.m):
                if i in self.mat:
                    row.append(str(self.mat[i].get(j,self.default)))
                else:
                    row.append(str(self.default))
            mat.append(row)
        return '\n'.join(['\t'.join(row) for row in mat])

    def __getitem__(self, x, y=None):
        if y is None:
            pass
            #implement this later
        else:
            return self.mat[x][y]

    def __setitem__(self, x, y):
        if len(x) == 2:
            self.mat[x[0]][x[1]] = y
        else:
            raise AttributeError


    def fill_from_lists(self,lists):
        pass

    def is_diagonal(self):
        # total = 0
        # for i in range(self.n):
        #     if i in self.mat:
        #         if i in self.mat[i]:
        #             total += self.mat[i][i]
        # return total == self.sum()
        tol = 1E-20
        # if self.n != self.m:
        #     return False
        for i in self.mat:
            for j in self.mat[i]:
                if i != j and abs(self.mat[i][j]) < tol:
                    return False
        return True

    def sum(self):
        total = 0
        for i in self.mat:
            for j in self.mat[i]:
               total += self.mat[i][j]
        return total


if __name__ == '__main__':
    # test = defaultdict(lambda: 5)
    # test['some key']
    # print test['some key']

    r'test'
    repr('test')

    mat = SparseMatrix(n=3,m=3)
    mat[1,2] = 1
    mat[2,1] = -1
    mat[1,1] = 3
    print mat.is_diagonal()
    print mat.sum()


import numpy as np

a = np.arange(6)
it = np.nditer(a , flags=['c_index'])
while not it.finished:
    print("%d <%d>" % (it[0], it.index)),
    it.iternext()
it.reset()
while not it.finished:
    print("%d <%d>" % (it[0], it.index)),
    it.iternext()
print('added this just for git test')
print('added this from ssrl for git test')
print("again with the test")

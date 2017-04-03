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

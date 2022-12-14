import matplotlib.pyplot as plt
import numpy as np
eng_no = [5,4]
lote_no = [2,3]
eng_yes = [5,5,4,5,5,5,5,5,4,5,4,4,5]
lote_yes = [2,3,2,1,1,2,3,2,3,4,3,2,4]

def rand_jitter(arr): # add some random jitter so multiple points are distinguishable
    stdev = .01 * (max(arr) - min(arr))
    return arr + np.random.randn(len(arr)) * stdev

def jitter(x, y, color=None, marker=None, label=None):
    ax.scatter(rand_jitter(x), rand_jitter(y), color=color, marker=marker, label=label)
    
fig=plt.figure()
ax=fig.add_subplot(111)
jitter(eng_no, lote_no, color='r', label="Subvocalization")
jitter(eng_yes, lote_yes, color='b', marker="v", label="No Subvocalization")
plt.legend(loc="upper left")
ax.set_xlabel('English reading comfort')
ax.set_ylabel('LOTE reading comfort')
ax.set_title('Subvocalization by English/LOTE reading comfort')
plt.show()

import numpy as np
import datetime as dt

def to_categorical(arr):
    s = set(arr)
    d = dict(zip(list(s), range(len(s))))
    rtn = list(map(d.get, arr))
    return np.array(rtn), d

def plot_labels(data, labels, xlim=None, ylim=None, save=None):
    import matplotlib.pyplot as plt
    [plt.plot(data[lab], label=lab) for lab in labels]
    plt.legend()
    if xlim:
        plt.xlim(*xlim)
    if ylim:
        plt.ylim(*ylim)
    if save:
        plt.savefig(save)
        plt.clf()
    return plt

class TimeCost:
    def __init__(self, msg='Time Cost', verbose=True):
        self.ts = None
        self.verbose = verbose
        self.msg = msg
    
    def __enter__(self):
        self.ts = dt.datetime.now()
    
    def __exit__(self, *args):
        self.ts = dt.datetime.now() - self.ts
        if self.verbose:
            print(f'{self.msg}: {self.ts.total_seconds()}')

if __name__ == "__main__":
    print(to_categorical([1, 2, 3, 2, 1]))
    print(to_categorical(['香草', '巧克力', '草莓', '巧克力', '香草']))

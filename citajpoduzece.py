import  pickle
from poduz import *


if __name__ == "__main__":
    with open("poduzece.dat", "rb") as file:
        pod = pickle.load(file)
        print(pod)
        for zap in pod:
            print(zap)

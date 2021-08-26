from itertools import permutations
import numba as nb
import numpy as np
import time


def calculateCombs():
  initTime = time.time()

  lists = [[1, 2, 3, 4, 5, 6, 7, 8], [3, 2, 1, 4, 5, 6, 8, 9],
          [8, 7, 6, 5, 4, 3, 2, 1], [2, 1, 1, 1, 1, 2, 2, 2],
          [8, 7, 5, 6, 3, 4, 2, 1]]

  #No se cuentan los digitos de referencia
  ciphers = [2, 3, 4, 5, 6, 7, 8]

  emptyArr = []

  permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])


  endTime = time.time()

  print(endTime)

  print("fin permutations 12 p con tiempo", endTime - initTime)

  return endTime

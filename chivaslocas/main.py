import numpy as np

def is_isolated(matrix):
  n,m = matrix.shape
  for i in range(n):
    for j in range(m):
      if matrix[i,j] == 1:
        for k in range(i):
          if matrix[k,j] == -1: break
          elif matrix[k,j] == 1: return False
        for k in range(i+1,n): 
          if matrix[k,j] == -1: break
          elif matrix[k,j] == 1: return False
        for k in range(j):
          if matrix[i,k] == -1: break
          elif matrix[i,k] == 1: return False
        for k in range(j+1,m):
          if matrix[i,k] == -1: break
          elif matrix[i,k] == 1: return False
  return True

def fill_diagonal (matrix, diagonals):
  for diagonal in diagonals:
    start = diagonal[:2]
    end = diagonal[2:]
    m = (start[1]-end[1])/(start[0]-end[0])
    if abs(m) != 1 : return np.ones(matrix.shape)
    matrix[start[0],start[1]] = -1
    matrix[end[0],end[1]] = -1
    if start[0] < end[0]:
        i_values = range(start[0]+1, end[0])
    else:
        i_values = range(start[0]-1, end[0], -1)
    for i in i_values:
      x = int(i)
      y = int(start[1] + m*(i-start[0]))
      matrix[x, y] = -1
  return matrix

def main() :
  matrix = np.array([
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0]])
  diagonals = np.array([
    [0,1,3,4],
    [0,3,3,0]])
  fill_diagonal(matrix, diagonals)
  print(is_isolated(matrix))

if __name__ == '__main__':
  main()

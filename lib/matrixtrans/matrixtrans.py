import numpy as np

def update_matrix(ground_ts, new_element):
  ground_ts = np.append(ground_ts[1:], new_element)
  return ground_ts

def extract_submatrices(matrix, k, m):
    n, d = matrix.shape
    submatrices = []
    for i in range(n-k+1):
        for j in range(d):
            submatrix = np.zeros((k, m))

            if(i==n-k and j>d-m):
              break

            for r in range(k):
                for c in range(m):
                  if(j + c < d):
                    row_idx = (i + r)
                    col_idx = (j + c)
                  elif(i+r<n-1):
                    row_idx = (i + r+1)
                    col_idx = (j + c) % d
                  submatrix[r, c] = matrix[row_idx, col_idx]

            submatrices.append(submatrix.flatten())

    return submatrices


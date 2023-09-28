from lib.matrixtrans.matrixtrans import *
from lib.distance.distance import * 
import numpy as np
import sys

def prediction(time_series, orig_r, orig_c, wind_r, wind_c):
  if(len(time_series)==1):
    return time_series[0]
  # Prepare and shape time series
  if(len(time_series)>orig_r*orig_c):
    time_series=time_series[-(orig_r*orig_c):]
  else:
    max_integer = sys.maxsize
    sparse =np.full((orig_r*orig_c)-len(time_series),max_integer)
    time_series= np.concatenate((sparse, time_series))

  time_series=update_matrix(time_series,0).reshape(orig_r, orig_c)
  
  # print(time_series)

  # Extract Submatrices
  submatrices = extract_submatrices(time_series, wind_r, wind_c)
  # print(submatrices)

  similarity_distances = {
    manhattan_distance: [],
    euclidean_distance: [],
    cosine_similarity:  [],
    fast_dtw: []
  }

  # Calculate the similarity between the main series (e.g the last submatrix) and other submatrix
  main_series=submatrices[-1]
  for submatrix in submatrices[:-1]:
     for key in similarity_distances:
      distance = key(main_series[:-1], submatrix[:-1])
      similarity_distances[key].append(distance)

  mst_similar = {
    "manhattan_distance": None,
    "euclidean_distance": None,
    "cosine_similarity":  None,
    "fast_dtw": None
  }

  for key in similarity_distances:
    if(key!=cosine_similarity):
      opt_dist =min(similarity_distances[key])
    else:
      opt_dist =max(similarity_distances[key])
    idx_of_mst_similar=similarity_distances[key].index(opt_dist)
    mst_similar[key.__name__]=submatrices[idx_of_mst_similar][-1]

    #Debug
  # print(similarity_distances)
  # print("the index is" ,idx_of_mst_similar)
  # print("the main array", main_series)
  # print("the mst simmiler array", mst_similar)
  # print("the forecast is ", mst_similar[-1])
  return mst_similar['fast_dtw']

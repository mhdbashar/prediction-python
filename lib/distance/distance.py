from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
import numpy as np


def manhattan_distance(point1, point2):
    return np.sum(np.abs(point1 - point2))

def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    if norm_vec1 == 0 or norm_vec2 == 0:
        # Handle the case where one of the vectors has zero magnitude
        similarity = 0.0  # or another appropriate value
    else:
        similarity = dot_product / (norm_vec1 * norm_vec2)
    return similarity

def euclidean_distance(vec1, vec2):
    return euclidean(vec1, vec2)
    
#DTW
# https://ealizadeh.com/blog/introduction-to-dynamic-time-warping/
# https://www.databricks.com/blog/2019/04/30/understanding-dynamic-time-warping.html
def fast_dtw(vec1, vec2):
    return fastdtw(vec1, vec2)[0]

import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import MDS
from sklearn.decomposition import PCA
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram

# helper method, factoring out the running of the MDS algorithm
def run_mds(data : np.ndarray):
    # assume that if it's not a square matrix, the extra row/column is for labels.
    # if it's imbalanced by more than 1, let the user know the shape of their data
    # doesn't fit.
    rows, cols = np.shape(data)
    if rows - cols == 1:
        labels = data[0].tolist()
        data = data[1:]
    elif cols - rows == 1:
        labels = data[:,0].tolist()
        data = data[:,1:]
    elif rows == cols:
        labels = []
    else:
        return False
    
    scaling = MDS(dissimilarity='precomputed', random_state=0)
    points = scaling.fit_transform(data)

    return points, labels

def mds(data : np.ndarray):
    points, labels = run_mds(data)

    plt.figure(0)
    plt.scatter(points[:,0], points[:,1])
    for i in range(len(labels)):
        plt.annotate(labels[i], points[i])
    
    plt.show()

def hc(data : np.ndarray):
    points, labels = run_mds(data)

    p_dist = pdist(points)

    plt.figure(1)
    dendrogram(linkage(squareform(p_dist)), labels=labels)
    plt.show()

# from homework 2
def biplot(data, pc_coeff, labels):
    plt.figure()
    xs = data[:,0]
    ys = data[:,1]
    n = pc_coeff.shape[1]
    xs = xs/(xs.max() - xs.min())
    ys = ys/(ys.max() - ys.min())
    plt.scatter(xs, ys )
    for i in range(n):
        print(labels[i], pc_coeff[0,i], pc_coeff[1,i])
        plt.arrow(0, 0, pc_coeff[0,i], pc_coeff[1,i], color = 'r', alpha = 0.7)
        plt.text(pc_coeff[0,i] + np.sign(pc_coeff[0,i]) * 0.02, pc_coeff[1,i] + np.sign(pc_coeff[1,i]) * 0.02, labels[i], color = 'g', ha = 'center', va = 'center')
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.title('Data projected into Eigenvector Space')
    plt.grid()
    plt.show()

def pca(data : np.ndarray):
    # assumes that the labels are the first row of data
    labels = data[0].tolist()
    data = data[1:]

    p = PCA()
    transformed_data = p.fit_transform(data)
    coefficients = p.components_
    evr = p.explained_variance_ratio_

    biplot(transformed_data, coefficients, labels)

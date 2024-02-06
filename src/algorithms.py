import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import MDS
from sklearn.decomposition import PCA
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram

# helper method, factoring out the running of the MDS algorithm
def run_mds(data : pd.DataFrame):

    labels = list(data.columns)
    data = data.to_numpy()

    # ensure that the data has the correct shape
    rows, cols = np.shape(data)
    if not rows == cols:
        print(data)
        raise ValueError
    
    scaling = MDS(dissimilarity='precomputed', random_state=0)
    points = scaling.fit_transform(data)

    return points, labels

def mds(data : pd.DataFrame):
    try:
        points, labels = run_mds(data)

        plt.figure(0)
        plt.scatter(points[:,0], points[:,1])
        for i in range(len(labels)):
            plt.annotate(labels[i], points[i])
    
        plt.show()
    except ValueError:
        print('Your data has an incompatible shape.')

def hc(data : pd.DataFrame):
    try:
        points, labels = run_mds(data)

        p_dist = pdist(points)

        plt.figure(1)
        dendrogram(linkage(squareform(p_dist)), labels=labels)
        plt.show()
    except ValueError:
        print('Your data has an incompatible shape.')

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
        plt.arrow(0, 0, pc_coeff[0,i], pc_coeff[1,i], color = 'r', alpha = 0.7)
        plt.text(pc_coeff[0,i] + np.sign(pc_coeff[0,i]) * 0.02, pc_coeff[1,i] + np.sign(pc_coeff[1,i]) * 0.02, labels[i], color = 'g', ha = 'center', va = 'center')
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.title('Data projected into Eigenvector Space')
    plt.grid()
    plt.show()

def pca(data : pd.DataFrame):
    # assumes that the labels are the first row of data
    labels = list(data.columns)
    data = data.to_numpy()

    p = PCA()
    transformed_data = p.fit_transform(data)
    coefficients = p.components_

    biplot(transformed_data, coefficients, labels)

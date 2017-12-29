# -- ALL TESTING --
import gensim
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import matplotlib.pyplot as plt

# Model Choice
model = gensim.models.Word2Vec.load('OOModel')
# model = gensim.models.KeyedVectors.load_word2vec_format('GoogleModel.bin', binary=True)
print(model["apple"])


def printEasy(forPrinting):
    toPrint = "["
    for i in forPrinting:
        toPrint += "`" + i[0] + "`, "
    print(toPrint[0:-2] + "]")


n = 500
# X = np.array([model['alien'], model['darkie'], model['nice'], model['mean'], model['happy'], model['sad']])
X = model.most_similar(positive=['nice', 'good', 'alien'], topn=n)
Y = model.most_similar(positive=['mean', 'bad', 'alien'], topn=n)

print(X)
print(Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xs, ys, index = [], [], []
for i in range(n):
    xs.append(X[i][1])
    ys.append(Y[i][1])
    index.append(i)
ax.plot(index, np.abs(np.subtract(xs, ys)), xs, 'r', label='Nice')
ax.plot(index, np.abs(np.subtract(xs, ys)), ys, 'b', label='Mean')

ax.legend()
ax.set_xlabel('Index')
ax.set_ylabel('Variation')
ax.set_zlabel('Amount')

plt.show()

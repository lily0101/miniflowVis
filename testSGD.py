"""
Have fun with the number of epochs!

Be warned that if you increase them too much,
the VM will time out :)
"""

import numpy as np
from sklearn.datasets import load_boston
from sklearn.utils import shuffle, resample
from miniFlow import *
import json

# Load data
data = load_boston()
X_ = data['data']
y_ = data['target']

# Normalize data
X_ = (X_ - np.mean(X_, axis=0)) / np.std(X_, axis=0)

n_features = X_.shape[1]
n_hidden = 10
W1_ = np.random.randn(n_features, n_hidden)
b1_ = np.zeros(n_hidden)
W2_ = np.random.randn(n_hidden, 1)
b2_ = np.zeros(1)

# Neural network
X, y = Input(), Input()
W1, b1 = Input(), Input()
W2, b2 = Input(), Input()
X.id = "X";
y.id = "y";
W1.id = "W1";
W2.id = "W2";
b1.id = "b1";
b2.id = "b2";
l1 = Linear(X, W1, b1)
s1 = Sigmoid(l1)
l2 = Linear(s1, W2, b2)
cost = MSE(y, l2)
l1.id = "L1";
s1.id = "S1";
l2.id = "L2";
cost.id = "MSE";

feed_dict = {
    X: X_,
    y: y_,
    W1: W1_,
    b1: b1_,
    W2: W2_,
    b2: b2_
}

epochs = 100
# Total number of examples
m = X_.shape[0]
batch_size = 10
steps_per_epoch = m // batch_size

graph = topological_sort(feed_dict)
#print(graph)
trainables = [W1, b1, W2, b2]
#X,y  non-broadcastable output operand with shape (10,) doesn't match the broadcast shape (10,10)
test = [X,W1,b1,l1,s1,W2,b2,l2,y,cost]
result = [];
print("Total number of examples = {}".format(m))
#序列化对象
class DateEncoder(json.JSONEncoder ):  
    def default(self, obj):  
        if isinstance(obj, Node): #or isinstance(obj,ndarray):  
            return obj.__str__()  
        return json.JSONEncoder.default(self, obj)  
# Step 4
for i in range(epochs):
    loss = 0
    for j in range(steps_per_epoch):
        # Step 1
        # Randomly sample a batch of examples
        X_batch, y_batch = resample(X_, y_, n_samples=batch_size)

        # Reset value of X and y Inputs
        X.value = X_batch
        y.value = y_batch

        # Step 2
        forward_and_backward(graph)
       
        # Step 3
        sgd_update(trainables)
        #json
        for i in range(len(test)):
            result.append({"id":test[i].id,"inNode":test[i].inbound_nodes,
                           "outNodes":test[i].outbound_nodes,"gradients":str(test[i].gradients),"value":test[i].value})
            print("gradients:!!!!!!!!!!!!!!!!!!!!!!!!!!",test[i].gradients)
           # result.append({"id":test[i].id,"gradient": test[i].gradients[test[i]].tolist(),"value":test[i].value.tolist()});
        
        #print("result!!!!!!!!!!!!!!!!!!!",result);
        with open("F:/graduateStudy/lab/drawing robot/miniflow/vis/cytoscape/record.json","w") as f:
            json.dump(list(result),f,cls=DateEncoder)
            print("加载入文件完成...")
        del result[:];
        
        loss += graph[-1].value

    print("Epoch: {}, Loss: {:.3f}".format(i+1, loss/steps_per_epoch))
# Stochastic-Gradient-Descent

1. 關鍵超參數 : regularization （正則化）、learning rate、 number of iterations （迭代次數）

2. SGDRegressor 非常適用於有大量訓練樣本（>10.000)的迴歸問題

3. minibatch : 一次取多個樣本點去 build regression model

  * ex : model.partial_fit(X,y)

4. loss function

  * loss=”hinge”: (soft-margin) linear Support Vector Machine （（軟-間隔）線性支持向量機）
  * loss=”log”: logistic regression （logistic 迴歸）
  * loss=”modified_huber”: smoothed hinge loss （平滑的 hinge 損失）

5. 使用訓練數據的方式分為以下三種 (partial_fit函數)：

  * 批量梯度下降法（Batch gradient descent, BGD）

  每次迭代使用「所有」的樣本，這樣做的好處是每次迭代都顧及了全部的樣本，考慮的是全局最優化。需要注意的是這個名字並不確切，但是機器學習領域中都這樣稱。它的缺點是每次迭代都要計算訓練集中所有樣本的訓練誤差，當數據量很大時，這種方法效率不高

  * 隨機梯度下降法（Stochastic gradient descent, SGD）

  每次迭代都隨機從訓練集中抽取出「1個」樣本，在樣本量極其大的情況下，可能不用抽取出所有樣本，就可以獲得一個損失值在可接受範圍之內的模型了。缺點是由於單個樣本可能會帶來噪聲，導致並不是每次迭代都向著整體最優方向前進  

  * 小批量梯度下降法（Mini-Batch gradient descent, MBGD）

  它介於批量梯度下降法與隨機梯度下降法之間。每次迭代隨機從訓練集抽取「一定數量」的數據進行訓練

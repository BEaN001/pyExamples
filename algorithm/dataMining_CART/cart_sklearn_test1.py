#! /usr/bin/env python
#-*- coding:utf-8 -*-

from sklearn import tree
import numpy as np

# scikit-learnʹ�õľ������㷨��CART

X = [[0,0],[1,1]]
Y = ["A","B"]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

data1 = np.array([2.,2.]).reshape(1,-1)
print clf.predict(data1) # Ԥ�����  
print clf.predict_proba(data1) # Ԥ�����ڸ�����ĸ���


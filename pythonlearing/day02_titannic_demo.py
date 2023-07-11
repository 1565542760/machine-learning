import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier,export_graphviz
#1、获取数据
titanic=pd.read_csv("D:/常用/医学人工智能/机器学习/机器学xiday2资料/02-代码/titanic.csv")
#筛选特征值与目标值
x=titanic[["pclass","age","sex"]]
y=titanic["survived"]
#2、数据处理
#1）缺失值处理
# x["age"]=x["age"].fillna(x["age"].mean(),inplace=True)
x["age"].fillna(x["age"].mean(),inplace=True)
#2、转换成字典
x=x.to_dict(orient="records")
#3、数据集划分
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=22)
#4、字典特征抽取
transfer=DictVectorizer()
x_train=transfer.fit_transform(x_train)
x_test=transfer.transform(x_test)
#3)决策树预估器
estimator=DecisionTreeClassifier(criterion='entropy',max_depth=8)
estimator.fit(x_train,y_train)
#4)模型评估
y_predict = estimator.predict(x_test)
print("y_predict:\n", y_predict)
print("直接比对真实值和预测值：\n", y_test == y_predict)
# 2）方法二：计算准确率
score = estimator.score(x_test, y_test)
print("准确率为:\n", score)
#plot_tree(estimator,feature_names=iris.feature_names)

#可视化决策树
export_graphviz(estimator,out_file="titanic_tree.dot",feature_names=transfer.get_feature_names_out())
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
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
#随机森林对泰坦尼克号乘客的生存进行预测
#实例化
estimator=RandomForestClassifier()
#加入网格搜索与交叉验证
#参数准备
param_dict ={"n_estimators":[120,200,300,500,800,1200],"max_depth":[5,8,15,25,30]}
estimator=GridSearchCV(estimator,param_grid=param_dict,cv=3)

estimator.fit(x_train,y_train)
# 5、模型评估
#1）方法一：直接比较真实值和预测值
y_predict = estimator.predict(x_test)
print("y_predict:\n",y_predict)
print("直接比对真实值和预测值：\n",y_test==y_predict)
#2）方法二：计算准确率
score=estimator.score(x_test,y_test)
print("准确率为:\n",score)

# 最佳参数: best_params_
print("最佳参数:\n",estimator.best_params_)
# 最佳结果: best_score_
print("最佳结果:\n", estimator.best_score_)
# 最佳估计器: best_estimator_
print("最佳估计器:\n", estimator.best_estimator_)
# 交叉验证结果: cv_results_
print("交叉验证结果:\n", estimator.cv_results_)
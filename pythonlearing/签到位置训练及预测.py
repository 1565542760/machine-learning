import pandas as pd
#1、获取数据
data=pd.read_csv("D:/常用/医学人工智能/机器学习/机器学xiday2资料/02-代码/FBlocation/train.csv")
#2、数据处理_特征值X_目标值Y
#缩小数据
data.head()
#1)x[2.5,2] y[1.0,1.5]
data=data.query("x<2.5&x>2&y<1.5&y>1.0")
#2)time->年月日时分秒
time_value=pd.to_datetime(data["time"],unit="s")
date=pd.DatetimeIndex(time_value)
data["day"]=date.day
data["weekday"]=date.weekday
data["hour"]=date.hour
#3)过滤签到次数较少的地点
place_count=data.groupby("place_id").count()["row_id"]
place_count[place_count>3].head()
data_final= data[data["place_id"].isin(place_count[place_count > 3].index.values)]
data_final.head()
#筛选特征值及目标值
x=data_final[["x","y","accuracy","day","weekday","hour"]]
y=data_final["place_id"]
#数据集划分
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
x_train, x_test, y_train, y_test=train_test_split(x,y)
# 3、特征工程：标准化
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test=transfer.transform(x_test)
# 4、KNN预估器流程
estimer=KNeighborsClassifier()

#加入网格搜索与交叉验证
#参数准备
param_dict ={"n_neighbors":[3,5,7,9]}
estimer=GridSearchCV(estimer,param_grid=param_dict,cv=3)

estimer.fit(x_train,y_train)
# 5、模型评估
#1）方法一：直接比较真实值和预测值
y_predict = estimer.predict(x_test)
print("y_predict:\n",y_predict)
print("直接比对真实值和预测值：\n",y_test==y_predict)
#2）方法二：计算准确率
score=estimer.score(x_test,y_test)
print("准确率为:\n",score)

# 最佳参数: best_params_
print("最佳参数:\n",estimer.best_params_)
# 最佳结果: best_score_
print("最佳结果:\n", estimer.best_score_)
# 最佳估计器: best_estimator_
print("最佳估计器:\n", estimer.best_estimator_)
# 交叉验证结果: cv_results_
print("交叉验证结果:\n", estimer.cv_results_)


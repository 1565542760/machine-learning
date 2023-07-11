from sklearn.datasets import load_iris
#实例化一个转换器类
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import jieba
import pandas as pd
def datasets_demo():
    """
    sklearn数据集使用
    :return:
    """
    #获取数据集
    iris=load_iris()
    print("鸢尾花数据集:\n",iris)
    print("查看数据集描述:\n",iris["DESCR"])
    print("查看特征值的名字:\n",iris.feature_names)
    print("查看特征值:\n",iris.data,iris.data.shape)

    #数据集划分
    x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.2)
    print("训练集的特征值:\n",x_train,x_train.shape)
    print("测试集的特征值:\n",x_test,x_test.shape)
    print("训练集的目标值:\n",y_train,y_train.shape)
    print("测试集的目标值:\n",y_test,y_test.shape)

    return None

def dict_demo():
    """
    字典特征提取
    :return:
    """
    data=[{'city':'北京','temperature':100},{'city': '上海', 'temperature':60},{'city':'深圳','temperature':30}]
    #1、实例化一个转换器类
    transfer=DictVectorizer(sparse=False)
    #2、调用fit_transform(传入字典或者字典的迭代器)方法
    data_new=transfer.fit_transform(data)
    print("data_new:\n",data_new)
    print("特征名\n",transfer.get_feature_names_out())
    return None


def count_demo():
    '''
    文本特征抽取：CountVectorizer
    :return:
    '''
    data=["life is short,i like like python","life is too long,i dislike python"]
    #1、实例化一个转换器类
    transfer = CountVectorizer()
    #2、调用fit_transform
    datanew=transfer.fit_transform(data)
    print("datanew:\n",datanew.toarray())
    print("特征名\n", transfer.get_feature_names_out())
    return None

def count_Chinesedemo():
    '''
    中文文本特征抽取：CountVecotrizer
    :return:
    '''
    data=["我 爱 北京 天安门","天安门 上 太阳 升"]#用分词工具
    #1、实例化一个转换器类
    transfer = CountVectorizer()
    #2、调用fit_transform
    datanew=transfer.fit_transform(data)
    print("datanew:\n",datanew.toarray())
    print("特征名\n", transfer.get_feature_names_out())
    return None
def cut_word(text):
    '''
    进行中文分词
    :param text:
    :return:
    '''
    text=" ".join(list(jieba.cut(text)))
    return text

def text_chinese_count_demo2():
    '''
    中文文本特征抽取：CountVecotrizer
    :return:
    '''
    #将中文文本进行分词
    data=["今天早上我的牙疼了一早上，"
          "妈妈给我想了好多办法都不行，"
          "先是用酒和棉球不行，后来又用花椒还是不行，"
          "妈妈就带我动去小白洋去看医生，医生说是牙龈发炎了，"
          "医生给我开了点药说没事的，吃点药就会好点。我和妈妈回家了，"
          "妈妈给我倒水让我吃药，我对妈妈说谢谢"]#用分词工具
    data_new=[]
    for sent in data:
        data_new.append(cut_word(sent))
    print(data_new)
    #1、实例化一个转换器类
    transfer = CountVectorizer()
    #2、调用fit_transform
    data_final=transfer.fit_transform(data_new)
    print("datanew:\n",data_final.toarray())
    print("特征名:\n", transfer.get_feature_names_out())
    return None

def tfidf_demo():
    '''
    用TF-IDF的方法进行文本特征抽取
    :return:
    '''
    data = ["今天早上我的牙疼了一早上，"
            "妈妈给我想了好多办法都不行，"
            "先是用酒和棉球不行，后来又用花椒还是不行，"
            "妈妈就带我动去小白洋去看医生，医生说是牙龈发炎了，"
            "医生给我开了点药说没事的，吃点药就会好点。我和妈妈回家了，"
            "妈妈给我倒水让我吃药，我对妈妈说谢谢"]  # 用分词工具
    data_new = []
    for sent in data:
        data_new.append(cut_word(sent))
    print(data_new)
    # 1、实例化一个转换器类
    transfer = TfidfVectorizer()
    # 2、调用fit_transform
    data_final = transfer.fit_transform(data_new)
    print("datanew:\n", data_final.toarray())
    print("特征名:\n", transfer.get_feature_names_out())
    return None

def minmax_damo():
    '''
    归一化
    :return:
    '''
    #1、获取数据
    data=pd.read_csv("dating.txt")
    print("data:\n",data)
    data=data.iloc[:,:3]
    print("data:\n", data)
    #2、实例化一个转换器类
    transfer=MinMaxScaler()

    #3、调用fit_transform进行转化
    data_new=transfer.fit_transform(data)
    print("data_new:\n",data_new)
    return None

def stand_demo():
    '''
    标准化
    :return:
    '''
    # 1、获取数据
    data = pd.read_csv("dating.txt")
    print("data:\n", data)
    data = data.iloc[:, :3]
    print("data:\n", data)
    # 2、实例化一个转换器类
    transfer = StandardScaler()

    # 3、调用fit_transform进行转化
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new)
    return None

def variance_demo():
    '''
    低方差特征过滤
    :return:
    '''
    #1、获取数据
    data=pd.read_csv("factor_returns.csv")
    # print(data)
    data=data.iloc[:,1:-2]
    print(data)
    #2、实例化一个转换器类
    transfer=VarianceThreshold(threshold=5)
    #3、调用fit_transform
    data_new=transfer.fit_transform(data)
    print(data_new,data_new.shape)
    #4、计算某两个变量之间的相关系数
    r1=pearsonr(data["pe_ratio"],data["pb_ratio"])
    print("相关系数1：",r1)
    r2=pearsonr(data['revenue'],data['total_expense'])
    print("相关系数2：",r2)
    plt.figure(figsize=(20,0),dpi=100)
    plt.scatter(data['revenue'],data['total_expense'])
    plt.show()
    return None

def pca_demo():
    '''
    pca降维
    :return:
    '''
    data=[[2,8,4,5],[6,3,0,8],[5,4,9,1]]
    #1、实例化一个转换器类
    transfer=PCA(n_components=2)
    #2、调用fit_transform
    data_new=transfer.fit_transform(data)
    print(data_new)
    return None

#1、获取数据
aisles=pd.read_csv("D:/常用/医学人工智能/机器学习/机器学xiday1资料/02-代码/instacart/aisles.csv")
order_products=pd.read_csv("D:/常用/医学人工智能/机器学习/机器学xiday1资料/02-代码/instacart/order_products__prior.csv")
orders=pd.read_csv("D:/常用/医学人工智能/机器学习/机器学xiday1资料/02-代码/instacart/orders.csv")
products=pd.read_csv("D:/常用/医学人工智能/机器学习/机器学xiday1资料/02-代码/instacart/products.csv")
#2、合并表
#合并aislses与products
table1=pd.merge(aisles,products,on=["aisle_id","aisle_id"])
table2=pd.merge(table1,order_products,on=["product_id","product_id"])
table3=pd.merge(table2,orders,on=["order_id","order_id"])
table3.head()
#3、找到user_id,aisle之间的关系
table=pd.crosstab(table3["user_id"],table3["aisle"])
#4、PCA降维
transfer=PCA(n_components=0.95)
data_new=transfer.fit_transform(table)

if __name__=="__main__":
    #代码1：sklearn数据集使用
    # datasets_demo()
    #代码2：字典特征提取
    # dict_demo()
    #代码3：文本特征抽取：CountVecotrizer
    # count_demo()
    # 代码4：中文文本特征抽取：CountVecotrizer
    # count_Chinesedemo()
    #代码5：中文分词
    # print(cut_word("我爱北京天安门"))
    #代码6：自动分词
    text_chinese_count_demo2()
    #代码7：用TF-IDF的方法进行文本特征抽取
    # tfidf_demo()
    #代码8：归一化
    # minmax_damo()
    #代码9、标准化
    # stand_demo()
    #代码10、低方差特征过滤
    # variance_demo()
    #代码11、PCA降维
    # pca_demo()
    #代码12、PCA降维实例
    # print(data_new)
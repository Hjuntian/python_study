# data 这个属性可能是 NumPy ndarray 或 pandas DataFrame，取决于你怎么加载数据或 sklearn 版本
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()

type(iris.data)  
# <class 'numpy.ndarray'>  -> 默认 ndarray

# 转成 DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)
type(df)
# <class 'pandas.core.frame.DataFrame'>



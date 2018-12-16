
import numpy as np

def createDataSetForPerson():
    dataSet = [
        # 1
        [1, '正常', '偏白', '男'],
        # 2
        [1, '较大', '偏黑', '男'],
        # 3
        [1, '正常', '偏黑', '男'],
        # 4
        [1, '较大', '偏黑', '女'],
        # 5
        [0, '正常', '偏白', '女'],
        # 6
        [0, '较大', '偏白', '女'],
    ]
    # 特征值列表
    labels = ['身高', '眼睛大小', '肤色']
    dataSet = np.array(dataSet)
    # 得到分类结果
    classify = dataSet[:, -1]
    # 去除分类之后的数据集
    dataSet = dataSet[:, :-1]
    return dataSet, classify, labels
def train_feature_value(dataSet, classify, feature_index, value):
    # 用来保存每个分类的个数
    class_counts = defaultdict(int)

    # 遍历所有的样本数据和对应的标签
    for sample, label in zip(dataSet, classify):
        # 如果当前样本的指定特征等于目标特征值的话
        if sample[feature_index] == value:
            # 对应的特征值个数加一
            class_counts[label] += 1

    # 根据分类的值排序，从大到小
    sorted_class_sounts = sorted(class_counts.items(), key=operator.itemgetter(1), reverse=True)

    # 找到对多的分类，也就是我们的目标分类
    most_class = sorted_class_sounts[0][0]

    # 在分类结果中找到分类不等于目标分类的
    incorrect_predictions = [class_count for class_value, class_count in class_counts.items()
                             if class_value != most_class]
    # 计算出错误个数
    error = sum(incorrect_predictions)

    return most_class, error


if __name__=='__main__':
   dataSet,classify,labels=createDataSetForPerson()
   print(dataSet)
   print(classify)
   print(labels)
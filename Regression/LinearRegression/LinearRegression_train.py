import numpy as np

def load_data(file_path):
    '''
        导入数据
    :param file_path: 训练数据
    :return: feature:特征
            label:标签
    '''
    f = open(file_path)
    feature = []
    label = []
    for line in f.readlines():
        feature_temp = []
        lines = line.strip().split("\t")
        feature_temp.append(1)
        for i in range(len(lines)-1):
            feature_temp.append(float(lines[i]))
        feature.append(feature_temp)
        label.append(float(lines[-1]))
    f.close()
    return np.mat(feature),np.mat(label).T

def least_square(feature,label):
    '''
        最小二乘法
    :param feature: 特征
    :param label: 标签
    :return: w(mat)回归系数
    '''

    w = (feature.T*feature).I*feature.T*label
    return w


def save_model(file_name,w):
    '''
        保存最终的模型
    :param file_name: 文件名
    :param w: 训练好的线性回归模型
    :return:
    '''
    f_resuult = open(file_name,"w")
    m,n = np.shape(w)
    for i in range(m):
        w_temp = []
        for j in range(n):
            w_temp.append(str(w[i,j]))
        f_resuult.write('\t'.join(w_temp)+'\n')
    f_resuult.close()




if __name__=='__main__':
    # 1,导入数据集
    print('-------- 1,load data -------')
    feature,label = load_data("data.txt")

    # 2.1，最小二乘法求解
    print('------ 2.training ---------')
    w_ls = least_square(feature, label)
    # 2.2，牛顿法
    # 3，保存最纵结果
    print('--------- 3.save result -------')
    save_model('weights',w_ls)


import numpy as np
from sklearn.preprocessing import minmax_scale


def AcceptableInterval(x, y, card, head_x, head_y, method='mean'):

    value_x = None
    value_y = None

    if method == 'mean':
        value_x = x.mean()
        value_y = y.mean()
    else:
        value_x = np.median(x)
        value_y = np.median(y)

    R = x / value_x - y / value_y

    argsort = R.argsort()
    print(head_x, '\t', end='')
    for item in argsort:
        print(x[item], end='\t')
    print()
    print(head_y, '\t', end='')
    for item in argsort:
        print(y[item], end='\t')
    print()
    print('Card No.', '\t', end='')
    """for item in argsort:
        print(card[item], end='\t')"""

    print(card[argsort[0]], card[argsort[-1]])
    print(R.min(), R.max())

    print()

def AcceptableInterval1(x, y, method='mean'):

    value_x = None
    value_y = None

    if method == 'mean':
        value_x = x.mean()
        value_y = y.mean()
    else:
        value_x = np.median(x)
        value_y = np.median(y)

    R = x / value_x - y / value_y

    return R, value_x, value_y

def main():
    colums = [0, 2, 4, 6, 7, 8, 11]
    headers = ['age', 'creatinine_phosphokinase', 'ejection_fraction', 'platelets',
               'serum_creatinine', 'serum_sodium', 'time']

    colums = [0, 2, 4, 6, 7, 8]
    headers = ['age', 'creatinine_phosphokinase', 'ejection_fraction', 'platelets',
               'serum_creatinine', 'serum_sodium']

    data = np.loadtxt('D:/data.txt')

    card = []
    [card.append(i + 1) for i in range(data.shape[0])]

    X = data[:, colums]

    _X = X.copy()

    minmax_scale(X, copy=False)

    for i in range(X.shape[1]):
        for j in range(i + 1, X.shape[1]):
            print('(', headers[i], ', ', headers[j], ')', sep='')
            AcceptableInterval(X[:, i], X[:, j], card, headers[i], headers[j], method='median')

def main1():

    colums = [0, 2, 4, 6, 7, 8, 11]
    headers = ['age', 'creatinine_phosphokinase', 'ejection_fraction', 'platelets',
               'serum_creatinine', 'serum_sodium', 'time']

    colums = [0, 2, 4, 6, 7, 8]
    headers = ['age', 'creatinine_phosphokinase', 'ejection_fraction', 'platelets',
               'serum_creatinine', 'serum_sodium']

    data = np.loadtxt('D:/data.txt')

    card = []
    [card.append(i + 1) for i in range(data.shape[0])]

    X = data[:, colums]

    _X = X.copy()

    minmax_scale(X, copy=False)
    #print(X)

    #result = np.empty(shape=(X.shape[1], X.shape[1]))
    percentage = 0

    query_temp_str = "{2}={0} bo'lganda, {3}={1} bo'lishi qanchalik o'rinli"

    indexing = np.arange(0, X.shape[0])
    print('Results for {0}%'.format(percentage))
    ss = set()
    s = 0
    for i in range(X.shape[0]):
        print('Карта №: ', card[i], sep='')
        k = 0
        for j in range(X.shape[1]):
            for l in range(j + 1, X.shape[1]):
                cond = indexing != i
                R, value_x, value_y = AcceptableInterval1(X[cond, j], X[cond, l], method='ss')
                q_left = np.percentile(R, percentage)
                q_right = np.percentile(R, 100 - percentage)

                test_value = X[i, j] / value_x - X[i, l] / value_y

                if (test_value < q_left or q_right < test_value):
                    query = query_temp_str.format(_X[i, j], _X[i, l], headers[j], headers[l])
                    print('(', headers[j], ', ', headers[l], ')', "\t" + query, sep='')
                    k += 1
                    ss.add(i)
        s += k
        """if k != 0:
            print("Количество пары: ", k, sep='')
        else:
            print("Нет пары")"""
    available = X.shape[1] * (X.shape[1] - 1) / 2
    print('Available number of pairs: ', available, sep='')
    print('Mean number of pairs: ', s / X.shape[0], sep='')

    print('Number of objects have pair: {0}'.format(len(ss)))

if __name__ == '__main__':
    main()
    #main1()
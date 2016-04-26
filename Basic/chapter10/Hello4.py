__author__ = 'hzliyong'
import sys, pprint

def hello():
    print("Hello, world!")


def test():
    hello()

if __name__ == '__main__':
    test()

pprint.pprint(sys.path)
# skuId=float(90.00)
skuId=323
print('dd%s' % skuId)

commonList = []
commonList.append('asd')
commonList.append('dsfsdf')
print('commonList----------', commonList)
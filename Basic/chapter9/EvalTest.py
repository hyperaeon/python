__author__ = 'hzliyong'


line = '{"accountId":"","action":"page","brandIds":" ","browser":"Firefox 3","category":" ","clientType":"web","cookie":"_da_ntes_uid=efWo56QW3dCVEDDjI1PSw2Tp;","deviceOs":"Linux","deviceType":"Computer","fromPos":"","ids":"5549726,5558111,5558115,5558148,5558188,5558232,5558250,5558283,5558313,5558328,","ip":"210.51.177.137","keyword":"puujapuu","provinceCode":"11","robot":"0","searchType":"input","success":"true","time":"1449339375389","totalHit":97,"type":"searchPage","typeName":"\xe6\x90\x9c\xe7\xb4\xa2\xe9\xa1\xb5\xe9\x9d\xa2"}\n'
record = eval(line)
print(record.get('success'))

sku_id_sale_money_map = {}
skuId = '7019174'
sku_id_sale_money_map[skuId]['web'] = 0
origin = float(sku_id_sale_money_map[skuId]['web'])
saleMoney = 0
sku_id_sale_money_map[skuId]['web'] = origin + saleMoney
print(sku_id_sale_money_map[skuId]['web'])


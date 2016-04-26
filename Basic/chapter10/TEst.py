__author__ = 'hzliyong'

prd_total_pv_web_map = {}
prd_total_pv_wap_map = {}
prd_total_pv_app_map = {}
prd_total_pv_app_chl_map = {}
prd_total_uv_web_map = {}
prd_total_uv_wap_map = {}
prd_total_uv_app_map = {}
prd_total_uv_app_chl_map = {}

prdId = 222
chl_list = ['web', 'app']


def check_init_type_map(id, map):
    if id not in map:
        map[id] = {}
        map[id]['web'] = 0
        map[id]['wap'] = 0
        for chll in chl_list:
            map[id][chll] = 0
        map[id]['other'] = 0

if prdId not in prd_total_pv_web_map:
    prd_total_pv_web_map[prdId] = [prdId, 0]
print(str(prd_total_pv_web_map[prdId][1]))

if prdId not in prd_total_pv_wap_map:
    prd_total_pv_wap_map[prdId] = [prdId, 0]
print(str(prd_total_pv_wap_map[prdId][1]))

if prdId not in prd_total_pv_app_map:
    prd_total_pv_app_map[prdId] = [prdId, 0]
print(str(prd_total_pv_app_map[prdId]))

if prdId not in prd_total_pv_app_chl_map:
    check_init_type_map(prdId, prd_total_pv_app_chl_map)
appChl = 'web'
print(str(prd_total_pv_app_chl_map[prdId][appChl]))

if prdId not in prd_total_uv_web_map:
    prd_total_uv_web_map[prdId] = [prdId, 0]
print(str(prd_total_uv_web_map[prdId][1]))

if prdId not in prd_total_uv_wap_map:
    prd_total_uv_wap_map[prdId] = [prdId, 0]
print(str(prd_total_uv_wap_map[prdId][1]))

if prdId not in prd_total_uv_app_map:
    prd_total_uv_app_map[prdId] = 0
print(str(prd_total_uv_app_map[prdId]))

if prdId not in prd_total_uv_app_chl_map:
    check_init_type_map(prdId, prd_total_uv_app_chl_map)
print(str(prd_total_uv_app_chl_map[prdId][appChl]))



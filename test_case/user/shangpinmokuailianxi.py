import random

import allure
import requests

from config.conf import API_URL
from tools.api import request_tool

'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''
# #创建商品
# def test_addProd(pub_data):
#     pub_data["productCode"] = "自动生成 字符串 5 数字字母"
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '创建商品'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/addProd"  # 接口地址
#     headers = {"token": pub_data["token"]}
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     json_data='''{
#   "brand": "耐克",
#   "colors": [
#     "黑色",
#     "蓝色"
#   ],
#   "price": 9999,
#   "productCode": "${productCode}",
#   "productName": "air force",
#   "sizes": [
#     "43",
#     "42"
#   ],
#   "type": "鞋子"
# }'''
#
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)
#
#
# #根据产品编码查商品
# def test_getSkuByProdCode(pub_data):
#     method = "GET"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '查询商品'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/getSkuByProdCode"  # 接口地址
#     headers = {"token": pub_data["token"]}
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     params={'prodCode': "${productCode}"}
#
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)
# #修改商品价格
# def test_changePrice(pub_data):
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '修改商品价格'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/changePrice"  # 接口地址
#     headers = {"token": pub_data["token"]}
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     data={'SKU': 'K9tGr_黑色_43', 'price': '8888'}
#
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)
# #查询单个商品验证
# def test_getSKU(pub_data):
#     method = "GET"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '单个商品验证'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/getSKU"  # 接口地址
#     headers = {"token": pub_data["token"]}
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     params={'SKU': 'K9tGr_黑色_43'}
#
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)
# #修改产品价格
# def test_changePriceByProdCode(pub_data):
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '修改产品价格'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/changePriceByProdCode"  # 接口地址
#     headers = {"token": pub_data["token"]}
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     data={'price': '6666', 'prodCode': 'K9tGr'}
#
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)
# #根据产品编码查看修改结果
# def test_getSkuByProdCode1(pub_data):
#     method = "GET"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '查询商品'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/getSkuByProdCode"  # 接口地址
#     headers = {"token": pub_data["token"]}
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     params={'prodCode': "K9tGr"}
#
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)
#  #下架
# def test_soldOut(pub_data):
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '下架'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/soldOut"  # 接口地址
#     headers = {"token": pub_data["token"]}
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     data={'productCode': 'K9tGr'}
#
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)
# #预售
# def test_toPreSale(pub_data):
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '预售'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/toPreSale"  # 接口地址
#     headers = {"token": pub_data["token"]}
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     data={'productCode': 'K9tGr'}
#
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)
# #全量调整单个商品库存
# def test_fullSku(pub_data):
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '全量调整单个商品库存'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/fullSku"  # 接口地址
#     headers = {"token": pub_data["token"]}
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     data={'qty': '999', 'skuCode': 'K9tGr_黑色_43'}
#
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)
# #增量调整单个商品库存
# def test_incrementSku(pub_data):
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '增量调整单个商品库存'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/incrementSku"  # 接口地址
#     headers = {"token": pub_data["token"]}
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     data={'qty': '888', 'skuCode': 'K9tGr_黑色_43'}
#
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)
# #查询单个库存
# def test_getSkuRepertory(pub_data):
#     method = "GET"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '查询单个库存'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/getSkuRepertory"  # 接口地址
#     headers = {"token": pub_data["token"]}
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     params={'skuCode': 'K9tGr_黑色_43'}
#
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)


@allure.feature("用户管理")#一级分类
@allure.story("充值提现模块")#二级分类
@allure.title("充值")#修改用例标题
def test_recharge2(db):
    #执行查询SQL语句
    with allure.step("第一步、执行SQL语句"):
        res = db.select_execute("SELECT account_name FROM `t_cst_account` WHERE STATUS = 0 AND account_name IS NOT NULL;")
    #从查询结果中随机获取一条，取第一个数据
    with allure.step("第二步、从查询结果中随机获取一条，取第一个数据"):
        account_name = random.choice(res)[0]
    # 准备请求数据
    with allure.step("第三步、准备请求数据"):
        data = {

  "accountName":account_name,
  "changeMoney": 9999
}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    #使用requests框架发送http请求
    with allure.step("第四步、发送请求"):
        r = requests.post(API_URL + "/acc/charge",json=data)
    with allure.step("第五步、获取请求url"):
        allure.attach(r.request.method,"请求方法",allure.attachment_type.TEXT)
        allure.attach(r.request.method, "请求url", allure.attachment_type.TEXT)
        allure.attach(r.request.method, "请求头", allure.attachment_type.TEXT)
        allure.attach(r.request.method, "请求正文", allure.attachment_type.TEXT)

    with allure.step("第六步、获取响应内容"):
        allure.attach(str(r.status_code), "响应状态码", allure.attachment_type.TEXT)
        allure.attach(str(r.headers), "响应头", allure.attachment_type.TEXT)
        allure.attach(str(r.text), "响应正文", allure.attachment_type.TEXT)

    with allure.step("第七步、添加断言"):
        allure.attach(r.text, "实际结果", allure.attachment_type.TEXT)
        allure.attach("账户余额不足", "预期结果", allure.attachment_type.TEXT)
        assert"账户余额不足" in r.text


    pass



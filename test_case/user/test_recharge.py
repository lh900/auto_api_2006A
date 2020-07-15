import os

import pytest
from tools.api import request_tool
from tools.data import excel_tool

data = excel_tool.get_test_case("test_case/user/充值接口测试数据.xlsx")
@pytest.mark.parametrize("account_name,money,expect",data[1],ids=data[0])
def test_recharge_01(pub_data,account_name,money,expect):
    pub_data["account_name"] = account_name
    pub_data["money"] = money
    headers={"token":pub_data["token"]}
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '充值'  # allure报告中二级分类
    # title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    status_code = 200  # 响应状态码
    expect = "充值成功"  # 预期结果
    json_data='''{
  "accountName": "${account_name}",
  "changeMoney": ${money}
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,json_data=json_data)
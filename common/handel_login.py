# coding=UTF-8
import requests
import json
import os
from S_接口耗时检测.common.handle_conf import conf

path = os.getcwd()+"\\"



def login(key='test',value='url'):
    login_url = "{}/api/individual-user/login".format(conf.get("env","base_url"))

    data = {
        'phone': conf.get("test_data","phone"),
        'password': conf.get("test_data","password"),
        'remember': 0,
        'area_code': 86}
    headers = {
        'Referer':'{}/home'.format(conf.get("env","base_url"))
    }

    try:
        r = requests.post(login_url,headers =headers, data=data)
        x = r.cookies.get('accountCenterSessionId')
        return x
    except:
        return "产生异常"

def login_company(key='test',value='url'):
    '''

    Parameters
    ----------
    company_id: 登录的企业id

    key: config.ini文件里面的【】，不用传值

    value: config.ini文件里面的值，不用传值

    Returns
    -------

    '''
    x = login()

    header = {
        'Referer':'https://user-test.tangees.com/home',
        'Cookie':'accountCenterSessionId='+ x
        }
    data = {'company_id': conf.get("test_data","company_id")}

    r = requests.post(conf.get("env","base_url")+"/api/company/enter", data=data, headers=header)

    print('登录成功！')

    writeInfo = 'accountCenterSessionId='+ r.cookies.get("accountCenterSessionId")
    # print(writeInfo)
    return writeInfo


cookies = login_company()
# print(cookies)


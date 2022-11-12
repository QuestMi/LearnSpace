# -*- coding: utf-8 -*- 
"""
Create on : 2022/11/9
@Author   : Xiao QingLin 
@File    : rqdata_test  
"""
import rqdatac, pandas, datetime


def get_fund_price():
    rqdatac.init('15811139020', 'msdc2022')
    print(rqdatac.user.get_quota())
    df = rqdatac.index_indicator(['HSI.HI'], start_date='2022-10-01', end_date='2022-11-07')
    print(df)


if __name__ == '__main__':
    get_fund_price()
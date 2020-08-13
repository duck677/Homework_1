import math
import pandas as pd
import numpy as np
import baostock as bs



lg = bs.login()
#显示登录返回信息
print('login respond error_code:'+lg.error_code)
print('login respond error_msg:'+lg.error_msg)

#####获取股票历史K线数据####

START_DATE = '2017-01-01'
END_DATE = '2018-10-25'

#详细指标参数
rs_1 = bs.query_history_k_data_plus('000001.SZ', "date,time,open,high,low,close,volume,pctChg", start_date = START_DATE, end_date = END_DATE, frequency = "5")
print('query_history_k_data_plus respond error_code:'+rs_1.error_code)
print('query_history_k_data_plus error_msg:'+rs_1.error_msg)
data_list = []
while (rs_1.error_code == '0') & rs_1.next():
    #获取一条记录，将记录合并在一起
    data_list.append(rs_1.get_row_data())
result = pd.DataFrame(data_list, columns=rs_1.fields)

s1 = result['pctChg']


rs_2 = bs.query_history_k_data_plus('399300.SZ', "date,time,open,high,low,close,volume,pctChg", start_date = START_DATE, end_date = END_DATE, frequency = "5")
print('query_history_k_data_plus respond error_code:'+rs_2.error_code)
print('query_history_k_data_plus error_msg:'+rs_2.error_msg)
data_list_2 = []
while (rs_2.error_code == '0') & rs_2.next():
    #获取一条记录，将记录合并在一起
    data_list_2.append(rs_2.get_row_data())
result = pd.DataFrame(data_list_2, columns=rs_2.fields)


s2 = result['pctChg']

#计算贝塔系数

print((np.cov(s1, s2))[0][1]/np.var(s2))

#计算夏普比率
rs_1['ex_pct_close'] = rs_1['pctChg'] - 0.04/252
print((rs_1['ex_pct_close'].mean() * math.sqrt(252))/rs_1['ex_pct_close'].std())
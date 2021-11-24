import pandas as pd
import re
import math


## 教程 http://joyfulpandas.datawhale.club/Content/ch2.html
## 教程 https://www.gairuo.com/p/pandas-io


def processA(frame):
    if (frame['compliance'] is pd.NA):
        return 1
    searchFlag = re.search('legal', frame['compliance'], re.IGNORECASE)
    if (searchFlag):
        return 3
    searchFlag = re.search('mandatory', frame['compliance'], re.IGNORECASE)
    if (searchFlag):
        return 2
    return 1


def processB(frame):
    if(frame['enforcer'] is  pd.NA):
        return 1
    searchFlag = re.search('National', frame['enforcer'], re.IGNORECASE)
    if (searchFlag):
        return 4
    searchFlag = re.search('Ministry', frame['enforcer'], re.IGNORECASE)
    if (searchFlag):
        return 3
    searchFlag = re.search('Municipal', frame['enforcer'], re.IGNORECASE)
    if (searchFlag):
        return 2
    return 1


## 读dem,得到2020年数据，还有选取需要的字段
dem_df = pd.read_csv('data/V-Dem-CY-Core-v11.1.csv', sep=',', header=0, dtype='string',
                     usecols=['country_text_id', 'year', 'v2x_polyarchy', 'v2x_libdem',
                              'v2x_delibdem', 'v2x_egaldem', 'v2x_partipdem'])

dem_df_1 = dem_df.loc[dem_df['year'] == '2020']
print("筛选操作：")
print(dem_df_1.info)

print("更换列名：")
dem_df_2 = dem_df_1.rename(columns={'country_text_id': 'ISO_A3'})

## 写入csv中
print("写入csv：")
dem_df_2.to_csv('data/V-Dem_result.csv')

## 重新读取该csv
print("读取csv：")
result_dem_df = pd.read_csv('data/V-Dem_result.csv', sep=',', header=0, dtype='string' )

## 读取主数据
print("读取total csv：")
total_df = pd.read_csv('data/total3.csv', sep=',', header=0, dtype='string')

## 两个数据进行合并
merge_df = pd.merge(total_df, result_dem_df, how='left', on='ISO_A3')
print("数据合并")

## 再新增一个字段
merge_df['enforcer_dict'] = merge_df.apply(lambda frame: processB(frame), axis=1)
print("新增字段 enforcer_dict")

## 新增一个字段
merge_df['compliance_dict'] = merge_df.apply(lambda frame: processA(frame), axis=1)
print("新增字段 compliance_dict")

## 写入文件
merge_df.to_csv('data/result_total.csv')
print("写入文件")

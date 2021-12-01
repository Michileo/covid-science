# covid-science


根据国别和日期将数据整合成一个数据集（按date_announced时间，国别的话可参照country	ISO_A3	）


1.项目corona_tscs-master--data_country--coronanet_release_allvars--下的所有国家整合（https://github.com/CoronaNetDataScience/corona_tscs），生成数据集coronasci



2.将current-covid-patients-hospital根据国别和日期整合进coronasci生成新数据集coronasci1


3.将eiu2020clean根据国别和日期整合进coronasci1生成新数据集coronasci2




整合之后，对coronasci2进行操作生成coronasci3（此代码可参照上期csv_aaa.py）
1. compliance 分3层 一层是有legal这个词的编码3，有mandatory的是2，剩下的编作1。
2. enforcer   如果National=4，Minstry=3，Municipal=2，剩下的编译为1。
3. 对新生成的compliance、enforcer变量求平均，生成新数据。



最后将result_total3_2中最后几列整合进入coronasci3，生成coronasci4
v2x_polyarchy	v2x_libdem	v2x_delibdem	v2x_egaldem	v2x_partipdem放后面

下一步对coronasci_5（新上传）进行操作生成coronasci_6（hospital）
1.API_SH.MED.BEDS.ZS_DS2_en_csv_v2_3365799文件中，按国家匹配（Country Name或者country code（对应ISOa3）），将数据整合进去，
2.具体规则为生成两列新的数据，一列是Hospital beds (per 1,000 people)，另一列是Hosyear
3.Hospital beds生成方式为用该国家最新一年的数据，例如某国数据范围为2010-2015年，此时选取2015年，另外一国为2010-2018，此时选取2018年。Hosyear即为选取的年份。




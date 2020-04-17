# coding: utf-8 
# @Time    : 2020/4/17 下午6:15
# @Software: PyCharm
# @File    : csvTest.py


from copy import deepcopy
import csv
with open("suites.csv", encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
    # rows1 = deepcopy(rows)
    # while True:
    #     name = input('请输出name,输入0退出>>>')
    #     if name == '0':
    #         break
    #     else:
    #         for i in rows1:
    #             if name == i[3]:
    #                 rows.remove(i)
    # print(rows)
    rows_dispatch_check = []
    rows_dispatch_distcp = []
    rows_dispatch_hive = []
    rows_dispatch_project = []
    rows_dispatch_spark = []
    rows_dispatch_touch = []
    rows_meta_struct = []
    rows_meta_doris = []
    rows_meta_create = []
    rows_all = []
    rows_all.append(['Status', 'Parent Suite', 'Sub Suite', 'Name', 'Description'])
    for i in rows:
        tmp = [i[0],i[4], i[6], i[9], i[10]]
        if 'TestCase.Dispatch' in i:
            # rows_dispatch.append(tmp)
            if 'TestCheck' in tmp:
                rows_dispatch_check.append(tmp)
            elif 'TestDistcp' in tmp:
                rows_dispatch_distcp.append(tmp)
            elif 'TestHive' in tmp:
                rows_dispatch_hive.append(tmp)
            elif 'TestProject' in tmp:
                rows_dispatch_project.append(tmp)
            elif 'TestSpark' in tmp:
                rows_dispatch_spark.append(tmp)
            elif 'TestTouch' in tmp:
                rows_dispatch_touch.append(tmp)
        elif 'TestCase.Meta' in i:
            if 'TestMetaStruct' in tmp:
                rows_meta_struct.append(tmp)
            elif 'TestMetaDoris' in tmp:
                rows_meta_doris.append(tmp)
            elif 'TestMapCreate' in tmp:
                rows_meta_create.append(tmp)
        else:
            print('i:', i)
    # print(rows_dispatch_check)
    # print(sorted(rows_dispatch_check))
    # print(rows_meta)
    rows_all.extend(sorted(rows_dispatch_check))
    rows_all.extend(sorted(rows_dispatch_distcp))
    rows_all.extend(sorted(rows_dispatch_hive))
    rows_all.extend(sorted(rows_dispatch_project))
    rows_all.extend(sorted(rows_dispatch_spark))
    rows_all.extend(sorted(rows_dispatch_touch))
    rows_all.extend(sorted(rows_meta_struct))
    rows_all.extend(sorted(rows_meta_doris))
    rows_all.extend(sorted(rows_meta_create))
    print(rows_all)

with open('suites_new.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(rows_all)
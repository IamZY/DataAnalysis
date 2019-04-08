import csv

#原始数据存储路径
data_path = './data/user_tag_query.10W.TRAIN'
#生成数据路径
csvfile = open(data_path + '-1w.csv', 'w')
writer = csv.writer(csvfile)
writer.writerow(['ID', 'age', 'Gender', 'Education', 'QueryList'])
#转换成utf-8编码的格式
with open(data_path, 'r',encoding='gb18030',errors='ignore') as f:
    lines = f.readlines()
    for line in lines[0:10000]:
        try:
            line.strip()
            data = line.split("\t")
            writedata = [data[0], data[1], data[2], data[3]]
            querystr = ''
            data[-1]=data[-1][:-1]
            for d in data[4:]:
                try:
                    cur_str = d.encode('utf8')
                    cur_str = cur_str.decode('utf8')
                    querystr += cur_str + '\t'
                except:
                    continue
                    #print (data[0][0:10])
            querystr = querystr[:-1]
            writedata.append(querystr)
            writer.writerow(writedata)
        except:
            #print (data[0][0:20])
            continue

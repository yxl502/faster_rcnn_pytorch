import os
import xml.etree.ElementTree as ET
import random
from os import getcwd

# 在train.txt和val.txt文件中生成各自数据集的图片绝对路径
# 再新建一个labels文件夹,其中以每张图片id为文件名生成该张图片的标注数据txt文档
# 每张txt的数据格式
# cls_id ymin xmin ymax max
# cls_id ymin xmin ymax max
# cls_id ymin xmin ymax max

# sets = ['train', 'val']

# classes = ["WhitehairedBanshee", "UndeadSkeleton", "WhitehairedMonster", "SlurryMonster", "MiniZalu", "Dopelliwin",
#            "ShieldAxe", "SkeletonKnight","Zalu","Cyclone","SlurryBeggar","Gerozaru","Catalog",
#            "InfectedMonst","Gold","StormRider","Close","Door",]
# classes = ['WBC', 'RBC', 'Platelets']
classes = ['Fire']

# classes_num = 18
# classes_num = 3
classes_num = 1
# 当前路径
# data_path = getcwd()
# print(data_path)
def convert_annotation(image_id):
    in_file = open(image_id.replace('JPGImages','Annotations').replace('jpg','xml'),'r')
    out_file = open(image_id.replace('JPGImages','labels').replace('jpg','txt'),'w')
    tree = ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('ymin').text), float(xmlbox.find('xmin').text), float(xmlbox.find('ymax').text),
             float(xmlbox.find('xmax').text))
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in b]) + '\n')


trainval_percent = 0.9
train_percent = 0.8
test_percent = 0.1
xmlfilepath = 'Annotations'
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
print(num)   # 114
list = range(num)
# print(list)
tv = int(num * trainval_percent)
print(tv)   # 102
list_tv = range(tv)
# print(list_tv)
tr = int(tv * train_percent)
print(tr)   # 81
tvv = int(tv * (1-train_percent))
print(tvv)  # 20
te = int(num * test_percent)
print(te)   # 11

trainval = random.sample(list, tv)
train = random.sample(list_tv, tr)
val = random.sample(list_tv, tvv)
test = random.sample(list, te)

ftrainval = open('ImageSets/Main/trainval.txt', 'w')
ftrain = open('ImageSets/Main/train.txt', 'w')
fval = open('ImageSets/Main/val.txt', 'w')
ftest = open('ImageSets/Main/test.txt', 'w')

for i in list:
    name = os.path.join(total_xml[i][:-4])
    if i in trainval:
        ftrainval.write(name+'\n')
    else:
        ftest.write(name+'\n')

for i in list_tv:
    name = os.path.join(total_xml[i][:-4])
    if i in train:
        ftrain.write(name + '\n')
    else:
        fval.write(name + '\n')

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()

# for image_set in sets:
#     # 如果labels文件夹不存在则创建
#     if not os.path.exists(data_path+'\labels\\'):
#         os.makedirs(data_path+'\labels\\')
#
#     image_ids = open(data_path+'\%s.txt' % (image_set)).read().strip().split()
#     for image_id in image_ids:
#         convert_annotation(image_id)

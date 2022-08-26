# faster_rcnn_pytorch  fire detection
# 1、数据准备
下载Fire数据放入data目录下

# 2、模型训练
cd pytorch_frcnn

python train.py

模型下载地址：
链接: https://pan.baidu.com/s/1BpncAs6vcVbb3ZB_sRyR3g 提取码: 69wb 

# 3、模型测试
python dection_img.py

# 4、训练自己的数据集
准备自己的数据VOC格式
修改 config.py

 class_name 改为自己的类别信息
# class_name = ('aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable',
#               'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor')

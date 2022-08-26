import os
import shutil

# train = os.listdir('./train')
train = os.listdir('./test')
# print(train)
for tr in train:
    if tr.endswith('.jpg'):
        shutil.move('./test/' + tr, './train/' + 'JPEGImages')

    if tr.endswith('.xml'):
        shutil.move('./test/' + tr, './train/' + 'Annotations')
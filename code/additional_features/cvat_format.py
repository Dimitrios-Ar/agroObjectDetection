import os, shutil, glob
from zipfile import ZipFile


def create_zip_for_cvat():
    os.chdir('annotation_txts')
    zipObj = ZipFile('cvat_annotations.zip', 'w')
    if not os.path.exists('object.names'):
        shutil.copyfile('../../data/config_files/object.names', 'object.names')
    zipObj.write('object.names')
    txt_files = glob.glob('*.txt')
    for txt in txt_files:
        zipObj.write(txt)
        os.remove(txt)
    zipObj.close()

create_zip_for_cvat()
import os, shutil, glob, sys

#training_setup = '../../saved_trainings/FULL_augmented_only_on_Randers_NOV_filtered_400_TRAINING_YT_100_NOV'
training_setup = sys.argv[1]
print(sys.argv[0])
data_used = '0' #used to save annotation files. option 1 for only yt_google data, option 2 for yt_google and randers_sep, and option 3 for yt_google data, randers_sep and randers_nov
type = 'tiny' #or 'full'
test = '../data/config_files/test.txt'
train = '../data/config_files/train.txt'
weights = glob.glob('../data/weights/last_training_weights/*.weights')

os.mkdir(training_setup)

if type == 'tiny':
    cfg = '../data/config_files/yolov3-tiny-obj.cfg'
    for weight in weights:
        weight_type = weight.split('/')[-1].split('-')[-2]
        if weight_type == 'tiny':
            shutil.copy(weight, training_setup)
elif type == 'full':
    cfg = '../data/config_files/yolov3-obj.cfg'
    for weight in weights:
        weight_type = weight.split('/')[-1].split('-')[-2]
        if weight_type == 'yolov3':
            shutil.copy(weight, training_setup)
else:
    print('no cfg file was saved')
chart = '../Yolov3_d/chart.png'


shutil.copy(chart,training_setup)
shutil.copy(cfg,training_setup)
shutil.copy(train,training_setup)
shutil.copy(test,training_setup)

if data_used == '1':
    yt_annotations = glob.glob('../../dataset/yt_and_google_data/*.txt')
    os.mkdir(training_setup+'/yt_and_google_data')
    for txt in yt_annotations:
        shutil.copy(txt, training_setup+'/yt_and_google_data')
elif data_used == '2':
    yt_annotations = glob.glob('../../dataset/yt_and_google_data/*.txt')
    os.mkdir(training_setup + '/yt_and_google_data')
    for txt in yt_annotations:
        shutil.copy(txt, training_setup + '/yt_and_google_data')
    randers_sep_annotations = glob.glob('../../dataset/randers_sep/*.txt')
    os.mkdir(training_setup + '/randers_sep')
    for txt in randers_sep_annotations:
        shutil.copy(txt, training_setup + '/randers_sep')
elif data_used == '3':
    yt_annotations = glob.glob('../../dataset/yt_and_google_data/*.txt')
    os.mkdir(training_setup + '/yt_and_google_data')
    for txt in yt_annotations:
        shutil.copy(txt, training_setup + '/yt_and_google_data')
    randers_sep_annotations = glob.glob('../../dataset/randers_sep/*.txt')
    os.mkdir(training_setup + '/randers_sep')
    for txt in randers_sep_annotations:
        shutil.copy(txt, training_setup + '/randers_sep')
    randers_nov_annotations = glob.glob('../../dataset/randers_nov/*.txt')
    os.mkdir(training_setup + '/randers_nov')
    for txt in randers_nov_annotations:
        shutil.copy(txt, training_setup + '/randers_nov')
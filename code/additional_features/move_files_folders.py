import os, shutil, glob

def move_file():
    #os.mkdir('../../dataset/yt_and_google_data')
    source = 'data_augmentation/equalized'
    destination = 'data_augmentation/yt_and_google_data'
    counter = 0
    files = glob.glob(source+'/*')
    for file in files:
        counter += 1
        new_file = file.split('/')[-1]
        print(file)
        shutil.copy(file,destination+'/'+new_file)
    print(counter)

def count_files():
    current_dir = 'data_augmentation/yt_and_google_data'
    counter = 0
    files = glob.glob(current_dir+'/*')
    for file in files:
        counter += 1
    print(counter)

def delete_folder():
    current_dir = '../../dataset/yt_and_google_data'
    shutil.rmtree('../../dataset/yt_and_google_data')


#move_file()
count_files()
#delete_folder()
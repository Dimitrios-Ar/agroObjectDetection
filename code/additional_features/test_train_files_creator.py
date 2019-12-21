import os, sys, glob, shutil

splitting_method = input('How would you like to split the data? \nType "1" to use one folder for testing data and another folder for training data\nType "2" to split the data of one folder into testing and training data\n')

def split_from_one_folder():
    try:
        os.mkdir('test_train_files/')
    except OSError as error:
        shutil.rmtree('test_train_files/')
        os.mkdir('test_train_files/')

    current_dir = input('Type path of folder to be split (example "../../dataset/yt_and_google_data") : ')
    image_type = input('What is the image type?\nType "1" for default youtube/google image type (.jpg) \nType "2" for default Randers recordings image_raw (.bmp) \nIf other type, write it in the format .bmp/.png/.jpg/.. : ')
    if image_type == '1':
        image_type = '.jpg'
    elif image_type == '2':
        image_type = '.bmp'

    percentage_test = input('Please type percentage of split (If "30", then 30%'+' of the images will be used as testing and the remaining (70%) as training images) : ')
    file_train = open('train.txt', 'w')
    file_test = open('test.txt', 'w')
    counter = 1
    index_test = round(100 / int(percentage_test))


    for pathAndFilename in glob.iglob(os.path.join(current_dir, '*'+image_type)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        if counter == index_test:
            counter = 1
            file_test.write(current_dir + "/" + title + image_type + "\n")
        else:
            file_train.write(current_dir + "/" + title + image_type + "\n")
            counter = counter + 1
    file_train.close()
    file_test.close()
    shutil.rmtree('test_train_files/')
    print('Files saved in current folder')

def use_two_folders():
    try:
        os.mkdir('test_train_files/')
    except OSError as error:
        shutil.rmtree('test_train_files/')
        os.mkdir('test_train_files/')

    train_folder = input('Type path of folder used for training (example "../../dataset/yt_and_google_data") : ')
    image_type_train = input('What is the image type of the train folder images?\nType "1" for default youtube/google image type (.jpg) \nType "2" for default Randers recordings image_raw (.bmp) \nIf other type, write it in the format .bmp/.png/.jpg/.. : ')
    test_folder = input('Type path of folder used for testing (example "../../dataset/randers_sep") : ')
    image_type_test = input('What is the image type of the test folder images?\nType "1" for default youtube/google image type (.jpg) \nType "2" for default Randers recordings image_raw (.bmp) \nIf other type, write it in the format .bmp/.png/.jpg/.. : ')
    
    if image_type_train == '1':
        image_type_train = '.jpg'
    elif image_type_train == '2':
        image_type_train = '.bmp'
    
    if image_type_test == '1':
        image_type_test = '.jpg'
    elif image_type_test == '2':
        image_type_test = '.bmp'

    file_train = open('train.txt', 'w')
    file_test = open('test.txt', 'w')
    #print(test_folder,train_folder)

    for pathAndFilename in glob.iglob(os.path.join(train_folder, '*'+image_type_train)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        #print(train_folder,title,image_type_train)
        file_train.write(train_folder + "/" + title + image_type_train + "\n")
    for pathAndFilename in glob.iglob(os.path.join(test_folder, '*'+image_type_test)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        file_test.write(test_folder + "/" + title + image_type_test + "\n")

    file_train.close()
    file_test.close()
    shutil.rmtree('test_train_files/')
    print('Files saved in current folder')


if splitting_method == '2':
    split_from_one_folder()
elif splitting_method == '1':
    use_two_folders()

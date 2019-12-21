import os, shutil, sys, glob

def class_counter_test():
    test_temp_txt = 'counter_txt/'
    try:
        os.mkdir(test_temp_txt)
    except OSError as error:
        shutil.rmtree(test_temp_txt)
        os.mkdir(test_temp_txt)

    annotation_counter, images_counter = 0,0

    class_0_test, class_1_test, class_2_test, class_3_test, class_4_test, = 0,0,0,0,0

    test_file_name = input('Which file do you want to count?\nType "1" for default train file (../data/config_files/train.txt)\nType "2" for default test file (../data/config_files/test.txt) \nWrite path for any other file: ')
    if test_file_name == '1':
        test_file_name = '../data/config_files/train.txt'
    elif test_file_name == '2':
        test_file_name = '../data/config_files/test.txt'
    #test_file_name = "/home/aut/dimitris/Yolo_v3/darknet/added_features/train_test_txt/test.txt" #+ #test_file_name

    image_type = input('What is the image type?\nType "1" for default youtube/google image type (.jpg) \nType "2" for default Randers recordings image_raw (.bmp) \nIf other type, write it in the format .bmp/.png/.jpg/.. : ')
    if image_type == '1':
        image_type = '.jpg'
    elif image_type == '2':
        image_type = '.bmp'

    test_file = open(test_file_name, "r")

    for line in test_file:
        if len(line) > 1:
            img_to_txt = line.rstrip().replace(image_type,'.txt')
            shutil.copy(str(img_to_txt), test_temp_txt)

    files = glob.glob(test_temp_txt+'*.txt')
    temp_test = open('classes_counter.txt','w+')

    for name in files:
        try:
            images_counter += 1
            f = open(name)
            for line in f:
                annotation_counter += 1
                temp_test.write(line)
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise          
    temp_test.close()
    all_classes_test = open('classes_counter.txt', 'r')
    for line in all_classes_test:
        if line[0] == '0':
            class_0_test += 1
        elif line[0] == '1':
            class_1_test += 1
        elif line[0] == '2':
            class_2_test += 1
        elif line[0] == '3':
            class_3_test += 1
        elif line[0] == '4':
            class_4_test += 1

    os.remove("classes_counter.txt")
    shutil.rmtree(test_temp_txt)
    print("Found " + str(annotation_counter) + " objects in " + str(images_counter) + " images")
    print("Class 0 (tree): " + str(class_0_test) + "\nClass 1 (buggy): " + str(class_1_test) + "\nClass 2 (trafficPole): " + str(class_2_test)
             + "\nClass 3 (tractor): " + str(class_3_test) + "\nClass 4 (person): " + str(class_4_test))


def class_counter_on_folder():
    test_temp_txt = 'counter_txt/'
    try:
        os.mkdir(test_temp_txt)
    except OSError as error:
        shutil.rmtree(test_temp_txt)
        os.mkdir(test_temp_txt)

    annotation_counter, images_counter = 0, 0

    class_0_test, class_1_test, class_2_test, class_3_test, class_4_test, = 0, 0, 0, 0, 0
    files = glob.glob('../../../dataset/original_data(no_augment_no_filter)/yt_and_google_data//*.txt')
    #files = glob.glob('class_removal/new_annotations/*.txt')

    temp_test = open('classes_counter.txt', 'w+')

    for name in files:
        try:
            images_counter += 1
            f = open(name)
            for line in f:
                annotation_counter += 1
                temp_test.write(line)
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise
    temp_test.close()
    all_classes_test = open('classes_counter.txt', 'r')
    for line in all_classes_test:
        if line[0] == '0':
            class_0_test += 1
        elif line[0] == '1':
            class_1_test += 1
        elif line[0] == '2':
            class_2_test += 1
        elif line[0] == '3':
            class_3_test += 1
        elif line[0] == '4':
            class_4_test += 1

    os.remove("classes_counter.txt")
    shutil.rmtree(test_temp_txt)
    print("Found " + str(annotation_counter) + " objects in " + str(images_counter) + " images")
    print("Class 0 : " + str(class_0_test) + "\nClass 1 : " + str(
        class_1_test) + "\nClass 2 : " + str(class_2_test)
          + "\nClass 3 : " + str(class_3_test) + "\nClass 4 : " + str(class_4_test))




#class_counter_test()
class_counter_on_folder()

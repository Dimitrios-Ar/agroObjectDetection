import os, shutil, sys, glob

def class_removal():

    old_classes_names = open('class_removal/old.names', "r")
    new_classes_names = open('class_removal/new.names', "r")
    global dict
    dict = {}
    counter_old,counter_new = 0,0

    for line in old_classes_names:
        dict[line.rstrip()] = [counter_old]
        counter_old += 1
    for line in new_classes_names:
        that_value = dict[line.rstrip()]
        that_value.append(counter_new)
        counter_new += 1
    #print(len(dict.values()))
    global class_list
    class_list = list(dict.values())
    print(len(class_list))

def new_annotations():
    files = glob.glob('class_removal/old_annotations/*.txt')
    #temp_test = open('class_removal/old_annotations/*.txt', 'w+')
    for file in files:
        file = file.split('/')
        #print(file)
        old_annotations = open('class_removal/old_annotations/'+file[2],'r')
        new_annotations = open('class_removal/new_annotations/'+file[2],'w')
        for line in old_annotations:
            line = line.split()
            print('was',line[0])
            #print(len(class_list[int(line[0])]))
            if len(class_list[int(line[0])]) == 1:
                print('adios', int(line[0]))
            elif len(class_list[int(line[0])]) == 2:
                new_id = class_list[int(line[0])][1]
                print('new_id', new_id)
                new_annotations.write(str(new_id) + ' ' + line[1] + ' ' + line[2] + ' ' + line[3] + ' ' + line[4] + '\n')



class_removal()
new_annotations()
import os
from PIL import Image

def convert_predicted_annotation_to_yolov3_format():
    if not os.path.exists('annotation_txts'):
        os.makedirs('annotation_txts')
    f = open('results.txt', "r")
    txt_annotation_file = open('blank_file.txt', "w+")
    image_type = input('What is the image type?\nType "1" for default youtube/google image type (.jpg) \nType "2" for default Randers recordings image_raw (.bmp) \nIf other type, write it in the format .bmp/.png/.jpg/.. : ')
    if image_type == '1':
        image_type = '.jpg'
    elif image_type == '2':
        image_type = '.bmp'
    counter = 0
    for line in f:
        if len(line) > 30:
            line_element = line.split(' ',1)
            if (line_element[0]) == 'Enter':
                txt_annotation_file.close()
                counter += 1
                for_image = line_element[1].rsplit('/',1)
                image_path = for_image[0].lstrip('Image Path: ')
                file_name = for_image[1].split(' ',1)[0].rstrip(':')
                txt_name = 'annotation_txts/' + file_name.rstrip(str(image_type)) + '.txt'
                # print(line_element[3].strip('/home/aut/dimitris/Yolo_v3/darknet/yt_frames/1//'))
                im = Image.open(os.path.join(image_path,file_name))
                image_width, image_height = im.size
                im.close()
                txt_annotation_file = open(txt_name, "w+")
                print(str(file_name + ' for image dimensions: ' + str(image_width) + ' * ' + str(image_height)))
            elif (line_element[0]) == 'tree:':
                class_id = '0'
                class_line_element = line_element[1].split()
                width_t = str(int(class_line_element[6]) / image_width)
                height_t = str(int(class_line_element[8].rstrip(')')) / image_height)
                position_t_x = str(int(class_line_element[2]) / image_width + float(width_t) / 2)
                position_t_y = str(int(class_line_element[4]) / image_height + float(height_t) / 2)
                txt_annotation_file.write(
                    class_id + ' ' + position_t_x + ' ' + position_t_y + ' ' + width_t + ' ' + height_t + '\n')
                print(str(class_line_element[
                              0]) + ' that the object *tree* of class *' + class_id + '* is in position x:' + position_t_x + ', y:' + position_t_y + ', w:' + width_t + ', h:' + height_t)
            elif (line_element[0]) == 'buggy:':
                class_id = '1'
                class_line_element = line_element[1].split()
                width_t = str(int(class_line_element[6]) / image_width)
                height_t = str(int(class_line_element[8].rstrip(')')) / image_height)
                position_t_x = str(int(class_line_element[2]) / image_width + float(width_t) / 2)
                position_t_y = str(int(class_line_element[4]) / image_height + float(height_t) / 2)
                txt_annotation_file.write(
                    class_id + ' ' + position_t_x + ' ' + position_t_y + ' ' + width_t + ' ' + height_t + '\n')
                print(str(class_line_element[
                              0]) + ' that the object *buggy* of class *' + class_id + '* is in position x:' + position_t_x + ', y:' + position_t_y + ', w:' + width_t + ', h:' + height_t)
            elif (line_element[0]) == 'trafficPole:':
                class_id = '2'
                class_line_element = line_element[1].split()
                width_t = str(int(class_line_element[6]) / image_width)
                height_t = str(int(class_line_element[8].rstrip(')')) / image_height)
                position_t_x = str(int(class_line_element[2]) / image_width + float(width_t) / 2)
                position_t_y = str(int(class_line_element[4]) / image_height + float(height_t) / 2)
                txt_annotation_file.write(
                    class_id + ' ' + position_t_x + ' ' + position_t_y + ' ' + width_t + ' ' + height_t + '\n')
                print(str(class_line_element[
                              0]) + ' that the object *trafficPole* of class *' + class_id + '* is in position x:' + position_t_x + ', y:' + position_t_y + ', w:' + width_t + ', h:' + height_t)
            elif (line_element[0]) == 'tractor:':
                class_id = '3'
                class_line_element = line_element[1].split()
                width_t = str(int(class_line_element[6]) / image_width)
                height_t = str(int(class_line_element[8].rstrip(')')) / image_height)
                position_t_x = str(int(class_line_element[2]) / image_width + float(width_t) / 2)
                position_t_y = str(int(class_line_element[4]) / image_height + float(height_t) / 2)
                txt_annotation_file.write(
                    class_id + ' ' + position_t_x + ' ' + position_t_y + ' ' + width_t + ' ' + height_t + '\n')
                print(str(class_line_element[
                              0]) + ' that the object *tractor* of class *' + class_id + '* is in position x:' + position_t_x + ', y:' + position_t_y + ', w:' + width_t + ', h:' + height_t)
            elif (line_element[0]) == 'person:':
                class_id = '4'
                class_line_element = line_element[1].split()
                width_t = str(int(class_line_element[6]) / image_width)
                height_t = str(int(class_line_element[8].rstrip(')')) / image_height)
                position_t_x = str(int(class_line_element[2]) / image_width + float(width_t) / 2)
                position_t_y = str(int(class_line_element[4]) / image_height + float(height_t) / 2)
                txt_annotation_file.write(
                    class_id + ' ' + position_t_x + ' ' + position_t_y + ' ' + width_t + ' ' + height_t + '\n')
                print(str(class_line_element[
                              0]) + ' that the object *person* of class *' + class_id + '* is in position x:' + position_t_x + ', y:' + position_t_y + ', w:' + width_t + ', h:' + height_t)

    # copy_to_newPath = shutil.copy(str(line.rstrip()), newPath)
    f.close()
    os.remove('blank_file.txt')
    print('Total Images: ' + str(counter))
    # print(image_width, image_height)

convert_predicted_annotation_to_yolov3_format()
import glob, os, cv2


def filter_by_size():
    kept_counter = 0
    deleted_counter = 0
    current_dir = input('Type folder path which contains the final images and annotations (example: "all_data/annotatedReady") : ')
    #current_dir = '../../dataset/txts_before_filtering/yt_and_google_data'
    files = glob.glob(current_dir+'/*.txt')
    print(current_dir)
    print(files)
    threshold = 1000
    path = os.path.join(current_dir,'filtered_annotations_by_size/'+str(threshold)+'/')
    print(path)
    try:
        os.makedirs(path)
    except OSError as error:
        check_input = input('Folder already exists. Please make sure to copy or delete previous data.')
        sys.exit()

    image_type = input('What is the image type?\nType "1" for default youtube/google image type (.jpg) \nType "2" for default Randers recordings image_raw (.bmp) \nIf other type, write it in the format .bmp/.png/.jpg/.. : ')
    if image_type == '1':
        image_type = '.jpg'
    elif image_type == '2':
        image_type = '.bmp'

    for name in files:
        print('name', name)
        try:
            txt_name = name.split('/')[-1]
            image_loc = os.path.join(current_dir, txt_name.replace('.txt',image_type))
            image = cv2.imread(image_loc, 1)
            height, width, channels = image.shape
            filtered_txt_name = os.path.join(path, txt_name)
            filtered_txt_file = open(filtered_txt_name,"w+")
            #print(txt_name)
            with open(name) as f:
                print(f)
                for line in f:
                    line_elements = line.split()
                    ###NEED TO CHECK THE FORMAT OF ANNOTATION
                    #in yolov3, it should be 0,1,2,3,4 = class, centerX, centerY, width, height
                    obj_size = float(line_elements[3]) * width * float(line_elements[4]) * height
                    print('obj_size', obj_size, line_elements[3], line_elements[4])
                    if obj_size < threshold:
                        deleted_counter += 1
                        print('deleted an object of size ', int(obj_size), 'pixels in an image of ',width,'*', height)
                    else:
                        filtered_txt_file.write(line)
                        kept_counter += 1
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise 
    deleted_percentage = float(float(deleted_counter)/(float(deleted_counter)+float(kept_counter))) * 100
    print('Deleted '+ str(deleted_counter) + ' annotations, around ' + str(("%.4f" % deleted_percentage)) + '%')  

filter_by_size()
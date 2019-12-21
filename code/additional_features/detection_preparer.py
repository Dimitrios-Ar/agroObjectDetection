import os,glob

def create_txt_of_images_to_use_by_detector():
    current_dir = input('Type folder path which contains the images to be detected (example: "all_data/annotatedReady") : ')
    current_dir = os.path.abspath(current_dir)
    file_test = open('auto_annotate.txt', 'w')
    image_type = input('What is the image type?\nType "1" for default youtube/google image type (.jpg) \nType "2" for default Randers recordings image_raw (.bmp) \nIf other type, write it in the format .bmp/.png/.jpg/.. : ')
    if image_type == '1':
        image_type = '.jpg'
    elif image_type == '2':
        image_type = '.bmp'

    for pathAndFilename in glob.iglob(os.path.join(current_dir,"*"+image_type)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        file_test.write(current_dir + "/" + title + image_type + "\n")

create_txt_of_images_to_use_by_detector()
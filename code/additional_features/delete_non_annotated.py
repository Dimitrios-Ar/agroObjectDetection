import os, glob, shutil

def delete_non_annotated():
    current_dir = input('Type folder path which contains the final images and annotations (example: "all_data") : ')
    image_type = input('What is the image type?\nType "1" for default youtube/google image type (.jpg) \nType "2" for default Randers recordings image_raw (.bmp) \nIf other type, write it in the format .bmp/.png/.jpg/.. : ')
    if image_type == '1':
        image_type = '.jpg'
    elif image_type == '2':
        image_type = '.bmp'

    if not os.path.exists(os.path.join(current_dir,'notAnnotated')):
        os.makedirs(os.path.join(current_dir,'notAnnotated'))
    if not os.path.exists(os.path.join(current_dir,'annotatedReady')):
        os.makedirs(os.path.join(current_dir,'annotatedReady'))

    files_txt = glob.glob(current_dir+'/*.txt')
    files_img = glob.glob(current_dir+'/*'+image_type)
    for img in files_img:
        img_name = img.split('/')[-1]
        img_name = img_name.replace(img_name.split('.')[-1],'')
        for txt in files_txt:
            txt_name = txt.split('/')[-1]
            txt_name =txt_name.replace(txt_name.split('.')[-1],'')
            if txt_name == img_name:
                shutil.move(txt, os.path.join(current_dir,'annotatedReady'))
                shutil.move(img, os.path.join(current_dir,'annotatedReady'))

    files_img_2 = glob.glob(current_dir+'/*'+image_type)
    for img_2 in files_img_2:
        shutil.move(img_2, os.path.join(current_dir,'notAnnotated'))

    print("Moved images that are annotated to 'annotatedReady' and remaining images to 'notAnnotated'")


delete_non_annotated()
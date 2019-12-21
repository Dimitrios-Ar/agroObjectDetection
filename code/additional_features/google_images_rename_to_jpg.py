import os, glob, cv2

def rename_downloaded_files():
    folder = input('Please provide folder that contains images (example "google_data"): ')
    destination = input('Please provide first part of name of files (example "google_tractors"): ')
    i = 0
    images = glob.glob(folder+'/*')
    for image in images:
        if os.path.getsize(image) > 1000:
            img = cv2.imread(image, 1)
            height, width, channels = img.shape
            if height > 600 and width > 600:
                cv2.imwrite(os.path.join(folder,destination) + '_' + str(i) + ".jpg", img)
                i += 1
            else:
                print('found a small ', image)
        else:
            print('found a broken ', image)
        os.remove(image)
    print('saved', i, 'images')

rename_downloaded_files()
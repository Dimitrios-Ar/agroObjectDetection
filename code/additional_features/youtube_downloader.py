import cv2, datetime, shutil, os, pytube, glob

def download_from_yt():
    if not os.path.exists('saved_frames'):
        os.makedirs('saved_frames')
    if not os.path.exists('videos'):
        os.makedirs('videos')
                
    try:
        youtube_link = input('Please paste the youtube link: ')
        yt = pytube.YouTube(youtube_link)
        global new_name
        new_name = pytube.extract.video_id(youtube_link)
        stream = yt.streams.filter(subtype='mp4').get_by_itag('22')
        print('Saving video under name: videos/' + new_name + '.mp4')
        stream.download(output_path='videos/', filename=new_name)
        video_links = open('video_links.txt', 'a')
        video_links.write(youtube_link+'\n')
    except:
        print("Connection Error")

def save_frames():
    video_path = 'videos/'+new_name+'.mp4'

    vidcap = cv2.VideoCapture(video_path)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = int(frame_count / fps)
    frameRate = input('Please select interval between saved frames: (example: "5" will capture an image each 5 seconds of the video) : ')
    print('Started saving frames.. Please be patient..')
    count = 1
    sec = 0  # 810
    now = datetime.datetime.now()
    stamp = int((now - datetime.datetime(2010, 1, 1)).total_seconds())
    os.mkdir('saved_frames/'+new_name)
    while sec < duration:
        count = count + 1
        sec = sec + int(frameRate)
        vidcap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
        hasFrames, image = vidcap.read()
        try:
            cv2.imwrite("saved_frames/"+new_name+"/image_" + str(stamp) + "_" + str(count) + ".png", image)
        except:
            print('no frame saved')
    print('Saved ' + str(count) + ' images at ' + new_name + ' folder')

def rename_downloaded_files_and_delete_bad():
    i = 0
    pngs = glob.glob('saved_frames/'+new_name+'/*.png')
    for j in pngs:
        if os.path.getsize(j) > 1000:
            img = cv2.imread(j)
            cv2.imwrite(j[:-3] + 'jpg', img)
        else:
            print('found a broken', j)
    for k in pngs:
        os.remove(k)
    os.chdir('saved_frames')
    for filename in os.listdir(new_name+'/'):
        dst = new_name + '/' + new_name + '_' + str(i) + ".jpg"
        src = new_name + '/' + filename
        os.rename(src, dst)
        i += 1

def delete_video():
    os.chdir('../')
    shutil.rmtree('videos')

download_from_yt()
save_frames()
rename_downloaded_files_and_delete_bad()
delete_video()
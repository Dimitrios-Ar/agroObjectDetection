cd ../Yolov3_d

./darknet detector train ../data/config_files/config_1.data ../data/config_files/yolov3-tiny-obj.cfg  ../data/weights/yolov3-tiny.conv.15 -map

cd ../additional_features
python save_trainings.py ../../saved_trainings/test_3

#cd ../Yolov3_d
#./darknet detector train ../data/config_files/config_2.data ../data/config_files/yolov3-tiny-obj.cfg  ../data/weights/yolov3-tiny.conv.15 -map


#cd ../additional_features
#python save_trainings.py ../../saved_trainings/test_2

cd ../Yolov3_d

./darknet detector test ../data/config_files/config.data ../data/config_files/yolov3-tiny-obj.cfg ../data/weights/config_1.weights -dont_show -ext_output < ../additional_features/auto_annotate.txt >../additional_features/results.txt

echo Saved detections into results.txt
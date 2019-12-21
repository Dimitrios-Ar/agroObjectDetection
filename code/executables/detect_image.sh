cd ../Yolov3_d
if [ $# -eq 0 ]
  then
    echo "No arguments supplied, running on default '../data/test_files/randers_1.bmp' image"
    ./darknet detector test ../data/config_files/config.data ../data/config_files/yolov3-tiny-obj.cfg ../data/weights/config_1.weights -ext_output ../data/test_files/randers_1.bmp
elif [ $# -eq 1 ]
	then
    ./darknet detector test ../data/config_files/config.data ../data/config_files/yolov3-tiny-obj.cfg ../data/weights/config_1.weights -ext_output $1
else
	echo "Please run again and provide one argument with the image path you which to detect, or no argument to use default '../data/test_files/randers_1.bmp'"
fi

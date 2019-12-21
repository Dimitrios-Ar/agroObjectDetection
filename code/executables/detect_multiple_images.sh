cd ../Yolov3_d

if [ $# -eq 0 ]
  then
    echo "No arguments supplied, running on default '../data/config_files/test.txt' images"
    ./darknet detector test ../data/config_files/config.data ../data/config_files/yolov3-tiny-obj.cfg ../data/weights/config_1.weights -ext_output < ../data/config_files/test.txt
elif [ $# -eq 1 ]
	then
    ./darknet detector test ../data/config_files/config.data ../data/config_files/yolov3-tiny-obj.cfg ../data/weights/config_1.weights -ext_output < $1
else
	echo "Please run again and provide one argument with the txt file that contains the paths to the images, or no argument to use default '../data/config_files/test.txt'"
fi

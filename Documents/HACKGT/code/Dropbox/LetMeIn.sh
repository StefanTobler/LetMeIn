
#! /bin/bash

#This code assumes the recognize.sh file and takephoto.py are stored in a
#Dropbox folder on the system, which makes the url of the image available online
#To get the url, make the link of the Dropbox photo available, and replace
#the query (?) with ?raw=1. Then, create 2 index.txt files with contents of '0'
#in the ~/Dropbox folder and your <file path> location, where the other python
#files are stored
python ~/Dropbox/takephoto.py
num=$(head -n 1 index.txt)
one=1
num1=$(($num + $one))
mv ~/Dropbox/face$num.PNG ~/Dropbox/face$num1.PNG

cd ~/<file path>
#sleeps to give dropbox time to receive the file
sleep 3.5
result=$(python -c 'import compare; print(compare.get_confidence())')
cd ~/Dropbox
cp ~/Desktop/Programming/HackGT2018/index.txt index.txt
echo $result
one=1;

#if the count is high enough, compare.py returns 1 and turns the motor
if [ $result == 1 ]
then
python ~/<file path>/actuate.py
fi

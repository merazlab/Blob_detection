## Question

In the given image, create an algorithm that counts the number of white spots in the image.  You can imagine the image as a depth map whiter pixels are closer to the camera. Each spot is the depth image of a head taken by a depth sensing camera placed above a crowd of people and pointing downwards.  The application needs to count the number of heads, and this is done by counting the number of white spots in the image. There is noise in the image, so it is not very easy to count the number of spots.

## Project setup

```
# Create conda environment
conda create -n env37 python=3.7

# Activate conda environment
conda activate env37
```

Python package install
```
pip install numpy==1.20.3
pip install matplotlib=3.5.1
pip install opencv-python==4.5.5.62

```

## Method-1 input/output
```
python method1.py

#output
Total no of blobs detected-22
```
![output1](output/output1.jpg)


## Method-2 input/output
```
python method2.py

#output
Total no of blobs detected-20
```
![output1](output/output2.jpg)

## Reference

https://opencv.org/

https://learnopencv.com/blob-detection-using-opencv-python-c/
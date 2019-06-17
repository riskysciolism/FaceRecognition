# FaceRecognition

## Prerequisites ##
Please download the latest [OpenCV Release](https://opencv.org/releases/) and place the classifier you'd like to use in the root directory of this repository.

If you plan to use your build in webcam you don't have to change anything, otherwise you might need to change the zero in line 8 to the number corresponding to your camera.

```python
cap = cv2.VideoCapture(0)
```


## Run ##
Now simply run:

```python
python faceRecog.py
```


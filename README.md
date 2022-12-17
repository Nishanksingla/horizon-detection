# horizon-detection

# Instructions to run the code

To run the horizon detection, run the script `horizon_line_detection.py` as shown below. The script takes 2 arguments as input `input_folder` and `output_folder`. The value of these 2 parameters can be either relative path of the folder with respect to the script or can be absolute paths. The script will save the output images with the horizon line in the output folder with the same name as the input image, along with a `predictions.json` with the same format as `ground_truth.json`

Note: Before running the script please install the dependencies using the `requirements.txt` file. Simply run `pip install -r requirements.txt` in your terminal. I would suggest to create a virtual env and install these dependencies in the virtual env. I have used Python 3.9.7 version to develop and to execute the script.

```
python horizon_line_detection.py --input_folder <input_1> --output_folder <output_1>
```
### Here are the complete sets of the commands that one can use to run the program. 

```
Open the terminal and go to this projects folder.
1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python horizon_line_detection.py --input_folder input_1 --output_folder output_1

```


# Evaluation Metric: 
I have used Euclidean distance as a evaluation metric. It calculates the distance between 2 points. I think it's a good metric to use to evaluate the prediction of the points. This is for a single point. I have used root mean square error (RMSE) for all the left points and the right points. 

# Instructions to run the evaluation script
Evaluation script also takes 
```
python evaluation.py --input_folder input_2 --output_folder output_2  
```

### Evaluation metric output for input 1 folder
```
For image: frame0001.jpg, evaluation metric for left point: 22, right point: 4
For image: frame0002.jpg, evaluation metric for left point: 11, right point: 2
For image: frame0003.jpg, evaluation metric for left point: 20, right point: 3
For image: frame0004.jpg, evaluation metric for left point: 25, right point: 6
For image: frame0005.jpg, evaluation metric for left point: 32, right point: 6
For image: frame0006.jpg, evaluation metric for left point: 29, right point: 4
For image: frame0007.jpg, evaluation metric for left point: 24, right point: 7
For image: frame0008.jpg, evaluation metric for left point: 30, right point: 21
For image: frame0009.jpg, evaluation metric for left point: 26, right point: 14
For image: frame0010.jpg, evaluation metric for left point: 29, right point: 6
For image: frame0011.jpg, evaluation metric for left point: 30, right point: 5
For image: frame0012.jpg, evaluation metric for left point: 30, right point: 5
For image: frame0013.jpg, evaluation metric for left point: 34, right point: 37
For image: frame0014.jpg, evaluation metric for left point: 28, right point: 3
For image: frame0015.jpg, evaluation metric for left point: 28, right point: 3
For image: frame0016.jpg, evaluation metric for left point: 26, right point: 5
For image: frame0017.jpg, evaluation metric for left point: 29, right point: 20
For image: frame0018.jpg, evaluation metric for left point: 26, right point: 5
For image: frame0019.jpg, evaluation metric for left point: 24, right point: 5
For image: frame0020.jpg, evaluation metric for left point: 24, right point: 5
For image: frame0021.jpg, evaluation metric for left point: 24, right point: 7
For image: frame0022.jpg, evaluation metric for left point: 24, right point: 5
For image: frame0023.jpg, evaluation metric for left point: 23, right point: 5
For image: frame0024.jpg, evaluation metric for left point: 24, right point: 7
For image: frame0025.jpg, evaluation metric for left point: 24, right point: 7
For image: frame0026.jpg, evaluation metric for left point: 23, right point: 7
For image: frame0027.jpg, evaluation metric for left point: 29, right point: 5
For image: frame0028.jpg, evaluation metric for left point: 17, right point: 8
For image: frame0029.jpg, evaluation metric for left point: 14, right point: 5
For image: frame0030.jpg, evaluation metric for left point: 14, right point: 6
For image: frame0031.jpg, evaluation metric for left point: 4, right point: 11
For image: frame0032.jpg, evaluation metric for left point: 6, right point: 8
For image: frame0033.jpg, evaluation metric for left point: 9, right point: 9
For image: frame0034.jpg, evaluation metric for left point: 4, right point: 8
For image: frame0035.jpg, evaluation metric for left point: 55, right point: 10
For image: frame0036.jpg, evaluation metric for left point: 5, right point: 11
For image: frame0037.jpg, evaluation metric for left point: 2, right point: 8
For image: frame0038.jpg, evaluation metric for left point: 8, right point: 8
For image: frame0039.jpg, evaluation metric for left point: 70, right point: 8
For image: frame0040.jpg, evaluation metric for left point: 72, right point: 7
For image: frame0041.jpg, evaluation metric for left point: 7, right point: 11
For image: frame0042.jpg, evaluation metric for left point: 1, right point: 9
For image: frame0043.jpg, evaluation metric for left point: 64, right point: 10
For image: frame0044.jpg, evaluation metric for left point: 8, right point: 13
For image: frame0045.jpg, evaluation metric for left point: 9, right point: 8
For image: frame0046.jpg, evaluation metric for left point: 72, right point: 10
For image: frame0047.jpg, evaluation metric for left point: 14, right point: 10
For image: frame0048.jpg, evaluation metric for left point: 36, right point: 13
For image: frame0049.jpg, evaluation metric for left point: 3, right point: 12
For image: frame0050.jpg, evaluation metric for left point: 13, right point: 12
For image: frame0051.jpg, evaluation metric for left point: 10, right point: 8
For image: frame0052.jpg, evaluation metric for left point: 68, right point: 12
For image: frame0053.jpg, evaluation metric for left point: 13, right point: 12
For image: frame0054.jpg, evaluation metric for left point: 15, right point: 14
For image: frame0055.jpg, evaluation metric for left point: 11, right point: 7
For image: frame0056.jpg, evaluation metric for left point: 15, right point: 13
For image: frame0057.jpg, evaluation metric for left point: 16, right point: 13
For image: frame0058.jpg, evaluation metric for left point: 21, right point: 7
For image: frame0059.jpg, evaluation metric for left point: 14, right point: 17
For image: frame0060.jpg, evaluation metric for left point: 14, right point: 7
For image: frame0061.jpg, evaluation metric for left point: 17, right point: 13
For image: frame0062.jpg, evaluation metric for left point: 9, right point: 15
For image: frame0063.jpg, evaluation metric for left point: 19, right point: 13
For image: frame0064.jpg, evaluation metric for left point: 13, right point: 12
For image: frame0065.jpg, evaluation metric for left point: 80, right point: 1
For image: frame0066.jpg, evaluation metric for left point: 35, right point: 0
For image: frame0067.jpg, evaluation metric for left point: 113, right point: 22
For image: frame0068.jpg, evaluation metric for left point: 101, right point: 1
For image: frame0069.jpg, evaluation metric for left point: 81, right point: 26
For image: frame0070.jpg, evaluation metric for left point: 65, right point: 18
For image: frame0071.jpg, evaluation metric for left point: 73, right point: 12
For image: frame0072.jpg, evaluation metric for left point: 77, right point: 26
For image: frame0073.jpg, evaluation metric for left point: 78, right point: 5
For image: frame0074.jpg, evaluation metric for left point: 83, right point: 12
For image: frame0075.jpg, evaluation metric for left point: 86, right point: 15
For image: frame0076.jpg, evaluation metric for left point: 77, right point: 6
For image: frame0077.jpg, evaluation metric for left point: 70, right point: 68
For image: frame0078.jpg, evaluation metric for left point: 56, right point: 8
For image: frame0079.jpg, evaluation metric for left point: 58, right point: 0
For image: frame0080.jpg, evaluation metric for left point: 76, right point: 3
For image: frame0081.jpg, evaluation metric for left point: 72, right point: 3
For image: frame0082.jpg, evaluation metric for left point: 70, right point: 0
For image: frame0083.jpg, evaluation metric for left point: 76, right point: 2
For image: frame0084.jpg, evaluation metric for left point: 76, right point: 8
For image: frame0085.jpg, evaluation metric for left point: 79, right point: 5
For image: frame0086.jpg, evaluation metric for left point: 66, right point: 11
For image: frame0087.jpg, evaluation metric for left point: 69, right point: 7
For image: frame0088.jpg, evaluation metric for left point: 67, right point: 12
For image: frame0089.jpg, evaluation metric for left point: 55, right point: 38
For image: frame0090.jpg, evaluation metric for left point: 61, right point: 5
For image: frame0091.jpg, evaluation metric for left point: 66, right point: 17
For image: frame0092.jpg, evaluation metric for left point: 49, right point: 35
For image: frame0093.jpg, evaluation metric for left point: 56, right point: 10
For image: frame0094.jpg, evaluation metric for left point: 59, right point: 10
For image: frame0095.jpg, evaluation metric for left point: 58, right point: 7
For image: frame0096.jpg, evaluation metric for left point: 50, right point: 10
For image: frame0097.jpg, evaluation metric for left point: 48, right point: 13
For image: frame0098.jpg, evaluation metric for left point: 53, right point: 6
For image: frame0099.jpg, evaluation metric for left point: 49, right point: 13
For image: frame0100.jpg, evaluation metric for left point: 45, right point: 10
For image: frame0101.jpg, evaluation metric for left point: 43, right point: 9
For image: frame0102.jpg, evaluation metric for left point: 40, right point: 8
For image: frame0103.jpg, evaluation metric for left point: 25, right point: 32
For image: frame0104.jpg, evaluation metric for left point: 24, right point: 32
For image: frame0105.jpg, evaluation metric for left point: 20, right point: 36
For image: frame0106.jpg, evaluation metric for left point: 18, right point: 38
For image: frame0107.jpg, evaluation metric for left point: 98, right point: 13
For image: frame0108.jpg, evaluation metric for left point: 13, right point: 35
For image: frame0109.jpg, evaluation metric for left point: 17, right point: 36
For image: frame0110.jpg, evaluation metric for left point: 18, right point: 35
For image: frame0111.jpg, evaluation metric for left point: 12, right point: 36
For image: frame0112.jpg, evaluation metric for left point: 17, right point: 20
For image: frame0113.jpg, evaluation metric for left point: 24, right point: 11
For image: frame0114.jpg, evaluation metric for left point: 25, right point: 10
For image: frame0115.jpg, evaluation metric for left point: 24, right point: 10
For image: frame0116.jpg, evaluation metric for left point: 32, right point: 2
For image: frame0117.jpg, evaluation metric for left point: 13, right point: 5
For image: frame0118.jpg, evaluation metric for left point: 19, right point: 4
For image: frame0119.jpg, evaluation metric for left point: 11, right point: 30
For image: frame0120.jpg, evaluation metric for left point: 8, right point: 23
For image: frame0121.jpg, evaluation metric for left point: 1, right point: 41
For image: frame0122.jpg, evaluation metric for left point: 26, right point: 4
For image: frame0123.jpg, evaluation metric for left point: 14, right point: 3
For image: frame0124.jpg, evaluation metric for left point: 12, right point: 39
For image: frame0125.jpg, evaluation metric for left point: 2, right point: 16
For image: frame0126.jpg, evaluation metric for left point: 9, right point: 17
For image: frame0127.jpg, evaluation metric for left point: 2, right point: 15
For image: frame0128.jpg, evaluation metric for left point: 5, right point: 7
For image: frame0129.jpg, evaluation metric for left point: 9, right point: 8
For image: frame0130.jpg, evaluation metric for left point: 20, right point: 12
For image: frame0131.jpg, evaluation metric for left point: 15, right point: 0
For image: frame0132.jpg, evaluation metric for left point: 24, right point: 9
For image: frame0133.jpg, evaluation metric for left point: 25, right point: 10
For image: frame0134.jpg, evaluation metric for left point: 32, right point: 23
For image: frame0135.jpg, evaluation metric for left point: 14, right point: 28
For image: frame0136.jpg, evaluation metric for left point: 10, right point: 29
For image: frame0137.jpg, evaluation metric for left point: 11, right point: 39
For image: frame0138.jpg, evaluation metric for left point: 13, right point: 37
For image: frame0139.jpg, evaluation metric for left point: 49, right point: 44
For image: frame0140.jpg, evaluation metric for left point: 24, right point: 3
For image: frame0141.jpg, evaluation metric for left point: 9, right point: 3
For image: frame0142.jpg, evaluation metric for left point: 14, right point: 3
For image: frame0143.jpg, evaluation metric for left point: 7, right point: 1
For image: frame0144.jpg, evaluation metric for left point: 64, right point: 67
For image: frame0145.jpg, evaluation metric for left point: 23, right point: 1
For image: frame0146.jpg, evaluation metric for left point: 31, right point: 3
For image: frame0147.jpg, evaluation metric for left point: 25, right point: 3
For image: frame0148.jpg, evaluation metric for left point: 23, right point: 1
For image: frame0149.jpg, evaluation metric for left point: 29, right point: 5
For image: frame0150.jpg, evaluation metric for left point: 24, right point: 0
For input folder: input_1, left RMSE: 29.446335369051727, right RMSE: 12.537410684294692
```
-----------------------------------------------------------------

### Evaluation metric for input 2 folder

```
For image: frame0001.jpg, evaluation metric for left point: 3, right point: 35
For image: frame0002.jpg, evaluation metric for left point: 24, right point: 5
For image: frame0003.jpg, evaluation metric for left point: 18, right point: 6
For image: frame0004.jpg, evaluation metric for left point: 12, right point: 23
For image: frame0005.jpg, evaluation metric for left point: 10, right point: 17
For image: frame0006.jpg, evaluation metric for left point: 10, right point: 16
For image: frame0007.jpg, evaluation metric for left point: 3, right point: 383
For image: frame0008.jpg, evaluation metric for left point: 17, right point: 3
For image: frame0009.jpg, evaluation metric for left point: 18, right point: 11
For image: frame0010.jpg, evaluation metric for left point: 16, right point: 0
For image: frame0011.jpg, evaluation metric for left point: 16, right point: 8
For image: frame0012.jpg, evaluation metric for left point: 16, right point: 7
For image: frame0013.jpg, evaluation metric for left point: 14, right point: 4
For image: frame0014.jpg, evaluation metric for left point: 337, right point: 3
For image: frame0015.jpg, evaluation metric for left point: 15, right point: 1
For image: frame0016.jpg, evaluation metric for left point: 16, right point: 12
For image: frame0017.jpg, evaluation metric for left point: 15, right point: 14
For image: frame0018.jpg, evaluation metric for left point: 340, right point: 25
For image: frame0019.jpg, evaluation metric for left point: 15, right point: 21
For image: frame0020.jpg, evaluation metric for left point: 11, right point: 21
For image: frame0021.jpg, evaluation metric for left point: 15, right point: 19
For image: frame0022.jpg, evaluation metric for left point: 15, right point: 22
For image: frame0023.jpg, evaluation metric for left point: 14, right point: 19
For image: frame0024.jpg, evaluation metric for left point: 13, right point: 19
For image: frame0025.jpg, evaluation metric for left point: 13, right point: 20
For image: frame0026.jpg, evaluation metric for left point: 13, right point: 21
For image: frame0027.jpg, evaluation metric for left point: 15, right point: 14
For image: frame0028.jpg, evaluation metric for left point: 17, right point: 15
For image: frame0029.jpg, evaluation metric for left point: 12, right point: 24
For image: frame0030.jpg, evaluation metric for left point: 13, right point: 20
For image: frame0031.jpg, evaluation metric for left point: 17, right point: 11
For image: frame0032.jpg, evaluation metric for left point: 19, right point: 20
For image: frame0033.jpg, evaluation metric for left point: 17, right point: 19
For image: frame0034.jpg, evaluation metric for left point: 17, right point: 9
For image: frame0035.jpg, evaluation metric for left point: 16, right point: 19
For image: frame0036.jpg, evaluation metric for left point: 16, right point: 19
For image: frame0037.jpg, evaluation metric for left point: 16, right point: 20
For image: frame0038.jpg, evaluation metric for left point: 30, right point: 21
For image: frame0039.jpg, evaluation metric for left point: 31, right point: 17
For image: frame0040.jpg, evaluation metric for left point: 30, right point: 20
For image: frame0041.jpg, evaluation metric for left point: 17, right point: 23
For image: frame0042.jpg, evaluation metric for left point: 15, right point: 22
For image: frame0043.jpg, evaluation metric for left point: 14, right point: 20
For image: frame0044.jpg, evaluation metric for left point: 18, right point: 21
For image: frame0045.jpg, evaluation metric for left point: 16, right point: 7
For image: frame0046.jpg, evaluation metric for left point: 16, right point: 18
For image: frame0047.jpg, evaluation metric for left point: 13, right point: 16
For image: frame0048.jpg, evaluation metric for left point: 15, right point: 20
For image: frame0049.jpg, evaluation metric for left point: 14, right point: 16
For image: frame0050.jpg, evaluation metric for left point: 13, right point: 16
For image: frame0051.jpg, evaluation metric for left point: 18, right point: 21
For image: frame0052.jpg, evaluation metric for left point: 16, right point: 15
For image: frame0053.jpg, evaluation metric for left point: 16, right point: 16
For image: frame0054.jpg, evaluation metric for left point: 13, right point: 23
For image: frame0055.jpg, evaluation metric for left point: 17, right point: 23
For image: frame0056.jpg, evaluation metric for left point: 16, right point: 16
For image: frame0057.jpg, evaluation metric for left point: 29, right point: 18
For image: frame0058.jpg, evaluation metric for left point: 14, right point: 15
For image: frame0059.jpg, evaluation metric for left point: 15, right point: 14
For image: frame0060.jpg, evaluation metric for left point: 11, right point: 14
For image: frame0061.jpg, evaluation metric for left point: 20, right point: 7
For image: frame0062.jpg, evaluation metric for left point: 14, right point: 23
For image: frame0063.jpg, evaluation metric for left point: 29, right point: 23
For image: frame0064.jpg, evaluation metric for left point: 28, right point: 17
For image: frame0065.jpg, evaluation metric for left point: 19, right point: 16
For image: frame0066.jpg, evaluation metric for left point: 29, right point: 12
For image: frame0067.jpg, evaluation metric for left point: 28, right point: 23
For image: frame0068.jpg, evaluation metric for left point: 30, right point: 12
For image: frame0069.jpg, evaluation metric for left point: 33, right point: 8
For image: frame0070.jpg, evaluation metric for left point: 31, right point: 15
For image: frame0071.jpg, evaluation metric for left point: 17, right point: 14
For image: frame0072.jpg, evaluation metric for left point: 17, right point: 10
For image: frame0073.jpg, evaluation metric for left point: 29, right point: 15
For image: frame0074.jpg, evaluation metric for left point: 16, right point: 4
For image: frame0075.jpg, evaluation metric for left point: 29, right point: 16
For image: frame0076.jpg, evaluation metric for left point: 24, right point: 15
For image: frame0077.jpg, evaluation metric for left point: 17, right point: 18
For image: frame0078.jpg, evaluation metric for left point: 20, right point: 10
For image: frame0079.jpg, evaluation metric for left point: 19, right point: 16
For image: frame0080.jpg, evaluation metric for left point: 34, right point: 9
For image: frame0081.jpg, evaluation metric for left point: 18, right point: 13
For image: frame0082.jpg, evaluation metric for left point: 42, right point: 9
For image: frame0083.jpg, evaluation metric for left point: 41, right point: 7
For image: frame0084.jpg, evaluation metric for left point: 43, right point: 7
For image: frame0085.jpg, evaluation metric for left point: 46, right point: 3
For image: frame0086.jpg, evaluation metric for left point: 53, right point: 1
For image: frame0087.jpg, evaluation metric for left point: 49, right point: 1
For image: frame0088.jpg, evaluation metric for left point: 49, right point: 7
For image: frame0089.jpg, evaluation metric for left point: 49, right point: 2
For image: frame0090.jpg, evaluation metric for left point: 53, right point: 7
For image: frame0091.jpg, evaluation metric for left point: 58, right point: 10
For image: frame0092.jpg, evaluation metric for left point: 65, right point: 12
For image: frame0093.jpg, evaluation metric for left point: 68, right point: 11
For image: frame0094.jpg, evaluation metric for left point: 63, right point: 49
For image: frame0095.jpg, evaluation metric for left point: 74, right point: 11
For image: frame0096.jpg, evaluation metric for left point: 72, right point: 14
For image: frame0097.jpg, evaluation metric for left point: 71, right point: 48
For image: frame0098.jpg, evaluation metric for left point: 72, right point: 48
For image: frame0099.jpg, evaluation metric for left point: 78, right point: 49
For image: frame0100.jpg, evaluation metric for left point: 32, right point: 45
For image: frame0101.jpg, evaluation metric for left point: 71, right point: 45
For image: frame0102.jpg, evaluation metric for left point: 69, right point: 49
For image: frame0103.jpg, evaluation metric for left point: 72, right point: 45
For image: frame0104.jpg, evaluation metric for left point: 71, right point: 45
For image: frame0105.jpg, evaluation metric for left point: 67, right point: 53
For image: frame0106.jpg, evaluation metric for left point: 75, right point: 55
For image: frame0107.jpg, evaluation metric for left point: 72, right point: 52
For image: frame0108.jpg, evaluation metric for left point: 73, right point: 54
For image: frame0109.jpg, evaluation metric for left point: 88, right point: 51
For image: frame0110.jpg, evaluation metric for left point: 80, right point: 83
For image: frame0111.jpg, evaluation metric for left point: 71, right point: 52
For image: frame0112.jpg, evaluation metric for left point: 81, right point: 82
For image: frame0113.jpg, evaluation metric for left point: 74, right point: 71
For image: frame0114.jpg, evaluation metric for left point: 51, right point: 76
For image: frame0115.jpg, evaluation metric for left point: 51, right point: 59
For image: frame0116.jpg, evaluation metric for left point: 59, right point: 84
For image: frame0117.jpg, evaluation metric for left point: 44, right point: 57
For image: frame0118.jpg, evaluation metric for left point: 17, right point: 73
For image: frame0119.jpg, evaluation metric for left point: 11, right point: 85
For image: frame0120.jpg, evaluation metric for left point: 19, right point: 8
For image: frame0121.jpg, evaluation metric for left point: 30, right point: 6
For image: frame0122.jpg, evaluation metric for left point: 30, right point: 10
For image: frame0123.jpg, evaluation metric for left point: 23, right point: 11
For image: frame0124.jpg, evaluation metric for left point: 12, right point: 10
For image: frame0125.jpg, evaluation metric for left point: 15, right point: 7
For image: frame0126.jpg, evaluation metric for left point: 13, right point: 3
For image: frame0127.jpg, evaluation metric for left point: 6, right point: 348
For image: frame0128.jpg, evaluation metric for left point: 10, right point: 8
For image: frame0129.jpg, evaluation metric for left point: 11, right point: 1
For image: frame0130.jpg, evaluation metric for left point: 6, right point: 3
For image: frame0131.jpg, evaluation metric for left point: 11, right point: 341
For image: frame0132.jpg, evaluation metric for left point: 0, right point: 2
For image: frame0133.jpg, evaluation metric for left point: 2, right point: 1
For image: frame0134.jpg, evaluation metric for left point: 15, right point: 2
For image: frame0135.jpg, evaluation metric for left point: 18, right point: 7
For image: frame0136.jpg, evaluation metric for left point: 34, right point: 12
For image: frame0137.jpg, evaluation metric for left point: 20, right point: 6
For image: frame0138.jpg, evaluation metric for left point: 12, right point: 7
For image: frame0139.jpg, evaluation metric for left point: 18, right point: 3
For image: frame0140.jpg, evaluation metric for left point: 15, right point: 3
For image: frame0141.jpg, evaluation metric for left point: 10, right point: 4
For image: frame0142.jpg, evaluation metric for left point: 8, right point: 7
For image: frame0143.jpg, evaluation metric for left point: 17, right point: 9
For image: frame0144.jpg, evaluation metric for left point: 19, right point: 11
For image: frame0145.jpg, evaluation metric for left point: 11, right point: 19
For image: frame0146.jpg, evaluation metric for left point: 4, right point: 14
For image: frame0147.jpg, evaluation metric for left point: 3, right point: 13
For image: frame0148.jpg, evaluation metric for left point: 12, right point: 9
For image: frame0149.jpg, evaluation metric for left point: 11, right point: 6
For image: frame0150.jpg, evaluation metric for left point: 7, right point: 5
For input folder: input_2, left RMSE: 37.096405935526064, right RMSE: 40.71261065894284
```

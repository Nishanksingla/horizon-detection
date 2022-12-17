import os
import cv2
import json
import argparse
import numpy as np


import config as config

def parse_args():
    """Parse command line arguments"""

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--input_folder', type=str, required=True, help='Relative or absolute directory path of input images.'
    )
    parser.add_argument(
        '--output_folder', type=str, required=True, help='Relative or absolute directory path to save output images.'
    )

    args = parser.parse_args()
    return args

def edge_detection(img, lower_thres=config.lower_threshold, upper_thres=config.upper_threshold):
    """
    Use Canny edge detection method to detect edges in the image.

    Args:
        img (ndarray): image in the numpy format
        lower_thres (int, optional): lower threshold for the Canny edge detection. Defaults to 100.
        upper_thres (int, optional): upper threshold for the Canny edge detection. Defaults to 120.

    Returns:
        ndarray: image with the detected edges
    """
    edges = cv2.Canny(img, lower_thres, upper_thres)
    
    return edges


def get_left_lines(lines):
    """
    Return the set of lines from the left subset of the image.
    Current input image dimensions are (1080,1920) so this function
    will return the lines in the range less than 500 or 750 or 1000
    This is to detect the left point on the image of the line

    Args:
        lines (ndarray): numpy array of the detected lines

    Returns:
        ndarray: numpy array of the lines on the left side of the image
    """
    for val in [500,750,1000]:
        left_lines = lines[lines[:,:,0]<val]
        if left_lines.shape[0]!=0:
            break
    return left_lines


def get_right_lines(lines):
    """
    Return the set of lines from the right subset of the images.
    Current input image dimensions are (1080,1920) so this function
    will return the lines in the range above than 1500 or 1250 or 1000
    This is to detect the right point on the image of the line

    Args:
        lines (ndarray): numpy array of the detected lines

    Returns:
        ndarray: numpy array of the lines on the right side of the image
    """
    for val in [1500,1250,1000]:
        right_lines = lines[lines[:,:,0]>val]
        if right_lines.shape[0]!=0:
            break
    return right_lines
    
    

def get_lines(edges):
    """
    Find the lines using Hough Lines on the image with edges

    Args:
        edges (ndarray): image with detected edges

    Returns:
        ndarray: 3D numpy array of co-ordinates of the lines (x1, y1, x2, y2).
        The dimension of this array is in the format [<#lines>, 1, <co-ordinates>]
        
    """

    lines = cv2.HoughLinesP(edges, config.rho, config.theta, config.threshold, config.min_line_length, config.max_line_gap)
    return lines

def evaluation():
    pass

def detect_horizon_lines(input_folder, img_filename, output_folder):
    """
    Detect horizon lines and write the image with the horizon line in
    the output folder
    
    Args:
        input_folder(str): path of the input folder
        img_filename(str): name of the image file
        output_folder(str): path of the output folder
    Returns: 
        prediction(dict): prediction dictionary with left and right keys.
    """
    try:
        print("img_filename: {}".format(img_filename))
        img_path = os.path.join(input_folder, img_filename)
        img = cv2.imread(img_path)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        img_blurred = cv2.GaussianBlur(img_gray, ksize=(5,5), sigmaX=0)
        edges = edge_detection(img_blurred)
        lines = get_lines(edges)
        # print("lines: {}".format(lines.shape))

        x1 = 0
        x2 = img_gray.shape[-1] - 1

        left_lines = get_left_lines(lines)
        # print("left_lines: {}".format(left_lines.shape))
        y1 = left_lines[np.argmin(left_lines[:,1], axis=0)][1]

        right_lines = get_right_lines(lines)
        # print("right_lines: {}\n".format(right_lines.shape))
        y2 = right_lines[np.argmin(right_lines[:,3], axis=0)][3]

        cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)
        output_filepath = os.path.join(output_folder, img_filename)
        cv2.imwrite(output_filepath, img)
        prediction = {
            "left": [
                0,
                int(y1)
            ],
            "right": [
                int(x2),
                int(y2)
            ]
        }
        return prediction
    except Exception as exc:
        print("Exception: {} in detecting lines in image: {}\n".format(exc, img_filename))

def main():
    args = parse_args()
    predictions = {}
    input_folder = args.input_folder
    output_folder = args.output_folder

    if input_folder == output_folder:
        return "Input and output folder can not be same."

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    input_images = os.listdir(input_folder)
    for input_img_filename in input_images:
        if input_img_filename.endswith(".jpg"):
            prediction = detect_horizon_lines(input_folder, input_img_filename, output_folder)
            predictions[input_img_filename] = prediction
    
    prediction_output_path = os.path.join(output_folder, "predictions.json")
    with open(prediction_output_path, "w") as f:
        json.dump(predictions, f)


if __name__ == '__main__':
    main()

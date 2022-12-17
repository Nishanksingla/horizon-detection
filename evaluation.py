import os
import json
import argparse
import numpy as np

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

def calculate_distance(true_point, pred_point):
    # true_x, true_y = true_point
    # pred_x, pred_y = left_point

    dist = np.sqrt(np.sum(np.square(np.array(true_point) - np.array(pred_point))))
    
    return int(dist)


def read_json(json_file_path):
    return json.load(open(json_file_path))


def main():
    args = parse_args()
    input_folder = args.input_folder
    output_folder = args.output_folder
    ground_truth_path = os.path.join(input_folder, "ground_truth.json")
    predictions_path = os.path.join(output_folder, "predictions.json")
    if os.path.exists(ground_truth_path) and os.path.exists(predictions_path):
        ground_truths = read_json(ground_truth_path)
        predictions = read_json(predictions_path)

        for img_name, ground_truth in ground_truths.items():
            true_left_point = ground_truth["left"]
            true_right_point = ground_truth["right"]

            prediction = predictions[img_name]
            pred_left_point = prediction["left"]
            pred_right_point = prediction["right"]

            left_point_eval = calculate_distance(true_left_point, pred_left_point)
            right_point_eval = calculate_distance(true_right_point, pred_right_point)

            print("For image: {}, evaluation metric for left point: {}, right point: {}".format(img_name, left_point_eval, right_point_eval))


if __name__ == '__main__':
    main()
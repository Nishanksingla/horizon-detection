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
    dist = np.sqrt(np.sum(np.square(np.array(true_point) - np.array(pred_point))))
    
    return int(dist)

def get_rmse(y_true, y_pred):
    sq_err = np.square(np.array(y_true) - np.array(y_pred))
    rmse = np.sqrt(sq_err.mean())
    return rmse

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
        
        left_gt_points = []
        left_pred_points = []

        right_gt_points = []
        right_pred_points = []
        for img_name, ground_truth in ground_truths.items():
            left_gt_point = ground_truth["left"]
            right_gt_point = ground_truth["right"]

            left_gt_points.append(left_gt_point)
            right_gt_points.append(right_gt_point)

            prediction = predictions[img_name]
            left_pred_point = prediction["left"]
            right_pred_point = prediction["right"]

            left_pred_points.append(left_pred_point)
            right_pred_points.append(right_pred_point)

            left_point_eval = calculate_distance(left_gt_point, left_pred_point)
            right_point_eval = calculate_distance(right_gt_point, right_pred_point)

            print("For image: {}, evaluation metric for left point: {}, right point: {}".format(img_name, left_point_eval, right_point_eval))

        left_rmse = get_rmse(left_gt_points, left_pred_points)
        right_rmse = get_rmse(right_gt_points, right_pred_points)

        print("For input folder: {}, left RMSE: {}, right RMSE: {}".format(input_folder, left_rmse, right_rmse))

if __name__ == '__main__':
    main()
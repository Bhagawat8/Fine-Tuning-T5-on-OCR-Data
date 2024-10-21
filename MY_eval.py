import pandas as pd
import numpy as np

def performance(TP, FP, FN):
    if (TP + FP) == 0:
        precision = float('nan')
    else:
        precision = TP / float(TP + FP)
        
    if (TP + FN) == 0:
        recall = float('nan')
    else:
        recall = TP / float(TP + FN)
    
    if (precision != float('nan')) and (recall != float('nan')):
        f1_score = (2.0 * precision * recall) / (precision + recall) if (precision + recall) != 0 else float('nan')
    else:
        f1_score = float('nan')
    
    return precision, recall, f1_score

def get_dataset_metrics(true_labels, pred_labels):
    metrics_dict = dict()
    
    for true_label, pred_label in zip(true_labels, pred_labels):
        if true_label not in metrics_dict:
            metrics_dict[true_label] = {"TP": 0, "FP": 0, "FN": 0, "Support": 0}
        
        if true_label != "OTHER":
            metrics_dict[true_label]["Support"] += 1
            
            if true_label == pred_label:
                metrics_dict[true_label]["TP"] += 1
            elif pred_label == "OTHER":
                metrics_dict[true_label]["FN"] += 1
        else:
            if pred_label != "OTHER":
                if pred_label not in metrics_dict:
                    metrics_dict[pred_label] = {"TP": 0, "FP": 0, "FN": 0, "Support": 0}
                metrics_dict[pred_label]["FP"] += 1
    
    df = pd.DataFrame()
    
    for field in metrics_dict:
        precision, recall, f1_score = performance(metrics_dict[field]["TP"], metrics_dict[field]["FP"], metrics_dict[field]["FN"])
        support = metrics_dict[field]["Support"]
        
        if field != "OTHER":
            temp_df = pd.DataFrame([[precision, recall, f1_score, support]], 
                                   columns=["Precision", "Recall", "F1-Score", "Support"], index=[field])
            df = pd.concat([df, temp_df])
    
    return df

def get_labels(true_file, pred_file):
    # Load the datasets
    true_df = pd.read_csv(true_file)
    pred_df = pd.read_csv(pred_file)

    # Extract the true and predicted labels
    true_labels = true_df['field'].tolist()
    pred_labels = pred_df['predicted_field'].tolist()

    return true_labels, pred_labels

def evaluate_model(true_file, pred_file, save=False):
    y_true, y_pred = get_labels(true_file, pred_file)

    df = get_dataset_metrics(y_true, y_pred)
    print(df)
    
    if save:
        df.to_csv("eval_metrics.csv", index=True)

if __name__ == "__main__":
    # File paths (update these to your actual file paths)
    true_file = "C:/Users/dell/Documents/Data science/campusX/Assignment_internship/combined_output_true_labels.csv"
    pred_file = "C:/Users/dell/Documents/Data science/campusX\Assignment_internship/test_data_with_ploy_predictions (1).csv"


    evaluate_model(true_file, pred_file, save=True)

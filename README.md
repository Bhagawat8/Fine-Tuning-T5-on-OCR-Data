# T5 Fine-Tuning Project

## Overview

This repository showcases the fine-tuning of the T5 (Text-to-Text Transfer Transformer) model from Hugging Face, specifically the `google-t5/t5-base` version, on custom training data. The project demonstrates the impact of feature engineering on model performance and presents the evaluation metrics obtained from the training process.

## Contents

- **Training Data**: Contains the dataset used for training, including token-level extractions from images.
- **Feature Engineering**: Describes the feature engineering techniques applied to improve model performance.
- **Model Training**: Outlines the training process and the number of epochs run.
- **Evaluation Metrics**: Compares model performance with and without feature engineering.
- **Results**: Displays the results of the evaluation metrics after training.

## Data Description

The dataset comprises token-level extractions from images obtained via Optical Character Recognition (OCR). The data is provided in TSV format with the following columns:

### Training Data (Train)

- **start_index**: The position where the token starts in a single-line representation of the document.
- **end_index**: The position where the token ends in a single-line representation of the document.
- **x_top_left**: X-coordinate of the top-left corner of the token.
- **y_top_left**: Y-coordinate of the top-left corner of the token.
- **x_bottom_right**: X-coordinate of the bottom-right corner of the token.
- **y_bottom_right**: Y-coordinate of the bottom-right corner of the token.
- **transcript**: The OCR extraction of the image.
- **field**: The ground truth label for the transcript.

### Testing Data (Test)

- **start_index**: The position where the token starts in a single-line representation of the document.
- **end_index**: The position where the token ends in a single-line representation of the document.
- **x_top_left**: X-coordinate of the top-left corner of the token.
- **y_top_left**: Y-coordinate of the top-left corner of the token.
- **x_bottom_right**: X-coordinate of the bottom-right corner of the token.
- **y_bottom_right**: Y-coordinate of the bottom-right corner of the token.
- **transcript**: The OCR extraction of the image.

**Note**: The origin (0,0) of the document is the top-left corner of the image, and the y-coordinate increases as we go down the document.

## Feature Engineering

The following feature engineering techniques were applied to enhance the training data:

1. **File Name**: Added the `file_name` column to retain the context of the coordinates in the dataset.
2. **Transcript Length**: Calculated the length of the values in the transcript column and added it as a new feature.
3. **Polynomial Features**: Generated polynomial features of degree 2 on numerical columns, allowing the model to capture non-linear relationships in the data.
4. **Symbol Count**: Counted the number of symbols in the transcript column, adding this as an additional feature.

## Training Process

1. **Initial Training**:
   - The T5 model was fine-tuned on the raw training data without any preprocessing or feature engineering for **2 epochs**.
   - The evaluation metrics from this training are recorded in `eval_metrics_on_model_trained_on_data_without_feature_engineering.csv`.

2. **Feature Engineered Training**:
   - The model was then fine-tuned again on the feature-engineered dataset, leading to significant improvements in the evaluation metrics.
   - Evaluation metrics for this training are available in the repository.

3. **Extended Training**:
   - An additional epoch was run on the last fine-tuned model, resulting in further improvements.
   - Future experiments may include training for up to **6 epochs** to explore potential state-of-the-art results.

## Evaluation Metrics

The evaluation metrics used to assess model performance include:

- **Precision**: The ratio of correctly predicted positive observations to the total predicted positives.
- **Recall**: The ratio of correctly predicted positive observations to all actual positives.
- **F1 Score**: The weighted average of Precision and Recall, useful for imbalanced classes.

The results of the evaluations are contained within the repository. The metrics demonstrate the impact of feature engineering on model performance. Please refer to the respective CSV files for detailed results.

## Conclusion

The experiments conducted in this project illustrate the importance of feature engineering in improving model performance. The T5 model's ability to generalize and predict outputs can be significantly enhanced by incorporating relevant features derived from the training data.

## Future Work

- Extend the training process to 6 epochs to assess the potential for state-of-the-art results.
- Explore additional feature engineering techniques and their impact on model performance.

## Acknowledgments

Special thanks to the Hugging Face community for providing the T5 model and their extensive documentation, which facilitated the training and fine-tuning processes.

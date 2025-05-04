# AI Model Prediction Validator

A Python project to automate the testing of an AI model's predictions, designed for QA professionals to validate AI-driven systems. This project demonstrates skills in Python scripting, AI model evaluation, and test automation—key for future-oriented QA roles in AI projects.

## Project Overview
This script:
- Trains a simple RandomForestClassifier on the Iris dataset using scikit-learn.
- Tests the model's predictions against expected outputs.
- Logs results (pass/fail) in a CSV file and generates a summary report with accuracy metrics.

## Files
- `validate_model.py`: Main script to train, test, and validate the model.
- `model.pkl`: Pre-trained model file.
- `test_results.csv`: Output file with test results (Test ID, Predicted, Actual, Status).
- `summary.txt`: Summary report with total tests, passed tests, and accuracy.

## Setup
1. **Prerequisites**:
   - Python 3.x
   - Install dependencies:
     ```
     pip install scikit-learn pandas
     ```
2. **Run the Script**:
   ```
   python validate_model.py
   ```

## Usage
- The script loads the Iris dataset, trains a model, and tests its predictions.
- Results are saved in `test_results.csv` and a summary in `summary.txt`.
- Sample output in `summary.txt`:
  ```
  Total Tests: 150
  Passed: 144
  Accuracy: 96.00%
  ```

## Why This Project?
- **QA Skills**: Automates validation of AI model outputs, a critical QA task for AI-driven projects.
- **AI Experience**: Shows practical experience with AI model testing, aligning with future job market trends.
- **Portfolio Boost**: Highlights Python scripting and automation, enhancing relevance for QA roles.

## Future Enhancements
- Add support for testing other AI models (e.g., using TensorFlow/PyTorch).
- Integrate with CI/CD pipelines for continuous testing.
- Expand to handle larger datasets and more complex models.

## Contact
Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/darkokostov) for collaboration or hiring opportunities!
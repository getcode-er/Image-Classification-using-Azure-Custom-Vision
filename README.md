# Image-Classification-using-Azure-Custom-Vision
Classify images into 2-3 categories (e.g., Apple, Banana, Orange) using Azure Custom Vision and test prediction via Python

✅ Project: Fruit Image Classification using Azure Custom Vision
🧠 Type: Supervised ML / Computer Vision
🛠️ Tool: Azure Custom Vision
🔤 Categories: Apple, Banana, Orange

🔗 Prerequisites
✅ Microsoft Azure account (free tier is sufficient)
✅ Python installed
✅ customvision SDK installed
✅ Create a Custom Vision Resource on Azure (both Training and Prediction)


💡 Aim to do
1.Set up Azure Custom Vision.

2.Upload training images via Python.

3.Train the model using Azure SDK.

4.Test with new images using Azure Prediction API.

5.Show accuracy + visualize prediction.


✅ STEP 1: Install Required Libraries
          _pip install opencv-python numpy matplotlib scikit-learn_

📁 STEP 2: Project Folder Structure
          _fruit-classification/
│
├── apple/        # 10-15 images of apples
├── banana/       # 10-15 images of bananas
├── orange/       # 10-15 images of oranges
├── test/         # Test images
├── fruit_classifier.py_
You can download free fruit images from : https://www.kaggle.com/moltean/fruits

🧠 STEP 3: Python Code to Train the Classifier

Save this as fruit_classifier.py:


🖼️ STEP 4: Test the Model on New Image
Add this to the same file or create a new script:

python
Copy
Edit

📸 STEP 5: Simulate Dashboard (like Azure Custom Vision)
After training, you'll see:

Classification report (Precision, Recall, F1)

Accuracy

Visual output of prediction with image

# Image-Classification-using-Azure-Custom-Vision
Classify images into 2-3 categories (e.g., Apple, Banana, Orange) using Azure Custom Vision and test prediction via Python

<img width="1688" height="1125" alt="image" src="https://github.com/user-attachments/assets/93fe85e1-14a3-48a8-9465-a4ac4fa9956c" />


✅ Project: _Fruit Image Classification using Azure Custom Vision_

🧠 Type: _Supervised ML / Computer Vision_

🛠️ Tool: _Azure Custom Vision_

🔤 Categories: _Apple, Banana, Orange_

**🔗 Prerequisites**
          
          ✅ Microsoft Azure account (free tier is sufficient)
          ✅ Python installed
          ✅ customvision SDK installed
          ✅ Create a Custom Vision Resource on Azure (both Training and Prediction)


**💡 Aim to do**

          1.Set up Azure Custom Vision.
          2.Upload training images via Python.
          3.Train the model using Azure SDK.
          4.Test with new images using Azure Prediction API.
          5.Show accuracy + visualize prediction.


_**✅ STEP 1: Install Required Libraries**_
         
          _pip install opencv-python numpy matplotlib scikit-learn_

_**📁 STEP 2: Project Folder Structure**_

          _fruit-classification/
          │
          ├── apple/        # 10-15 images of apples
          ├── banana/       # 10-15 images of bananas
          ├── orange/       # 10-15 images of oranges
          ├── test/         # Test images
          ├── _train_fruit_classifier.py_
_You can download free fruit images from : https://www.kaggle.com/moltean/fruits_

_**🧠 STEP 3: Python Code to Train the Classifier**_

          Save the attached _fruit_classifier.py_


_**🖼️ STEP 4: Test the Model on New Image**_
          
          Add this file _**predict_image.py**_ to the same file or create a new script 

_**📸 STEP 5: Simulate Dashboard (like Azure Custom Vision)**_
          
          > After training, you'll see:
          > Classification report (Precision, Recall, F1)
          > Accuracy
          > Visual output of prediction with image

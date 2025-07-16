from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import matplotlib.pyplot as plt
import cv2

# Replace with your Azure details
PREDICTION_KEY = "8b2afda59b6a46b2b119337690ae911f"
ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com/"
PROJECT_ID = "15b80fca-f822-45fb-9220-83c87b1f2592"
PUBLISHED_NAME = "Iteration1"  # Change if yours is named differently

# Authenticate
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-Key": PREDICTION_KEY})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

# Predict function
def predict_image(image_path):
    with open(image_path, "rb") as image_data:
        results = predictor.classify_image(
            project_id=PROJECT_ID,
            published_name=PUBLISHED_NAME,
            image_data=image_data.read()
        )

    # Print top predictions
    print("\nPrediction Results:")
    for prediction in results.predictions:
        print(f"{prediction.tag_name}: {prediction.probability * 100:.2f}%")

    # Show image with predicted tag
    top_prediction = results.predictions[0]
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.title(f"Predicted: {top_prediction.tag_name} ({top_prediction.probability*100:.1f}%)")
    plt.axis('off')
    plt.show()

# Test it!
predict_image("test_apple.jpg")

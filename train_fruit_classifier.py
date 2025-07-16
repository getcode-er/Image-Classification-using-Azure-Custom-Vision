from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from msrest.authentication import ApiKeyCredentials
import os

# Replace with your Azure info
ENDPOINT = "https://<your-region>.api.cognitive.microsoft.com/"  # Example: https://centralindia.api.cognitive.microsoft.com/
TRAINING_KEY = "<your-training-key>"
PROJECT_ID = "<your-project-id>"

# Authenticate
credentials = ApiKeyCredentials(in_headers={"Training-key": TRAINING_KEY})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

# Get your existing project
project = trainer.get_project(PROJECT_ID)

# Create tags (labels for categories)
tags = {
    "apple": trainer.create_tag(project.id, "apple"),
    "banana": trainer.create_tag(project.id, "banana"),
    "orange": trainer.create_tag(project.id, "orange")
}

# Upload images
def upload_images(folder_name, tag_name):
    folder_path = os.path.join(".", folder_name)
    for image_file in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_file)
        with open(image_path, "rb") as image_data:
            trainer.create_images_from_data(project.id, image_data.read(), [tags[tag_name].id])
    print(f"Uploaded images for tag: {tag_name}")

upload_images("apple", "apple")
upload_images("banana", "banana")
upload_images("orange", "orange")

# Train the model
print("Training the model...")
iteration = trainer.train_project(project.id)

# Set this iteration as the default for prediction
trainer.update_iteration(project.id, iteration.id, is_default=True)
print(f"Training completed! Iteration ID: {iteration.id}")

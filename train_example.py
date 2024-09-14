import replicate

training = replicate.trainings.create(
    version="your-model-version",
    input={
        "train_data": "URL_to_your_Hugging_Face_dataset",
        "num_train_epochs": 3
    },
    destination="your-replicate-username/your-model"
)
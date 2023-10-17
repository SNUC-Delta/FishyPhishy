import torch
from PIL import Image
import requests
import torchvision.transforms as transforms
from sklearn.metrics.pairwise import cosine_similarity

from io import BytesIO
import pickle


class Similarity():
    def __init__(self):
        with open("model.pkl", "rb") as f:
            self.model = pickle.load(f)
        with open("extractor.pkl", "rb") as f:
            self.extractor = pickle.load(f)
        with open("hidden_dim.pkl", "rb") as f:
            self.hidden_dim = pickle.load(f)

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

    def get_image_embeddings(self, image_url1, image_url2):
        response1 = requests.get(image_url1)
        image1 = Image.open(BytesIO(response1.content))
        image1 = image1.convert("RGB")
        transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=self.extractor.image_mean, std=self.extractor.image_std),
        ])
        img_tensor1 = transform(image1).unsqueeze(0).to(self.device)

        response2 = requests.get(image_url2)
        image2 = Image.open(BytesIO(response2.content))
        image2 = image2.convert("RGB")
        img_tensor2 = transform(image2).unsqueeze(0).to(self.device)

        with torch.no_grad():
            embeddings1 = self.model(pixel_values=img_tensor1).last_hidden_state[:, 0].cpu().numpy()
            embeddings2 = self.model(pixel_values=img_tensor2).last_hidden_state[:, 0].cpu().numpy()

        embeddings1 = embeddings1.reshape(1, -1)
        embeddings2 = embeddings2.reshape(1, -1)

        similarity = cosine_similarity(embeddings1, embeddings2)[0][0]

        return similarity
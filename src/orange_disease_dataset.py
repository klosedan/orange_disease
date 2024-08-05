from torch.utils.data import Dataset
from PIL import Image
import os
from pathlib import Path


class OrangeDiseaseDataset(Dataset):
    def __init__(self, data_dir, labels, transform=None):
        self.data_dir = data_dir
        self.labels = labels
        self.transform = transform
        self.data = []
        self._load_images()

    def _load_images(self):
        for label in self.labels:
            label_dir = os.path.join(self.data_dir,label)
            [self.data.append((img_path, label)) for ext in ['*.jpg','*.png'] for img_path in Path(label_dir).rglob(ext)]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        img_path, label = self.data[idx]
        image = Image.open(img_path).convert('RGB')
        if self.transform:
            image = self.transform(image)
        label_idx = self.labels.index(label)
        return image, label_idx
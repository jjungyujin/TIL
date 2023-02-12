from pathlib import Path
import torch
from torchvision import datasets, transforms
from torch.utils.data import Dataset
from base import BaseDataLoader
from PIL import Image

class DogBreedsDataset(Dataset):
    def __init__(self, dir_path, transform):
        classes = []
        labels = []
        images = []
        for breed_dir in dir_path.iterdir():
            for jpg_path in breed_dir.glob('*.jpg'):
                label = str(breed_dir).split('/')[-1]
                images.append(jpg_path)
                labels.append(label)
                if label not in classes:
                    classes.append(label)     
        self.transform = transform
        self.data = images
        self.targets = labels
        self.classes = classes
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        img_path, target = self.data[idx], self.targets[idx]
        img = Image.open(img_path)
        if self.transform is not None:
            img = self.transform(img)    
        target = self.classes.index(target)
        target = torch.tensor(target)
        return img, target

class DogBreedsDataLoader(BaseDataLoader):
    def __init__(self, data_dir, batch_size, shuffle=True, validation_split=0.0, num_workers=1, training=True):
        trsfm = transforms.Compose([
            transforms.RandomResizedCrop(224),
            transforms.ToTensor(),
            # transforms.Normalize()
        ])
        self.data_dir = data_dir
        self.dataset = DogBreedsDataset(Path(data_dir), trsfm)
        super().__init__(self.dataset, batch_size, shuffle, validation_split, num_workers)
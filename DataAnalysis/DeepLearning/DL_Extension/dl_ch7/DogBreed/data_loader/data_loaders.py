from pathlib import Path
import torch
from torchvision import datasets, transforms
from torch.utils.data import Dataset
from base import BaseDataLoader
from PIL import Image
from data_loader.cutmix import CutMixCollator

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
    def __init__(self, data_dir, batch_size, shuffle=True, validation_split=0.0, num_workers=1, training=True, trsf_type='train_trsf', use_cutmix=False, cutmix_alpha=1.0):
        if use_cutmix:
            collator = CutMixCollator(cutmix_alpha)
        else :
            collator = torch.utils.data.dataloader.default_collate
        transform_dic = {
            'train_trsf' : transforms.Compose([
                                    transforms.Resize(256),
                                    # transforms.CenterCrop(224),
                                    transforms.RandomResizedCrop(224),
                                    transforms.RandomRotation(30),
                                    transforms.RandomHorizontalFlip(),
                                    transforms.ColorJitter(),
                                    transforms.RandomVerticalFlip(),
                                    transforms.ToTensor(),
                                    transforms.Normalize([0.485, 0.456, 0.406],
                                                        [0.229, 0.224, 0.225])
                                    ]),
            'valid_trsf' : transforms.Compose([
                                    transforms.Resize(255),
                                    transforms.CenterCrop(224),
                                    transforms.ToTensor(),
                                    transforms.Normalize([0.485, 0.456, 0.406],
                                                        [0.229, 0.224, 0.225])
                                    ]),
            'test_trsf' : transforms.Compose([
                                    transforms.Resize(255),
                                    transforms.CenterCrop(224),
                                    transforms.ToTensor(),
                                    transforms.Normalize([0.485, 0.456, 0.406],
                                                        [0.229, 0.224, 0.225])
                                    ]),
        }
        self.data_dir = data_dir
        self.dataset = DogBreedsDataset(Path(data_dir), transform=transform_dic[trsf_type])
        super().__init__(self.dataset, batch_size, shuffle, validation_split, num_workers, collator)
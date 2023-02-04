from pathlib import Path
import torch
from torch.utils.data import Dataset
from torchvision.io import read_image
from torchvision import transforms as transforms
from torchvision import datasets
from base import BaseDataLoader



class MnistDataLoader(BaseDataLoader):
    """
    MNIST data loading demo using BaseDataLoader
    """
    def __init__(self, data_dir, batch_size, shuffle=True, validation_split=0.0, num_workers=1, training=True):
        trsfm = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,))
        ])
        self.data_dir = data_dir
        self.dataset = datasets.MNIST(self.data_dir, train=training, download=True, transform=trsfm)
        super().__init__(self.dataset, batch_size, shuffle, validation_split, num_workers)

class NotMnistDataset(Dataset):
    def __init__(self, dir_path, transform):
        classes = []
        labels = []
        images = []
        for alphabet_dir in dir_path.iterdir():
            for png_path in alphabet_dir.glob('*.png'):
                try:
                    # 데이터 처리 (사전에 처리 후 삭제 / 1회 실행 후 주석 처리)
                    # img = read_image(str(png_path))
                    # img = transforms.ToPILImage()(img.cpu())
                    label = str(alphabet_dir).split('/')[-1]
                    images.append(png_path)
                    labels.append(label)
                    if label not in classes:
                        classes.append(label)
                except:
                    Path(png_path).unlink()
        self.transform = transform
        self.data = images
        self.targets = labels
        self.classes = classes
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        img_path, target = self.data[idx], self.targets[idx]
        # read_image : 이미지 파일을 Tensor로 바꾸나 dtype이 uint8로 설정됨 (transform의 다른 함수를 적용할 수 없음)
        img = read_image(str(img_path))
        # ToPILImage : Tensor type을 PILImage 형태로  변경
        img = transforms.ToPILImage()(img.cpu())
        if self.transform is not None:
            # transform 안의 ToTensor가 PILImage를 Tensor로 다시 변환
            img = self.transform(img)    
        target = self.classes.index(target)
        target = torch.tensor(target)
        return img, target

class NotMnistDataLoader(BaseDataLoader):
    """
    NotMNist data loading demo using BaseDataLoader
    """
    def __init__(self, data_dir, batch_size, shuffle=True, validation_split=0.0, num_workers=1, training=True):
        trsfm = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,))
        ])
        self.data_dir = data_dir
        self.dataset = NotMnistDataset(Path(data_dir), trsfm)
        super().__init__(self.dataset, batch_size, shuffle, validation_split, num_workers)

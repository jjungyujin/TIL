from pathlib import Path
from PIL import Image
from torchvision import datasets, transforms

dir_path = Path('../data/StanfordDogs/Images')

for breed_dir in dir_path.iterdir():
  for jpg_path in breed_dir.glob('*.jpg'):
    try:
      img = Image.open(jpg_path)
      if transforms.ToTensor()(img).shape[0] != 3:
          jpg_path.unlink()
    except:
      jpg_path.unlink()

print("Unlinked unavailable image files !")
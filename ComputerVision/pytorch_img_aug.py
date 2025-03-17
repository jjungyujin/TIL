# %%
import numpy as np
from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt
import albumentations as A


image = Image.open("./datasets/images/cat.jpg")

# %%
transform = transforms.Compose(  # 증강방법을 하나로 묶기
    [
        transforms.Resize(size=(512, 512)),
        transforms.ToTensor(),  # PIL.Image -> Tensor
    ]
)

transformed_image = transform(image)
print(transformed_image.shape)
plt.imshow(transforms.ToPILImage()(transformed_image))
# %%
transform = transforms.Compose(
    [
        transforms.RandomRotation(degrees=30, expand=False, center=None),
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomVerticalFlip(p=0.5),
    ]
)
transformed_image = transform(image)
transformed_image
# %%
transform = transforms.Compose(
    [
        transforms.RandomCrop(size=(512, 512)),
        transforms.Pad(padding=50, fill=127, padding_mode="constant"),
    ]
)

transformed_image = transform(image)
transformed_image
# %%

transform = transforms.Compose(
    [
        transforms.RandomAffine(
            degrees=15, translate=(0.2, 0.2), scale=(0.8, 1.2), shear=15
        )
    ]
)
transformed_image = transform(image)
transformed_image
# %%
transform = transforms.Compose(
    [
        transforms.ColorJitter(brightness=0.3, contrast=0.3, saturation=0.3, hue=0.3),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
        ),  # 정규화 변환은 tensor 형식을 입력으로 받음
        transforms.ToPILImage(),
    ]
)
transformed_image = transform(image)
transformed_image


# %%
transform = A.Compose(
    [
        A.SaltAndPepper(p=0.4, amount=(0.02, 0.06)),
        A.RandomRain(brightness_coefficient=0.8, drop_width=1, blur_value=3, p=1.0),
        A.ToRGB(),
    ]
)

transformed_image = transform(image=np.array(image))["image"]
plt.imshow(transformed_image)

# %%
transform = transforms.Compose(
    [
        transforms.ToTensor(),
        transforms.RandomErasing(p=0.7, value=0),  # RandomErasing : Tensor 형식만 처리
        transforms.RandomErasing(p=0.5, value="random"),
        transforms.ToPILImage(),
    ]
)

transformed_image = transform(image)
transformed_image
# %%

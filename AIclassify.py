import torchvision
import torch
from PIL import Image
import torchvision.transforms as trns
import torch.nn.functional as F


#pretrainmodel = torchvision.models.resnet50(weights='DEFAULT')
pretrainmodel = torchvision.models.efficientnet_b3(weights='DEFAULT')
pretrainmodel.eval()

image_path = r'C:\Users\TSAI\Desktop\cat.jpg'
image = Image.open(image_path).convert("RGB")

transforms = trns.Compose([trns.Resize((300, 300)), trns.ToTensor(), trns.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
image_tensor = transforms(image)
image_tensor = image_tensor.unsqueeze(0)

output = pretrainmodel(image_tensor)

class_path = r'C:\Users\TSAI\Desktop\imagenet_classes.txt'
with open(class_path) as f:
    classes = [line.strip() for line in f.readlines()]

index = torch.argmax(output)
print(classes[index])

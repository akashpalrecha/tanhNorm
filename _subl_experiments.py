import torch
import torch.nn as nn
import torchvision.models as models
from fastai.vision import *

def get_model()->nn.Sequential:
    return models.resnet18()

rnet = get_model().inplanes

m = simple_cnn([3, 16, 64, 8])
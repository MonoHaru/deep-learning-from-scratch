import numpy as np
from PIL import Image

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

def softmax(a):
	c = np.max(a)
	exp_a = np.exp(a-c)
	sum_exp_a = np.sum(exp_a)
	y = exp_a / sum_exp_a
	
	return y

def img_show(img):
	pil_img = Image.fromarray(np.uint8(img))
	pil_img.show()

def mean_squared_error(y, t):
	return 0.5 * np.sum((y-t)**2)

def cross_entropy_error(y, t):
	delta = 1e-7
	return -np.sum(t * np.log(y + delta)) # log0 방지
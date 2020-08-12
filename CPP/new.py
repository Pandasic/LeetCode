def random_brightness(img):
    ifprob<train_parameters['image_distort_strategy']['brightness_prob']:
    brightness_delta=train_parameters['image_distort_strategy']['brightness_delta']
    delta = np.random.uniform(-brightness_delta, brightness_delta) + 1
    img = ImageEnhance.Brightness(img).enhance(delta)
    return img
#增强对比度的函数
def random_contrast(img):
    prob = np.random.uniform(0, 1)
    if prob<train_parameters['image_distort_strategy']['contrast_prob']:
    contrast_delta=train_parameters['image_distort_strategy']['contrast_delta']
    delta = np.random.uniform(-contrast_delta, contrast_delta) + 1
    img = ImageEnhance.Contrast(img).enhance(delta)
    return img
#增强饱和度的函数
    def random_saturation(img):
    prob = np.random.uniform(0, 1)
    if prob<train_parameters['image_distort_strategy']['saturation_prob']:
    saturation_delta=train_parameters['image_distort_strategy']['saturation_delta']
    delta = np.random.uniform(-saturation_delta, saturation_delta) + 1
    img = ImageEnhance.Color(img).enhance(delta)
    return img
#增强色调的函数
def random_hue(img):
    prob = np.random.uniform(0, 1)
    if prob < train_parameters['image_distort_strategy']['hue_prob']:
    hue_delta=train_parameters['image_distort_strategy']['hue_delta']
    delta = np.random.uniform(-hue_delta, hue_delta)
    img_hsv = np.array(img.convert('HSV'))
    img_hsv[:, :, 0] = img_hsv[:, :, 0] + delta
    img = Image.fromarray(img_hsv, mode='HSV').convert('RGB')
    return img


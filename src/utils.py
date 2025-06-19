def preprocess_image(image, target_size=(224, 224)):
    from tensorflow.keras.preprocessing.image import img_to_array, load_img
    image = load_img(image, target_size=target_size)
    image = img_to_array(image)
    image = image / 255.0  # Normalize the image
    return image

def augment_data(image):
    from tensorflow.keras.preprocessing.image import ImageDataGenerator
    datagen = ImageDataGenerator(
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )
    return datagen.flow(image.reshape((1,) + image.shape))
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from keras.callbacks import EarlyStopping, ReduceLROnPlateau

def resize_image(img, size=(20,20)):

    h, w = img.shape[:2]
    
    if h == w: 
        return cv2.resize(img, size, cv2.INTER_AREA)

    dif = h if h > w else w


    if dif > (size[0] + size[1]):
        interpolation = cv2.INTER_AREA
    else:
        interpolation = cv2.INTER_CUBIC

    x_pos = (dif - w)//2
    y_pos = (dif - h)//2

    mask = np.zeros((dif, dif), dtype=img.dtype)
    mask[y_pos:y_pos+h, x_pos:x_pos+w] = img[:h, :w]

    return cv2.resize(mask, size, interpolation)


def get_categories(dir_path):
    categories = []
    for root, subdirectories, files in os.walk(dir_path):
        for subdirectory in subdirectories:
            categories.append(subdirectory)
    
    return categories


def compile_model(model):
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    return model


def earlystop(nbr_patience):
    return EarlyStopping(patience=nbr_patience)


def learning_rate_reduction():
    return ReduceLROnPlateau(monitor='val_acc', patience=2, verbose=1, factor=0.5, min_lr=0.00001)


def train_model(model, epochs, train_generator, validation_generator, callbacks = None):
    return model.fit_generator(train_generator, 
                                epochs=epochs, 
                                validation_data=validation_generator,
                                callbacks = callbacks)


def loss_visualisation(training_loss, training_val_loss):
    plt.plot(training_loss, color='red', label='Training loss')
    plt.plot(training_val_loss,  color='green', label='Validation loss')

    plt.xlabel('Epochs')
    plt.ylabel('Loss')

    plt.legend()

    plt.show()


def accuracy_visualtion(training_accuracy, training_val_accuracy):
    plt.plot(training_accuracy, color='red', label='Training accuracy')
    plt.plot(training_val_accuracy, color='green', label='Validation accuracy')

    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')

    plt.legend()

    plt.show()
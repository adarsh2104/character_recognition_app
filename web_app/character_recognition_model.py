from tensorflow import keras
import cv2
import numpy as np

model = keras.models.load_model('../CSV/model.h5')
def identify_character_class(image_path):
    
    image_size = 200
    X = [] 
    label_verification = {
                        0: '2',
                        1: '9',
                        2: 'adna',
                        3: 'bha',
                        4: 'cha',
                        5: 'daa',
                        6: 'ga',
                        7: 'gha',
                        8: 'gya',
                        9: 'kna',
                        10: 'patalosaw',
                        11: 'petchiryakha',
                        12: 'pha',
                        13: 'ra',
                        14: 'taamatar',
                        15: 'tha',
                        16: 'yaw'
                    }


    image_array = cv2.imread(image_path) 
    image_array = cv2.resize(image_array , (image_size  , image_size) ) 
    X.append(image_array)
    X = np.array(X)
    X = X/255 
    pred  = model.predict_classes(X)

    return label_verification[pred[0]]
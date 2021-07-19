from tensorflow import keras
import cv2
import numpy as np

model = keras.models.load_model('../CSV/model.h5')
def identify_character_class(image_path):
    
    image_size = 200
    X = [] 
    label_verification = {
                        0: '२ / 2',
                        1: '९ / 9',
                        2: 'ण / adna',
                        3: 'भ / bha',
                        4: 'छ / cha',
                        5: 'ड / daa',
                        6: 'ग / ga',
                        7: 'घ / gha',
                        8: 'ज्ञ / gya',
                        9: 'ड़ / kna',
                        10: 'स / patalosaw',
                        11: 'ष / petchiryakha',
                        12: 'फ / pha',
                        13: 'र / ra',
                        14: 'ट / taamatar',
                        15: 'ठ / tha',
                        16: 'य / yaw'
                    }


    image_array = cv2.imread(image_path) 
    image_array = cv2.resize(image_array , (image_size  , image_size) ) 
    X.append(image_array)
    X = np.array(X)
    X = X/255 
    pred  = model.predict_classes(X)

    return label_verification[pred[0]]
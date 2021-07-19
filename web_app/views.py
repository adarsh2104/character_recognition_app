<<<<<<< HEAD
from flask import Flask ,render_template,flash
=======
from flask import Flask ,render_template
>>>>>>> 30b0cfcb7e8576f8df85d25944371578a51e7a15
import os
from flask import request
import base64
from utils import decode_base64
from werkzeug.utils import secure_filename
from character_recognition_model import identify_character_class


app = Flask(__name__,template_folder='./templates', static_folder='./static')
<<<<<<< HEAD
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


=======
>>>>>>> 30b0cfcb7e8576f8df85d25944371578a51e7a15

@app.route("/" ,methods=['GET', 'POST'])
def character_recoginzer():
    if request.method == 'GET':
        return render_template('canvas.html')
    elif request.method == 'POST':
        file = request.files['image']
        file_path,saved = save_uploaded_file(file)
        # saved = True
        # file_path = '/home/adarsh/projects/new_project/kaggle/Kaggle-competitions/Character_Recognition/data_dir/test_file.jpg'
        if saved:
            character_string = identify_character_class(file_path)
<<<<<<< HEAD
            return str(character_string)
=======
            return '<h1>'+str(character_string)+'</h1>'
>>>>>>> 30b0cfcb7e8576f8df85d25944371578a51e7a15
        else:
            return 'Error'    

def save_uploaded_file(file):
    data_dir = '../data_dir/'
    test_file_name = 'test_file.jpg'
    os.makedirs(data_dir, exist_ok=True)

    full_file_path = data_dir+test_file_name
    test_file_name = secure_filename(test_file_name)
    file.save(full_file_path)

    return full_file_path,os.path.exists(full_file_path)



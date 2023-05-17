import os
from flask import send_from_directory
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired
from skimage import io
from skimage.transform import resize
import joblib
import numpy as np
# pylint: disable=C0103


#UPLOAD_FOLDER = 'static/files'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test'
app.config['UPLOAD_FOLDER'] = 'static/files'


class UploadFileForm(FlaskForm):
    file = FileField("Field",validators=[InputRequired()])
    submit = SubmitField("Predict")


@app.route('/', methods=["GET","POST"])
def upload_file():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'static/files',secure_filename(file.filename))
        file.save(file_path)
        message = doPred(file_path)
        return render_template('index.html', form=form, filename=file.filename, value=message)
    return render_template('index.html', form=form)
    
def doPred(file_path):
    temp = []
    img = io.imread(file_path)
    img_resized = resize(img, (100, 100))
    temp.append(img_resized)

    img_resized2 = np.array(temp).reshape(np.array(temp).shape[0], -1)
    
    dict = {"0":"Car","1":"Truck","2":"Bike"}

    loaded_model = joblib.load("random_forest.joblib")
    return dict[str(int(loaded_model.predict(img_resized2)[0]))]


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER']), filename)


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=True, port=server_port, host='0.0.0.0')
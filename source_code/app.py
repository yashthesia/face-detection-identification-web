from flask import Flask, render_template, request, flash, send_from_directory
from flask_uploads import UploadSet,configure_uploads,IMAGES
import subprocess
from subprocess import call
from flask import Flask, render_template, Response
from camera import VideoCamera


app = Flask(__name__)
source = 'usrImg.jpg'
photos = UploadSet('photos', IMAGES)
name = 'Tirth'
app.config['UPLOADED_PHOTOS_DEST'] = './darknet/data/'
configure_uploads(app,photos)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/my-link/')
def my_link():
    print('This is Python Script. Hello T !')
    return '15BCE127 | < Tirth Pandya > 15BCE126 | < Yash Thesia >'


@app.route('/signup.html')
def signup():
    return render_template('signup.html')

@app.route('/signup.php',methods=['GET','POST'])
def signup_php():
    php_out = subprocess.check_output(["php","static/signup.php"])
    return php_out

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/login.php',methods=['GET','POST'])
def login_php():
    php_out = subprocess.check_output(["php", "static/login.php"])
    return php_out

@app.route('/main.html')
def main1():
    return render_template('main.html')


@app.route('/haar-cascades/')
def haar_cascades():
    x = call(["python", "FaceDetection_HaarCascades.py"])
    print('Haar_Cascades Running Successfully.', x)
    return 'Haar_cascades Complete :)'


@app.route('/capture/')
def capture():
    return render_template('capture.html')
    x = call(["python", "FaceDetection_Yolo.py"])
    print('Yolo Running Successfully.')

    return 'Yolo Complete :)'


@app.route('/upload/', methods=['GET','POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        print('Inside def upload')
        filename = photos.save(request.files['photo'])
        print('Photo Saved as ',filename)
        global source
        source= filename
        return render_template('/upload_success.html')
    return render_template('upload.html')

@app.route('/yolo/', methods=['GET','POST'])
def load():
    return render_template('loading.html')




@app.route('/data-gen/')
def data_gen():
        return render_template('generate.html')

@app.route('/gen/', methods=['GET','POST'])
def gen():
    global name
    name = str(request.form['uname'])
    print('The Name from form is : ',name)
    return render_template('gt_loading.html')

@app.route('/data-gen-train/')
def data_gen_train():
        global name
        print("The Name is :", name)
        x = call("python dataGenerator.py "+name, shell=True)
        if x == 0:
            print('Data Generation successful !')
        x = call(["python", "trainer.py"])
        if x == 0:
            print('Training successful !')
        return render_template('training_success.html')


@app.route('/yolo-run/', methods=['GET','POST'])
def yolo_run():
    global source
    x = call(['bash', 'yolo_shell.sh', source])
    if x == 0:
        print('Yolo Run Successful.')
        return render_template('results.html')
    print('Yolo Run Failed.')
    return 'Yolo Run Failed...'

@app.route('/reco-results/', methods=['GET','POST'])
def reco_results():
    return render_template('reco_Loading.html')

@app.route('/recognize/', methods=['GET','POST'])
def recognize():
    global source
    x = call(['python', 'FaceRecognizer.py'])
    if x == 0:
        print('Recognition Successful !')
        return render_template('recognizer.html')
    print('Recognition Failed !')
    return 'Recog Failed.'


# @app.route('about')
# def about():

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
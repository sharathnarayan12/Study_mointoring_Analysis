from flask import Flask, render_template, Response
from Detection_Algo import HolisticDetection
app = Flask(__name__)

detection= HolisticDetection()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(detection.run_detection(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/reading')
def reading():
    detection.Reading_print()

@app.route('/not_reading')
def not_reading():
    detection.Not_Reading_print()
   
if __name__ == "__main__":
    app.run(host='0.0.0.0',port='9090', debug=True)
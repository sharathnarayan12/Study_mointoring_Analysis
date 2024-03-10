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

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5000', debug=True)
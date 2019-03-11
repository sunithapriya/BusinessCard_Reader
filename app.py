from package import *
import readCard
app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def trial():
    if str(request.method) == str('POST'):
        try:
            query_file = request.files['card']
        except:
            query_file = request.files['card1']
        #filename = secure_filename(query_file.filename)
        print "************"
        img = cv2.imdecode(np.fromstring(query_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        text, url = readCard.detectText(img)
        return render_template('index.html', text=text, link=url)

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=8001, debug=True)

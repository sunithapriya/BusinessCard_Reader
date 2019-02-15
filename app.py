from package import *
import readCard
app = Flask(__name__)
CORS(app) 




@app.route("/")     
def index():
    return render_template("index.html") 


@app.route("/predict", methods=['POST'])     
def trial():
    link_to_save = "/home/desktop-su-02/Documents/PPT/static" 
    if str(request.method)==str('POST'): 
        try:       
            query_file=request.files['card']
        except:
            query_file=request.files['card1']
        filename = secure_filename(query_file.filename) 

        print(filename)
        print("************")
        img = cv2.imdecode(np.fromstring(query_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        text,url=readCard.detectText(img)
        

       

        # if not filename.endswith(".pptx"):
        #     print("Fail")
        #     trades_output="File must be in pptx format."
        #     return render_template('index.html',datas=trades_output, filename=filename ) #,data=top_resume
        # else:
        #     path=save_path.get_path()
            
        #     link_to_save+="/"+path
        #     query_file.save(os.path.join(link_to_save,filename))
        #     query = str(link_to_save)+"/"+str(filename)
        #     filename=request.files['ppt_file'].filename
        #     code = str(path).split("_")[-1]

        #     filename="Sucess"
            # return render_template('index.html',filename=filename,code=code)

        # filename="Sucess"
        # return render_template('index.html',filename=filename)
        return render_template('index.html',text=text,link=url)

   

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=8003,debug=True)

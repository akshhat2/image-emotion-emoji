from flask import *
from werkzeug.wrappers import Request, Response
from werkzeug.utils import secure_filename
import os
# from flask_caching import Cache
import predict

app = Flask(__name__) 
i=1
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0.002

@app.route('/')     ##Home Page 
def test(): 
    return render_template('test.html') 
@app.route('/next') 
def next(): ##Result Page; after Uploading the Image
    return render_template('next.html')
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():  ##Uploading Function
    #############
    # NO-cache shoul be stored by the browser


    resp=Response()
    resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    resp.headers["Pragma"] = "no-cache"
    resp.headers["Expires"] = "0"
    #############

    if request.method == 'POST':
        f= request.files['pic']      ##Importing image from the webpage by mentioning the 'id'
        print(f)
        print(request.files)

        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        try:
            os.remove(os.path.join(THIS_FOLDER,'static','css','temp5.jpg'))
        except:
            print("No file")
        f.save(os.path.join(THIS_FOLDER,'static','css',secure_filename("temp5.jpg")))
        message=(predict.predict(f))
        emotion_dict = {0: "   Angry   ", 1: "Disgusted", 2: "  Fearful  ", 3: "   Happy   ", 4: "  Neutral  ", 5: "    Sad    ", 6: "Surprised"}
        emoji_dist={0:"/static/emojis/angry.jpg",2:"/static/emojis/disgusted.jpg",2:"/static/emojis/fearful.jpg",3:"/static/emojis/happy.jpg",4:"/static/emojis/neutral.jpg",5:"/static/emojis//sad.jpg",6:"/static/emojis/surpriced.jpg"}
        print(message)
        # message=message.capitalize()    
        # f.save("/static/"+f.filename)
        print(THIS_FOLDER)
    return render_template("next.html",message=emotion_dict[message],source=emoji_dist[message],ttt=os.path.join(THIS_FOLDER,emoji_dist[message]))
# @app.route('/about/') def about(): return render_template('about.html') 
if __name__ == '__main__': 
    app.run(debug=True)
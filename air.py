from flask import Flask
from flask import request
# from pymongo import MongoClient
app = Flask(__name__)

# client = MongoClient('localhost:27017')
# db=client.air_data

print("done establishing connection!")

@app.route('/sensor',methods = ['POST', 'GET'])
def sensor():
   if request.method == 'POST':
        # print (request.is_json)
        content = request.json
        print(content)
#         db.air_datas.insert_one(content)
#         fivestar = db.sensor_datas.find()
#         print(fivestar)
        return "done"
   else:
        return "error"
@app.route('/',methods = ['GET'])
def index():
   return "done"
  
@app.route('/val/<co>/<dust>',methods = ['GET'])
def val(co=None,dust=None):
	print(co+" "+dust)	
	db.air_datas.insert_one({'co': co,'dust':dust})
	return co+" "+dust
	
@app.route('/<area>',methods = ['GET'])
def val(area=None):
	print(area)	
	#db.air_datas.insert_one({'co': co,'dust':dust})
	
	return "{'co':'211','du':'211'}"
	


if __name__ == "__main__":
    app.run()

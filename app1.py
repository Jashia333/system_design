from flask import request,jsonify,Flask

app1=Flask(__name__)
CACHE={}

@app1.put("/cache")
def put_values():
    data=request.get_json(force=True)
    for k,v in data.items():
        CACHE[k]=v
    

    if data is None:
        return jsonify(error="Bad Request"),400

    
    return jsonify(key=list(data.keys()), stored=True)

@app1.get("/cache/<key>")
def get_key(key):
    if key not in CACHE:
        return jsonify(error="Key doesn't exists"),400
    return jsonify(request_key=key, value=CACHE[key])

@app1.get("/cache/_size")
def get_size():
    return jsonify(keys_length=len(CACHE))

@app1.get("/cache/_show")
def show_cache():
    return jsonify(data=CACHE)

if __name__=="__main__":
    app1.run(host="0.0.0.0", port=9000,debug=True)
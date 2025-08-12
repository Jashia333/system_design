from flask import request,jsonify,Flask
import time

app1=Flask(__name__)
CACHE={}

@app1.put("/cache")
def put_values():
    data=request.get_json(force=True)
    now=time.time()
    for k,v in data.items():
        val,ttl=v["data"],v["ttl"]
        ttl=now+float(ttl)
        CACHE[k]=(val,ttl)
    
    if data is None:
        return jsonify(error="Bad Request"),400

    
    return jsonify(key=list(data.keys()), stored=True)

@app1.get("/cache/<key>")
def get_key(key):
    clear_cache()
    if key not in CACHE:
        return jsonify(error="Key doesn't exists"),400
    time_left=CACHE[key][1]-time.time() 
    
    return jsonify(data=CACHE[key][0], time_remaining=f"{time_left:0.2f}")

@app1.get("/cache/size")
def get_size():
    # This line REBUILDS the cache with only the valid items, effectively deleting the expired ones.

    clear_cache()
    return jsonify(keys_length=len(CACHE))

@app1.get("/cache/show")
def show_cache():
    # This line REBUILDS the cache with only the valid items, effectively deleting the expired ones.
    clear_cache()
    return jsonify(data=CACHE)

def clear_cache():
    now=time.time()
    val_del=[k for k,v in CACHE.items() if v[1]<time.time() ]
    for val in val_del:
        del CACHE[val]

if __name__=="__main__":
    app1.run(host="0.0.0.0", port=9000,debug=True)
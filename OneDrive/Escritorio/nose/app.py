from flask import request
from flask import Flask
app = Flask(__name__)
Cubes = [
    {
        "name": "MyCubes",
        "items": [
            {
                "name": "mirrow",
                "price": 100
            }
        ]
    }
]

@app.get("/cube")
def get_cube():
    return {"Cubes": Cubes}


@app.post("/cube")
def create_cubes():
    request_data = request.get_json()
    new_cube = {"name": request_data["name"], "items": []}
    Cubes.append(new_cube)
    return new_cube, 201


@app.post("/cube/<string:name>/items")
def create_item(name):
    request_data = request.get_json()
    for cube in Cubes:
        if cube["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            cube["items"].append(new_item)
            return new_item, 201
    return {"message": "Cube not found"}, 404


@app.get("/cube/<string:name>")
def get_store(name):
    for cube in Cubes:
        if cube["name"] == name:
            return cube
    return {"message": "Cube not found"}, 404


@app.get("/cube/<string:name>/items")
def get_item_in_cubes(name):
    for Cubes in Cubes:
        if Cubes["name"] == name:
            return {"items": Cubes["items"]}
    return {"message": "Cube not found"}, 404
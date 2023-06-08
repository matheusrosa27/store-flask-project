from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "id": 1,
        "name": "Amazon Brazil",
        "items": [
            {
                "name": "PS5 Digital Edition - God of War Ragnarok Edition",
                "price": 3999.90,
                "quantity": 23,
                "imgUrl": "https://cdn.awsli.com.br/600x1000/1258/1258259/produto/175150262/playstation-5-digital-45ae12d606.jpg",
                "description": "Play has no limits!"
            }
        ]
    },
    {
        "id": 2,
        "name": "Americanas",
        "items": [
            {
                "name": "PS5 Digital Edition - God of War Ragnarok Edition",
                "price": 3999.90,
                "quantity": 23,
                "imgUrl": "https://cdn.awsli.com.br/600x1000/1258/1258259/produto/175150262/playstation-5-digital-45ae12d606.jpg",
                "description": "Play has no limits!"
            },
            {
                "name": "Kit-Kat 41,5g",
                "price": 2.49,
                "quantity": 5320,
                "imgUrl": "https://lojasantoantonio.vtexassets.com/arquivos/ids/165175/Chocolate-Kitkat-415G-NESTLE.jpg?v=1768327518",
                "description": "Have a break. Have a Kit-Kat!"
                
            }
        ]
    }
]

@app.get('/store')
def get_store():
    return stores, 200

@app.post('/store')
def create_store():
    request_data = request.get_json()
    requiredFields = ['id', 'name', 'items']
    if all(field in request_data.keys() for field in requiredFields):
        newStore = {
            "id": request_data["id"],
            "name": request_data["name"],
            "items": request_data["items"]
        }
    else:
        return {"message": "Error adding store."}, 400
        
    allowInsert = False
    for store in stores:
        if newStore["name"] == store['name'] or newStore["id"] == store["id"]:
            allowInsert = False
            break
        else:
            allowInsert = True
            
    if allowInsert:
        stores.append(newStore)
        return newStore, 201
    else:
        return {"message": "Store already exists!"}, 409
    
@app.post('/store/<string:store_id>/item')
def insert_item(store_id):
    pass
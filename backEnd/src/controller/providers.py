from flask import request
from src.model.providers import ProviderDAO

def search():
    query = request.args.get("s", "")
    page = request.args.get("page", 0, type=int)
    data = ProviderDAO.findByName(query, int(page))
    if data != None: 
        data = [x.to_dict() for x in data]
        return data
    return {"msg": "Nao foram encontrados dados"}
        

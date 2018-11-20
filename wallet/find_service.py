# coding=utf_8

import utils.mongo as db
import utils.errors as error
import re


def getFundsWallet(user_id):
    """
    Busca la cantidad de dinero disponible de la billetera de un usuario.\n
    user_id string usuario a buscar
    """
    """
    @api {get} /v1/wallet/:user_id/ Consultar fondos
    @apiName Consultar fondos
    @apiGroup Wallet
    @apiDescription Consulta los fondos de una billetera de usuario

    @apiSuccessExample {json} Respuesta
        HTTP/1.1 200 OK
            {
                "user_id": "{id de usuario}"
                "balance": "{cantidad de dinero}"
            }

    @apiUse Errors
    """
    try:
       # regx = re.compile(text, re.IGNORECASE)
        result = 0

        cursor = db.transaction.aggregate({ 
            "$match": {
                "$and": [
                    { "to_user_id": user_id }
                ]} 
            },
            {"$group": { 
                "_id" : null, 
                "sum ": 
                    { "$sum": "$amount" } 
                } 
            })

        result = result + cursor["amount"]
        
        cursor = db.transaction.aggregate({ 
            "$match": {
                "$and": [
                    { "from_user_id": user_id }
                ]} 
            },
            {"$group": { 
                "_id" : null, 
                "sum ": 
                    { "$sum": "$amount" } 
                } 
            })

        result = result - cursor["amount"]

        
        return result
    except Exception:
        raise error.InvalidRequest("Invalid criteria")

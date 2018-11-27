# coding=utf_8

import utils.mongo as db
import utils.errors as error


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

        funds = 0
        """
        results = []

        cursor = db.articles.find({
            "$and": [{
                "to_user_id": bson.ObjectId(user_id)
            }]
        })

        for doc in cursor:
            results.append(doc)

        for item in results:
            funds = funds + item["amount"]

        """
        cursor = db.transaction.aggregate({ 
            '$match': {
                '$and': [
                    { 'to_user_id': bson.ObjectId(user_id) }
                ]} 
            },
            {'$group': { 
                '_id' : null, 
                'sum': 
                    { '$sum': '$amount' } 
                } 
            })

        funds = funds + cursor["sum"]

        
        cursor = db.transaction.aggregate({ 
            '$match': {
                '$and': [
                    { 'from_user_id': bson.ObjectId(user_id) }
                ]} 
            },
            {'$group': { 
                '_id' : null, 
                'sum': 
                    { '$sum': '$amount' } 
                } 
            })

        funds = funds - cursor['sum']
        

        return funds
    except Exception:
        raise error.InvalidRequest("Invalid criteria")

def getHistoryWallet(params, user_id):
    """
    Busca transacciones en un rango de fechas.\n
    user_id string usuario a buscar
    """
    """
    @api {get} /v1/wallet/:user_id/history Consultar transacciones en rango de fechas
    @apiName Consultar transacciones
    @apiGroup Wallet
    @apiDescription Consulta de las transacciones de una billetera de usuario en un rango de fechas

    @apiSuccessExample {json} Respuesta
        HTTP/1.1 200 OK
        {
            "_id": "{id de Transaccion}"
            "amount": "{importe}",
            "datetime": "{fecha y hora de creacion}",
            "observation": "{observacion de la transaccion}",
            "type": "{tipo de transaccion}",
            "to_user_id": {Para cual usuario},
            "from_user_id": {Desde cual usuario}
        }

    @apiUse Errors
    """
    try:

        results = []

        """
        cursor = db.transaction.find({
                "$or": [{
                    "from_user_id": bson.ObjectId(user_id)
                }, {
                    "to_user_id": bson.ObjectId(user_id)
                }], 
                "datetime": {
                    "$gte": ISODate(params["date_since"]), 
                    "$lte": ISODate(params["date_until"])
                }
        })
        """
        cursor = db.transaction.find({})

        for doc in cursor:
            results.append(doc)
    except Exception:
        raise error.InvalidRequest("Invalid criteria")
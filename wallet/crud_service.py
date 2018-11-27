# coding=utf_8

import utils.mongo as db
import utils.errors as error
import bson.objectid as bson
import datetime
import wallet.transaction_schema as schema


def addDeposit(params, user_id):
    """
    Agrega un deposito.\n
    params: dict<propiedad, valor> Transaccion\n
    return dict<propiedad, valor> Transaccion
    """
    """
    @api {post} /v1/wallet Crear un deposito
    @apiName Crear Transaccion
    @apiGroup Wallet

    @apiUse AuthHeader

    @apiExample {json} Body
        {
            "amount": "{importe}",
            "observation": "{observacion de la transaccion}",
            "type": "{tipo de transaccion}",
            "to_user_id": {Para cual usuario},
            "from_user_id": {Desde cual usuario}
        }

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

    transaction = schema.newDeposit(user_id)

    # Actualizamos los valores validos a actualizar
    transaction.update(params)

    schema.validateSchema(transaction)

    transaction["_id"] = db.transaction.insert_one(transaction).inserted_id

    return transaction

def addWithdraw(params, user_id):
    """
    Agrega un retiro.\n
    params: dict<propiedad, valor> Transaccion\n
    return dict<propiedad, valor> Transaccion
    """
    """
    @api {post} /v1/wallet Crear un retiro
    @apiName Crear Transaccion
    @apiGroup Wallet

    @apiUse AuthHeader

    @apiExample {json} Body
        {
            "amount": "{importe}",
            "observation": "{observacion de la transaccion}",
            "type": "{tipo de transaccion}",
            "to_user_id": {Para cual usuario},
            "from_user_id": {Desde cual usuario}
        }

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

    transaction = schema.newWithdraw(user_id)

    # Actualizamos los valores validos a actualizar
    transaction.update(params)

    schema.validateSchema(transaction)

    transaction["_id"] = db.transaction.insert_one(transaction).inserted_id

    return transaction

def addSend(params, user_id):
    """
    Agrega un Envio de fondos.\n
    params: dict<propiedad, valor> Transaccion\n
    return dict<propiedad, valor> Transaccion
    """
    """
    @api {post} /v1/wallet Crear un Envio de fondos
    @apiName Crear Transaccion
    @apiGroup Wallet

    @apiUse AuthHeader

    @apiExample {json} Body
        {
            "amount": "{importe}",
            "observation": "{observacion de la transaccion}",
            "type": "{tipo de transaccion}",
            "to_user_id": {Para cual usuario},
            "from_user_id": {Desde cual usuario}
        }

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

    transaction = schema.newSend(user_id)

    # Actualizamos los valores validos a actualizar
    transaction.update(params)

    schema.validateSchema(transaction)

    transaction["_id"] = db.transaction.insert_one(transaction).inserted_id

    return transaction

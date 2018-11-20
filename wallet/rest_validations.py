# coding=utf_8
# Son las validaciones de los servicios rest, se validan los parametros obtenidos desde las llamadas externas rest

import utils.errors as error
import wallet.crud_service as crud
import utils.schema_validator as schemaValidator
import numbers


# Son validaciones sobre las propiedades que pueden actualizarse desde REST
TRANSACTION_UPDATE_SCHEMA = {
    "observation": {
        "type": str,
        "maxLen": 2048
        },
    "amount": {
        "type": numbers.Real,
        "min": 0
        },
    "stock": {
        "type": numbers.Integral,
        "min": 0
        }
}


def validateWalletParams(params):
    """
    Valida los parametros para crear un objeto.\n
    params: dict<propiedad, valor> Article
    """
    if ("_id" in params):
        raise error.InvalidArgument("_id", "Inválido")

    return schemaValidator.validateAndClean(ARTICLE_UPDATE_SCHEMA, params)


def validateEditWalletParams(articleId, params):
    """
    Valida los parametros para actualizar un objeto.\n
    params: dict<propiedad, valor> Article
    """
    if (not articleId):
        raise error.InvalidArgument("_id", "Inválido")

    return schemaValidator.validateAndClean(TRANSACTION_UPDATE_SCHEMA, params)


def validateWalletFunds(user_id):
    wallet = crud.getFunds(user_id)
    if(wallet["balance"] == 0):
        raise error.InvalidArgument("_id", "Without funds")

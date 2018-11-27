# coding=utf_8

import numbers
import datetime
import utils.schema_validator as validator
import utils.errors as errors

# Validaciones generales del esquema, se valida solo lo que el usuario puede cambiar
TRANSACTION_DB_SCHEMA = {
    "amount": {
        "required": True,
        "type": numbers.Real,
        "min": 0
        },
    "description": {
        "required": False,
        "type": str,
        "maxLen": 2048
        },
    "type": {
        "required": True,
        "type": str,
        "minLen": 1,
        "maxLen": 12
        },
    "to_user_id": {
        "required": False,
        "type": str,
        "minLen": 22,
        "maxLen": 26
        },
    "from_user_id": {
        "required": False,
        "type": str,
        "minLen": 22,
        "maxLen": 26
        }
}


def newDeposit(user_id):
    """
    Crea un nuevo deposito en blanco.\n
    return dict<propiedad, valor> Wallet
    """

    return {
        "amount": 0.0,
        "datetime": datetime.datetime.utcnow(),
        "observation": "",
        "type": "",
        "to_user_id": user_id
    }

def newWithdraw(user_id):
    """
    Crea un nuevo retiro en blanco.\n
    return dict<propiedad, valor> Wallet
    """

    return {
        "amount": 0.0,
        "datetime": datetime.datetime.utcnow(),
        "observation": "",
        "type": "",
        "from_user_id": user_id
    }

def newSend(user_id):
    """
    Crea un nuevo retiro en blanco.\n
    return dict<propiedad, valor> Wallet
    """

    return {
        "amount": 0.0,
        "datetime": datetime.datetime.utcnow(),
        "observation": "",
        "type": "",
        "to_user_id": "",
        "from_user_id": user_id
    }

def validateSchema(document):
    err = validator.validateSchema(TRANSACTION_DB_SCHEMA, document)

    if (len(err) > 0):
        raise errors.MultipleArgumentException(err)
# coding=utf_8

import utils.schema_validator as validator
import utils.errors as errors

# Validaciones generales del esquema, se valida solo lo que el usuario puede cambiar
WALLET_DB_SCHEMA = {
    "user_id": {
        "required": True,
        "type": str,
        "minLen": 1,
        "maxLen": 32
        },
    "wallet_id": {
        "required": False,
        "type": str,
        "maxLen": 32
        },
}

def validateSchema(document):
    err = validator.validateSchema(WALLET_DB_SCHEMA, document)

    if (len(err) > 0):
        raise errors.MultipleArgumentException(err)

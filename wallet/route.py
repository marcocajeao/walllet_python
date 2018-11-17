# coding=utf_8

import flask
# import articles.crud_service as crud
# import articles.find_service as find
import utils.json_serializer as json
import utils.errors as errors
# import utils.security as security
# import articles.rest_validations as restValidator


def init(app):
    """
    Inicializa las rutas para Wallet\n
    app: Flask
    """

    @app.route('/v1/wallet/<user_id>/deposit', methods=['POST'])
    def addWallet(user_id):
        try:
            # security.validateAdminRole(flask.request.headers.get("Authorization"))

            # params = json.body_to_dic(flask.request.data)

            # params = restValidator.validateAddArticleParams(params)

            # result = crud.addArticle(params)

            return json.dic_to_json({
                "wallet": 2,
                "user_id": user_id
            })
        except Exception as err:
            return errors.handleError(err)

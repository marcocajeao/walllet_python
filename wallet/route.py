# coding=utf_8

import flask
import numbers
# import articles.crud_service as crud
import wallet.find_service as find
import utils.json_serializer as json
import utils.errors as errors
import utils.security as security
# import articles.rest_validations as restValidator


def init(app):
    """
    Inicializa las rutas para Wallet\n
    app: Flask
    """

    @app.route('/v1/wallet/<user_id>/deposit', methods=['POST'])
    def deposit(user_id):
        try:
            security.validateAdminRole(flask.request.headers.get("Authorization"))

            params = json.body_to_dic(flask.request.data)

            # params = restValidator.validateAddArticleParams(params)

            # result = find.addArticle(params)

            return json.dic_to_json({
                "_id": "0xasd564wes4daSDx5165as5d4da65WKJsd44s",
                "to_user_id": "4daSDx5165as5d4da65WKJ" ,
                "amount": params["amount"],
                "date": "2018-11-17",
                "time": "17:46:45.009",
                "observation": params["observation"]
            })
        except Exception as err:
            return errors.handleError(err)

    @app.route('/v1/wallet/<user_id>/withdraw', methods=['POST'])
    def withdraw(user_id):
        try:
            security.validateAdminRole(flask.request.headers.get("Authorization"))

            params = json.body_to_dic(flask.request.data)

            # params = restValidator.validateAddArticleParams(params)

            # result = crud.addArticle(params)

            return json.dic_to_json({
                "_id": "0x5WKJsd44asd5es4daSDx5165a64ws5d4dAAs",
                "amount": params["amount"],
                "date": "2018-11-18",
                "time": "08:16:25.058",
                "observation": params["observation"]
            })
        except Exception as err:
            return errors.handleError(err)

    @app.route('/v1/wallet/<user_id>', methods=['GET'])
    def getFunds(user_id):
        try:
            security.validateAdminRole(flask.request.headers.get("Authorization"))

            params = json.body_to_dic(flask.request.data)

            # params = restValidator.validateAddArticleParams(params)

            result = find.getFundsWallet(user_id)

            return json.dic_to_json({
                "user_id": user_id,
                "balance": result
            })
        except Exception as err:
            return errors.handleError(err)

    @app.route('/v1/wallet/<user_id>/send', methods=['POST'])
    def sendFunds(user_id):
        try:
            security.validateAdminRole(flask.request.headers.get("Authorization"))

            params = json.body_to_dic(flask.request.data)

            # params = restValidator.validateAddArticleParams(params)

            # result = crud.addArticle(params)

            return json.dic_to_json({
                "_id": "0x5WKJsGFT3456G548sdsdkSD64ws5d4G5d4dsJ",
                "amount": params["amount"],
                "from_user_id": user_id,
                "to_user_id": "0x5W8sdsdkSDKJsGFT3456G5464w",
                "date": "2018-11-19",
                "time": "11:25:35.958",
                "observation": params["observation"]
            })
        except Exception as err:
            return errors.handleError(err)

    @app.route('/v1/wallet/<user_id>/history', methods=['POST'])
    def getHistory(user_id):
        try:
            security.validateAdminRole(flask.request.headers.get("Authorization"))

            params = json.body_to_dic(flask.request.data)

            # params = restValidator.validateAddArticleParams(params)

            # result = crud.addArticle(params)

            return json.dic_to_json({
                "_id": "0x5WKJsGFT3456G548sdsdkSD64ws5d4G5d4dsJ",
                "amount": 985.85,
                "from_user_id": user_id,
                "to_user_id": "0x5W8sdsdkSDKJsGFT3456G5464w",
                "date": "2018-11-19",
                "time": "11:25:35.958",
                "observation": params["observation"]
            })
        except Exception as err:
            return errors.handleError(err)
# coding=utf_8

import flask
import wallet.crud_service as crud
import wallet.find_service as find
import utils.json_serializer as json
import utils.errors as errors
import utils.security as security


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

            result = crud.addDeposit(params, user_id)

            return json.dic_to_json(result)
        except Exception as err:
            return errors.handleError(err)

    @app.route('/v1/wallet/<user_id>/withdraw', methods=['POST'])
    def withdraw(user_id):
        try:
            security.validateAdminRole(flask.request.headers.get("Authorization"))

            params = json.body_to_dic(flask.request.data)

            result = crud.addWithdraw(params, user_id)

            return json.dic_to_json(result)
        except Exception as err:
            return errors.handleError(err)

    @app.route('/v1/wallet/<user_id>', methods=['GET'])
    def getFunds(user_id):
        try:
            security.validateAdminRole(flask.request.headers.get("Authorization"))

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

            result = crud.addSend(params, user_id)

            return json.dic_to_json(result)
        except Exception as err:
            return errors.handleError(err)

    @app.route('/v1/wallet/<user_id>/history', methods=['POST','GET'])
    def getHistory(user_id):
        try:
            security.validateAdminRole(flask.request.headers.get("Authorization"))

            params = json.body_to_dic(flask.request.data)

            result = find.getHistoryWallet(params, user_id)

            return json.dic_to_json(result)
        except Exception as err:
            return errors.handleError(err)
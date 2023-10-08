from flask import Blueprint, jsonify, redirect, request, url_for

import traceback

# Logger
from src.utils.Logger import Logger
from src.utils.Security import Security

main = Blueprint('index_blueprint', __name__)


@main.route('/')
def index():
    has_access = Security.verify_token(request.headers)

    if has_access:
                      
        return "ok"
    
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401

   
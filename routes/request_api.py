"""The Endpoints to manage the Delivery Service API"""
import json
from flask import jsonify, abort, request, Blueprint
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

REQUEST_API = Blueprint('request_api', __name__)

# Init firestore service account
cred = credentials.Certificate(
    'delivery-biz-firebase-adminsdk-f8kue-afc933be68.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API


def is_json(myjson):
    try:
        json_object = json.dumps(myjson)
    except ValueError as e:
        return False
    return True


@REQUEST_API.route('/list/<string:_id>', methods=['GET'])
def get_record_by_user_id(_id):
    """Return user list by user id
    @param _id: the usr id
    @return: 200: a json object of items in user list as a flask/response object \
    with application/json mimetype.
    @raise 404: if user list request not found
    """
    if not _id:
        abort(400)

    doc_ref = db.collection(u'users').document(_id)

    doc = doc_ref.get()

    if doc.exists:
        return jsonify(doc.to_dict())
    else:
        abort(404)


@REQUEST_API.route('/list/<string:_id>', methods=['POST'])
def create_list(_id):
    """Create a user list 
    @param _id: the usr id
    @param list: post : the fields to add to a new list
    @return: 201: with application/json mimetype.
    @raise 400: misunderstood request
    """

    if not _id:
        abort(400)

    if not request.get_json():
        abort(400)

    data = request.get_json(force=True)

    if not is_json(data):
        abort(405)

    Items_list = {
        "item_list": data,
    }

    # Add a new doc in collection 'users' by user id
    db.collection(u'users').document(_id).set(Items_list)
    # HTTP 201 Created
    return 'list created', 201


@REQUEST_API.route('/list/<string:_id>', methods=['PUT'])
def update_list(_id):
    """Update the user list
    @param _id: the usr id
    @param list: post : the fields to update the exsisting list
    @return: 200: with application/json mimetype.
    @raise 400: misunderstood request
    """

    if not _id:
        abort(400)

    if not request.get_json():
        abort(400)

    data = request.get_json(force=True)

    if not is_json(data):
        abort(405)

    Items_list = {
        "item_list": data,
    }

    # Add a new doc in collection 'users' by user id
    db.collection(u'users').document(_id).set(Items_list)
    return 'list update success', 200


@REQUEST_API.route('/list/<string:_id>', methods=['DELETE'])
def clear_list(_id):
    """Clear the user list
    @param id: the user id
    @return: 200: success.
    @raise 404: if list request not found
    """
    if not _id:
        abort(404)

    item_list = {}
    # Add a new doc in collection 'users' by user id
    db.collection(u'users').document(_id).set(item_list)

    return 'list cleared success', 200

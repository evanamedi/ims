from flask import jsonify

def format_response(status, message, data=None):
    response = jsonify({
        "status": status,
        "message": message,
        "data": data if isinstance(data, list) else [data],
    })
    response.status_code = status
    return response

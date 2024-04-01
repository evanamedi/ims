from flask_restful import Resource, reqparse
from api_v3.models import db, Customer

class CustomerResource(Resource):
    def __init__(self):
        self.model = Customer
        self.parser = reqparse.RequestParser()
        for column in Customer.__table__.columns:
            self.parser.add_argument(column.name)

    def post(self):
        return self._post()

    def put(self, id):
        return self._put(id)

    def delete(self, id):
        return self._delete(id)

    def get(self, id):
        return self._get(id)

    def _post(self):
        args = self.parser.parse_args()
        new_row = self.model(**args)
        db.session.add(new_row)
        db.session.commit()
        return {column.name: getattr(new_row, column.name) for column in self.model.__table__.columns}, 201

    def _put(self, id):
        args = self.parser.parse_args()
        instance = db.session.query(self.model).get(id)
        if instance:
            for column in self.model.__table__.columns:
                if args[column.name] is not None:
                    setattr(instance, column.name, args[column.name])
            db.session.commit()
            return {column.name: getattr(instance, column.name) for column in self.model.__table__.columns}, 200
        else:
            return {'message': 'Item not found'}, 404

    def _delete(self, id):
        instance = db.session.query(self.model).get(id)
        if instance:
            db.session.delete(instance)
            db.session.commit()
            return {'message': 'Deleted successfully'}, 200
        else:
            return {'message': 'Item not found'}, 404

    def _get(self, id):
        instance = db.session.query(self.model).get(id)
        if instance:
            return {column.name: getattr(instance, column.name) for column in self.model.__table__.columns}, 200
        else:
            return {'message': 'Item not found'}, 404

class CustomerQueryResource(Resource):
    def __init__(self):
        self.model = Customer
        self.operations = {
            'all': self.get_all,
            'count': self.get_count,
            'filter': self.get_filter,
        }

    def get(self, operation, field=None, value=None):
        getFunction = self.operations.get(operation)
        if getFunction:
            return getFunction(field, value)
        else:
            return {'message': 'Invalid operation'}, 400

    def get_all(self, field, value):
        return [self.row2dict(row) for row in db.session.query(self.model).all()], 200

    def get_count(self, field, value):
        return {'count': db.session.query(self.model).count()}, 200

    def get_filter(self, field, value):
        if field and value:
            return [self.row2dict(row) for row in db.session.query(self.model).filter(getattr(self.model, field) == value).all()], 200
        else:
            return {'message': 'Invalid filter parameters'}, 400

    @staticmethod
    def row2dict(row):
        return {column.name: getattr(row, column.name) for column in row.__table__.columns}

from factory import create_app

app = create_app()

class TableIdData:
    def __init__(self, model):
        self.model = model

    def get_ids(self):
        with app.app_context():
            records = self.model.query.all()
            return [record.id for record in records]


def getID(tableName):
    table_data = TableIdData(tableName)
    ids = table_data.get_ids()
    return ids



# if __name__ == '__main__':
#     table_data = TableIdData(Supplier)
#     supplier_ids = table_data.get_ids()
#     print(supplier_ids)


import requests
import db_connector

def get_test(id):

    try:
        res = requests.get(f"http://127.0.0.1:5000/users/{id}")
        print(res, res.text)
    except:
        print("Error")

def post_test(id, name):
    try:
        res = requests.post(f"http://127.0.0.1:5000/users/{id}", json={"name": f"{name}"})
        print(res, res.text)
    except:
        print("Error")

def put_test(id, name):
    try:
        res = requests.put(f"http://127.0.0.1:5000/users/{id}", json={"name": f"{name}"})
        print(res, res.text)
    except:
        print("Error")

def delete_test(id):
    try:
        res = requests.delete(f"http://127.0.0.1:5000/users/{id}")
        print(res, res.text)
    except:
        print("Error")

def backend_test(id, name, mod_name):

    try:
        db_connector.get_table()
        post_test(id, name)
        get_test(id)
        db_connector.get_table()
        put_test(id, mod_name)
        db_connector.get_table()
        delete_test(id)
        db_connector.get_table()

    except Exception as e:
        print("Frontend test failed")
        print(e)

if __name__ == '__main__':
    backend_test('543', 'Jamie', 'JamieNew')

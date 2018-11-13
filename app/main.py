# Για να δουλέψει αντικαταστήστε στο config.json το
# "SQLALCHEMY_DATABASE_URI": "postgresql://postgres:postgres@localhost/solidity" με
# "SQLALCHEMY_DATABASE_URI": "postgresql://postgres:member2018@83.212.123.145/solidity"

from app import app

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)

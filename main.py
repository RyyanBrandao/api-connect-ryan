from flask import Flask, jsonify, request

app = Flask(__name__)

users_db = []
_next_id = 1

def generate_id():
    global _next_id
    id_gerado = _next_id
    _next_id += 1
    return id_gerado

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users_db), 200

@app.route('/users', methods=['POST'])
def create_user():
    dados = request.get_json()
    
    if not dados or 'nome' not in dados or 'email' not in dados:
        return jsonify({"error": "Os campos 'nome' e 'email' são obrigatórios."}), 400
        
    if not str(dados['nome']).strip() or not str(dados['email']).strip():
        return jsonify({"error": "Os campos não podem estar em branco."}), 400
    
    novo_usuario = {
        "id": generate_id(),
        "nome": dados["nome"],
        "email": dados["email"]
    }
    users_db.append(novo_usuario)
    
    return jsonify({"data": novo_usuario}), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    for user in users_db:
        if user['id'] == user_id:
            return jsonify(user), 200
    return jsonify({"erro": "Usuário não encontrado."}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)
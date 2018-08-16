from sanic import Sanic
from sanic.response import json

from models import db, User

app = Sanic()
app.config.DB_HOST = 'localhost'
app.config.DB_USER = 'gino'
app.config.DB_PASSWORD = 'gino'
app.config.DB_DATABASE = 'gino'
db.init_app(app)


@app.route('/v1/users/', methods=['GET'])
async def users_list(request):
    users = await User.query.gino.all()

    data = [
        {'id': user.id, 'nickname': user.nickname}
        for user in users
    ]
    return json(data)


@app.route('/v1/users/<user_id:int>/', methods=['GET'])
async def users_fetch(request, user_id):
    user = await User.get_or_404(user_id)

    data = {'id': user.id, 'nickname': user.nickname}
    return json(data)


@app.route('/v1/users/', methods=['POST'])
async def users_create(request):
    user = await User.create(**request.json)

    data = {'id': user.id, 'nickname': user.nickname}
    return json(data, status=201)


@app.route('/v1/users/<user_id:int>/', methods=['PATCH'])
async def users_update(request, user_id):
    nickname = request.json['nickname']
    await User.update.values(nickname=nickname).where(User.id == user_id).gino.status()

    data = {'id': user_id, 'nickname': nickname}
    return json(data)


@app.route('/v1/users/<user_id:int>/', methods=['DELETE'])
async def users_delete(request, user_id):
    await User.delete.where(User.id == user_id).gino.status()

    return json({}, status=204)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

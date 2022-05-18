from flask import Flask, g, request, jsonify
from database import get_db
from functools import wraps

app = Flask(__name__)
app.config['debug'] = True

api_username = "admin"
api_password = "password"


def protected(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if (auth and auth.username == api_username and auth.password == api_password):
            return f(*args, **kwargs)
        else:
            return jsonify({"message": "authentication failed"}), 403
    return decorated


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/member', methods=['GET'])
@protected
def get_members():
    db = get_db()
    members_cur = db.execute('select id, name, email, level from members;')
    members = members_cur.fetchall()
    members_list = list()
    for member in members:
        temp = {
            "id": member['id'],
            "name": member['name'],
            "email": member['email'],
            "level": member['level']
        }
        members_list.append(temp)
    return jsonify(members=members_list)


@app.route('/member/<int:member_id>', methods=['GET'])
@protected
def get_member(member_id):
    db = get_db()
    member_cur = db.execute('''
                            select id, name, email, level from members
                            where id = ? ;''', [member_id])
    member = member_cur.fetchone()
    return jsonify({
        "member": {
            "id": member["id"],
            "name": member["name"],
            "email": member["email"],
            "level": member["level"]
        }
    })


@app.route('/member', methods=['POST'])
@protected
def add_member():
    member_data = request.get_json()
    name = member_data['name']
    email = member_data['email']
    level = member_data['level']
    db = get_db()
    db.execute('''
                insert into members (name, email, level)
                values (?, ?, ?)''', [name, email, level])
    db.commit()
    member_cur = db.execute('''
                                select id, name, email, level from members
                                where name = ?''', [name])
    member_result = member_cur.fetchone()
    return jsonify({
        "member": {
            "id": member_result['id'],
            "name": member_result['name'],
            "email": member_result['email'],
            "level": member_result['level']
        }
    })


@app.route('/member/<int:member_id>', methods=['PUT', 'PATCH'])
@protected
def edit_member(member_id):
    member_data = request.get_json()
    name = member_data['name']
    email = member_data['email']
    level = member_data['level']
    db = get_db()
    db.execute('''
                update members set name = ?, email = ?, level = ?
                where id = ?''', [name, email, level, member_id])
    db.commit()
    member_cur = db.execute('''
                            select id, name, email, level from members
                            where id = ?''', [member_id])
    member_result = member_cur.fetchone()
    return jsonify({
        "member": {
            "id": member_result['id'],
            "name": member_result['name'],
            "email": member_result['email'],
            "level": member_result['level']
        }
    })


@app.route('/member/<int:member_id>', methods=['DELETE'])
@protected
def delete_member(member_id):
    db = get_db()
    db.execute('delete from members where id = ?', [member_id])
    db.commit()
    return jsonify({"message": "member has been deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)

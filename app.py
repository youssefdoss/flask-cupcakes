"""Flask app for Cupcakes"""

from flask import Flask, request, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.get('/api/cupcakes')
def list_all_cupcakes():
    '''Return JSON of all cupcakes {'cupcakes': [{id, ...}, ...]}'''

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)

@app.get('/api/cupcakes/<int:cupcake_id>')
def list_single_cupcake(cupcake_id):
    """ Return JSON data from single cupcake. {'cupcake': {id, ...}}"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake = serialized)

@app.post('/api/cupcakes')
def create_cupcake():
    """ Create cupcake from posted JSON data and return it
        {'cupcake': {id, ...}} """

    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    try:
        image = request.json['image'] #can replace with request.json.get()

    except KeyError:
        image = None

    new_cupcake = Cupcake(flavor = flavor,
                            size = size,
                            rating = rating,
                            image = image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(cupcake = serialized), 201)

@app.patch('/api/cupcakes/<int:cupcake_id>')
def update_cupcake(cupcake_id):
    '''Update cupcake from patched JSON data and return it
    {'cupcake': {id, flavor, size, rating, image}}'''

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.check_if_none_and_update()

    db.session.commit()

    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.delete('/api/cupcakes/<int:cupcake_id>')
def delete_cupcake(cupcake_id):
    '''Delete cupcake from JSON cupcake_id and return JSON cupcake_id
    {deleted: cupcake_id}'''

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)

    db.session.commit()

    return jsonify(deleted=cupcake_id)
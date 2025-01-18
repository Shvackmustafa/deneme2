from sanic import Sanic
from database import db
from routes.user_routes import user_bp
from routes.blog_routes import blog_bp
from routes.pet_routes import pet_bp
from routes.sterilization_routes import sterilization_bp
from routes.contact_routes import contact_bp

app = Sanic("pet_app")

app.blueprint(user_bp)
app.blueprint(blog_bp)
app.blueprint(pet_bp)
app.blueprint(sterilization_bp)
app.blueprint(contact_bp)

@app.listener('after_server_start')
async def connect_to_db(*args, **kwargs):
    await db.connect()

@app.listener('after_server_stop')
async def disconnect_from_db(*args, **kwargs):
    await db.disconnect()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

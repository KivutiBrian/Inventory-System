from main import db
from sqlalchemy import func

class InventoryModel(db.Model):
    __tablename__ = "inventories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(55), nullable=False, unique=True)
    type = db.Column(db.String(55), nullable=False)
    bp = db.Column(db.Float, nullable=False)
    sp = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
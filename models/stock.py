from main import db
from sqlalchemy import func

class StockModel(db.Model):
    __tablename__ = 'stocks'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    inv_id = db.Column(db.Integer, db.ForeignKey('inventories.id'), nullable=False)

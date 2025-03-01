from sqlalchemy import Column, String, Float
from sqlalchemy import orm

from app.models.base_model import BaseModel


class Expense(BaseModel):
    __tablename__ = 'expense'

    name = Column(String)
    amount = Column(Float)
    category = Column(String)

    @classmethod
    def create_expense(cls, exp_data: dict, db: orm.Session):
        try:
            expense = Expense()
            expense.name = exp_data.get('name')
            expense.amount = exp_data.get('amount')
            expense.category = exp_data.get('category')

            db.commit()
            db.refresh(expense)

            return expense
        except Exception as e:
            db.rollback()
            print("occurred inside create_exp", str(e))

    @classmethod
    def get_expense(cls, exp_id, db: orm.Session):
        try:
            query = db.query(cls).filter(id=exp_id)
            return query
        except:
            raise Exception

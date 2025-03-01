from fastapi import Depends, Response, Request

from app.models.model import Expense
from app.models.db_session import get_db
from app.routes.base_router import api_router


@api_router.post('create')
async def create_expense(request: Request, db: Depends(get_db())):
    try:
        req_json = await request.json()

        exp_dict = {
            'name': req_json['name'],
            'amount': req_json['amount'],
            'category': req_json['category']}

        create_exp = Expense.create_expense(exp_data=exp_dict, db=db)

        if create_exp is not None:
            return create_exp
        else:
            return Response({'success': False})
    except Exception as e:
        return e

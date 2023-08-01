from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

import sqlalchemy as sa


class User(db.Model):
    id = sa.column(sa.Integer, primary_key=True)
    username = sa.column(sa.String(80), )


    # id=sa.column(sa.Integer, primary_key=True)
    # username=sa.column(sa.String)
    #

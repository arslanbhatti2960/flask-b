from app import db

class user (db.Model):
    _tablename_="users"

    id=db.column(
        db.Integer,
        primary_key=True
    )
    username = db.column(
        db.string(50),
        unique=True,
        nullable=False
    )
    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    def __repr__(self):
        return f"<User {self.username}>"
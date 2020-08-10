from .. import db


class Source(db.Model):
    __tablename__ = "sources"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.VARCHAR(64), nullable=False, unique=True)
    url = db.Column(db.VARCHAR(120), nullable=False)

    data = db.relationship("Datum", backref="source")

    def __repr__(self):
        return '<Source#{}:"{}" from {}>'.format(self.id, self.name, self.url)

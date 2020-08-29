from .. import db


class Country(db.Model):
    __tablename__ = "countries"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.VARCHAR(64), unique=True, nullable=False)

    provinces = db.relationship("Province", backref="country")

    def __repr__(self):
        return '<Country#{}:"{}">'.format(self.id, self.name)

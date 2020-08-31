from .. import db


class News(db.Model):
    __tablename__ = "news"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)

    date = db.Column(db.TIMESTAMP, index=True, nullable=False)
    title = db.Column(db.VARCHAR(120), nullable=False)
    brief = db.Column(db.Text, nullable=False)
    source = db.Column(db.VARCHAR(120), index=True, nullable=False)

    def __repr__(self):
        return '<News#%d@%s[%s]%sfrom %s}>' % (
            self.id, self.date, self.title, self.brief, self.source
        )

    def json(self):
        return {
            "id": self.id,
            "date": self.date,
            "title": self.title,
            "brief": self.brief,
            "source": self.source
        }
#app = RecordDatainGoogleSheet(create_app())
#app.writeInGoogleSheet()
import db.db as db
from db.models import Employee


def run():
    pass

if __name__ == "__main__":
    #p1 = Person()
    #p1.insert(23657851, "Leonardo", "Febres")
    db.BASE.metadata.create_all(db.engine)
    p1 = Employee(identificationNationalDocument=23657851, firstName="Leonardo", lastName="Febres")
    db.session.add(p1)
    db.session.commit()


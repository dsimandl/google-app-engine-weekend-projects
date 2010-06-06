from google.appengine.ext import db
class VoittoRivi(db.Model):
    kierros=db.IntegerProperty()
    vuosi=db.IntegerProperty()
    numerot=db.ListProperty(int)
    lisanumerot=db.ListProperty(int)
    
class LottoRivi(db.Model):
    owner=db.UserProperty(auto_current_user_Add=True)
    numerot=db.ListProperty(int)

class Voittoluokat(db.model):
    numerot_count=db.IntegerProperty()
    lisanumerot_count=db.IntegerProperty()

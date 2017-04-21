from kon import db, kusi
import datetime
db = db
kusi = kusi

tday = datetime.date.today()

def cba(isi1, isi2, isi3, isi4, isi5, isi6, isi7, isi8):
    kusi.execute("insert into movie (title, tanggal, episode, keterangan, rating, country, lang, genre, tglinput) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)" % (isi1, isi2, isi3, isi4, isi5, isi6, isi7, isi8, tday))
    db.commit()
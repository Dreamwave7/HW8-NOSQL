from models import *
import pprint
tag = Tag(name="Weekends")

record1 = Record(description="Take tables")
record2 = Record(description="Buy cigarettes")
record3 = Record(description = "Buy meat")

not11e =Notes(name = "Weekend", records =[record1,record2,record3],tags= [tag,])


notes = Notes.objects()
for note in notes:
    pprint.pprint(note.to_mongo().to_dict())


















from datetime import datetime
from neomodel import StructuredNode, UniqueIdProperty, StringProperty, IntegerProperty, RelationshipTo, StructuredRel, DateTimeProperty
from pydantic import BaseModel
import pytz


class FollowUp(StructuredRel):
    since = DateTimeProperty(
        default=lambda: datetime.now(pytz.utc)
    )


class UserNode(StructuredNode):
    uid = UniqueIdProperty()

    pk = StringProperty(unique_index=True)
    username = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)
    
    follows = RelationshipTo('UserNode', 'Follows', model=FollowUp)


class UserCreate(BaseModel):
    pk: str
    username: str
    age: int

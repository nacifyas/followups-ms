import datetime
from neomodel import StructuredNode, UniqueIdProperty, StringProperty, IntegerProperty, RelationshipFrom, StructuredRel, DateTimeProperty
import pytz


class FollowUp(StructuredRel):
    since = DateTimeProperty(
        default=lambda: datetime.now(pytz.utc)
    )


class User(StructuredNode):
    uid = UniqueIdProperty()
    username: StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)

    following = RelationshipFrom('User', 'Follows', model=FollowUp)

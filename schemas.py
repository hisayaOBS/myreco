from datetime import datetime, time

from typing import Union

from pydantic import BaseModel

# データの作成、読み取り
class RecordBase(BaseModel):
    inputday: Union[datetime, time]
    value: int
    memo: Union[str, None] = None
    tag_id: Union[int, None] = None



class RecordCreate(RecordBase):
    pass

class RecordUpdate(RecordBase):
    pass

# APIからデータを返すときに使用する(データを読み取り用)
class Record(RecordBase):
    id: int
    user_id: int
    tag_id: Union[int, None]

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    Records: list[Record] = []

    class Config:
        orm_mode = True


class TagBase(BaseModel):
    tag_name = str
    unit = Union[str, None] = None



class TagCreate(TagBase):
    pass

class TagUpdate(TagBase):
    pass

class Tag(TagBase):
    id: int
    Records: list[Record] = []

    class Config:
        orm_mode = True

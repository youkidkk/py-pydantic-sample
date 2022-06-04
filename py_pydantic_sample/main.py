from datetime import datetime

from pydantic import BaseModel


class SampleModel(BaseModel):
    number: int
    text: str
    time: datetime
    default_value: int = 111


# コンストラクタから生成
model = SampleModel(number=123, text="Text", time=datetime(2000, 1, 1, 11, 22))
print(model)

# dict から生成
sample_data = {"number": 123, "text": "Text", "time": "2022-04-01 12:34"}
model = SampleModel(**sample_data)
print(model)

# dict に変換
print(model.dict())

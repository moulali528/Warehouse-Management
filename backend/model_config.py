from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field

class TaskRequest(BaseModel):
    task: str = Field(max_length=100)
    description: str = Field(max_length=500)
    status: bool = Field(default=False)
    is_deleted: Optional[bool] = Field(default=False)

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "task":"Go to grocory",
                "description":"Bring the eggs",
                "status": False
            }
        }
    )

class UserAddress(BaseModel):
    door_number: int = Field(le=999)
    street_name: str = Field(max_length=50)
    district: str = Field(max_length=50)
    postcode: str = Field(max_length=15)

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                            "door_number": 101,
                            "street_name": "Baker Street",
                            "district": "Westminster",
                            "postcode": "W1U 8ED"
                        }
        }
    )


class UserRequest(BaseModel):
    email: str = Field(max_length=50)
    username: str = Field(max_length=15)
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    hased_password: str = Field(max_length=15, min_length=6)
    is_active: bool = Field(default=True)
    role: str = Field(max_length=15)
    # addresses: List[UserAddress]

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "email":"mouli@gmail.com",
                "username":"moulali528",
                "first_name": "Moulali",
                "last_name": "Dudekula",
                "hased_password": "Jun@2025",
                "is_Active": False,
                "role": "Active Member",
                # "addresses": [
                #                 {
                #                     "door_number": 101,
                #                     "street_name": "Baker Street",
                #                     "district": "Westminster",
                #                     "postcode": "W1U 8ED"
                #                 },
                #                 {
                #                     "door_number": 101,
                #                     "street_name": "Baker Street",
                #                     "district": "Westminster",
                #                     "postcode": "W1U 8ED"
                #                 }
                #             ]
            }
        }
    )
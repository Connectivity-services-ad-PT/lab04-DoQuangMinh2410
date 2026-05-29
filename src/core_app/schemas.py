from pydantic import BaseModel, Field, HttpUrl
from typing import Literal, Union, Optional
from datetime import datetime

# --- KHỐI 1: XỬ LÝ LỖI CHUẨN RFC 7807 ---
class ProblemDetails(BaseModel):
    type: HttpUrl = Field(..., examples=["https://smartcampus.dnu.edu.vn/probs/bad-request"])
    title: str = Field(..., examples=["Invalid Request Payload"])
    status: int = Field(..., examples=[400])
    detail: str = Field(..., examples=["Trường dữ liệu 'card_id' bắt buộc phải truyền."])
    instance: Optional[str] = Field(None, examples=["/api/v1/events/access"])

# --- KHỐI 2: SCHEMAS TIẾP NHẬN ĐỒNG BỘ TỪ ACCESS GATE (B3) ---
class AccessCheckEvent(BaseModel):
    event_type: Literal["ACCESS_CHECK"]
    timestamp: datetime
    card_id: str = Field(..., pattern=r"^card-[0-9]{8}$", examples=["card-12345678"])
    gate_id: str = Field(..., pattern=r"^gate-[a-z0-9\-]+$", examples=["gate-block-d-01"])
    direction: Literal["IN", "OUT"]

class SensorReadingEvent(BaseModel):
    event_type: Literal["SENSOR_READING"]
    timestamp: datetime
    sensor_id: str
    value: float

# Định nghĩa Đa hình (Polymorphism) bằng Union + Discriminator theo quy chuẩn lớp
GenericCampusEvent = Union[AccessCheckEvent, SensorReadingEvent]

class AccessCheckResponse(BaseModel):
    event_id: str
    status: Literal["ALLOWED", "DENIED"]
    reason: Optional[str] = Field(None, examples=["Thẻ hợp lệ, cho phép mở chốt cửa."])
    processed_at: datetime

# --- KHỐI 3: SCHEMAS QUẢN LÝ CẢNH BÁO (ALERTS) ---
class AlertResponse(BaseModel):
    alert_id: str
    severity: Literal["INFO", "WARNING", "CRITICAL"]
    source: str
    message: str
    resolved: bool
    created_at: datetime
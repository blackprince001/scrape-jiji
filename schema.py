from typing import Dict, List, Optional, Union

from pydantic import BaseModel


class ImageObj(BaseModel):
    url: str
    center: Optional[Dict[str, str]]


class PriceObj(BaseModel):
    value: Optional[int]
    view: Optional[str]
    period: Optional[str]
    bulk: Optional[Dict[str, str]]


class FbViewContentData(BaseModel):
    content_name: str
    content_category: str
    content_ids: List[str]
    content_type: str
    value: str
    currency: str


class EventParams(BaseModel):
    cpc_campaign_id: int = 14038
    position_type: str = "cpc"


class Image(BaseModel):
    url: str
    center: Optional[Dict[str, str]]
    size: List[int]


class Property(BaseModel):
    admin_info: Dict[str, str]
    as_top: bool
    attrs: List[dict]
    badge_info: Dict[str, str]
    can_view_contacts: bool
    category_id: int
    category_name: str
    category_slug: str
    count_images: int
    details: str
    event_params: EventParams = {}
    fb_view_content_data: FbViewContentData
    guid: str
    id: int
    image_obj: ImageObj
    images: List[Image]
    images_count: int
    is_boost: Union[str, bool]
    is_cv: bool
    is_inspected: bool
    is_job: bool
    is_owner: bool
    is_top: bool
    labels: List[dict]
    message_url: str
    paid_info: dict
    price_obj: PriceObj
    price_title: str
    region: str
    region_id: int
    region_item_text: str
    region_name: str
    region_parent_name: str
    region_slug: str
    short_description: str
    slug: str
    status: str
    title: str
    title_labels: List[str]
    tops_count: int
    url: str
    user_id: int
    user_phone: str


class ExtractedData(BaseModel):
    region_id: int
    region_name: str
    region_parent_name: str
    description: str
    price: int
    message_url: str

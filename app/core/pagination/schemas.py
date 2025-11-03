from typing import TypeVar, Generic, Sequence
from pydantic import BaseModel, Field

T = TypeVar('T')

class PageParams(BaseModel):
    page: int = Field(default=1, ge=1, description="Pàage number (start 1)")
    size: int = Field(default=10, ge=1, le=100, description="items for page (beetween 1 and 100)")

class PageResponse(BaseModel, Generic[T]):
    items: Sequence[T]
    total: int
    page: int
    size: int
    pages: int
    has_next: bool
    has_previous: bool

    @classmethod
    def create(cls, items: Sequence[T], total: int, page_params: PageParams) -> "PageResponse[T]":
        pages = (total + page_params.size - 1) // page_params.size
        return cls(
            items=items,
            total=total,
            page=page_params.page,
            size=page_params.size,
            pages=pages,
            has_next=page_params.page < pages,
            has_previous=page_params.page > 1
        )
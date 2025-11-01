from typing import TypeVar, Generic, Sequence, Type
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import Select

from app.core.pagination.schemas import PageParams, PageResponse

T = TypeVar('T')

class Paginator(Generic[T]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def paginate(
        self,
        query: Select,
        page_params: PageParams,
        model: Type[T]
    ) -> PageResponse[T]: 
        count_query = select(func.count()).select_from(query.subquery())
        total = await self.session.scalar(count_query) or 0
        offset = (page_params.page - 1) * page_params.size
        query = query.offset(offset).limit(page_params.size)
        result = await self.session.execute(query)
        items = result.scalars().all()
        return PageResponse.create(
            items=items,
            total=total,
            page_params=page_params
        )
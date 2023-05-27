import uuid
from typing import Optional

from sqlalchemy import ForeignKey, Table
from app.schemas.base import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Table, Column


# class UrlUserLinkDb(Base):
#     __tablename__ = "url_user_link"

#     url_id: Mapped[Optional[uuid.UUID]] = mapped_column(
#         ForeignKey("url.id"),
#         primary_key=True,
#         default=None,
#     )

#     user_id: Mapped[Optional[uuid.UUID]] = mapped_column(
#         ForeignKey("user.id"),
#         primary_key=True,
#         default=None,
#     )


UrlUserLinkDb = Table(
    "url_user_link",
    Base.metadata,
    Column("url_id", ForeignKey("url.id"), primary_key=True, nullable=False),
    Column("user_id", ForeignKey("user.id"), primary_key=True, nullable=False),
)

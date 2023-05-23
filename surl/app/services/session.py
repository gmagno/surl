from typing import Optional
from uuid import uuid4
from fastapi import Depends, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.session import SessionDb, SessionDbCreate
import datetime as dt

from app.services.base import BaseService

from app.db.crud.crud_session import crud_session


class SessionService(BaseService):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(db=db)

    async def get_or_create(
        self,
        *,
        request: Request,
    ) -> str:
        # session = request.session.get("foo", None)
        # if not session:
        #     request.session["foo"] = {"1": 1}
        request.session["ble"] = {"1": 1}

        # session = request.session.get("surl_session", None)
        # try:
        #     session = request.session["surl_session"]
        # except KeyError:
        #     request.session["surl_session"] = {"1": 1}
        # # if not session:
        # #     # request.session["surl_session"] = {"1", "2"}
        # #     request.session["surl_session"] = {"1": 1}

        # request.session["surl_session"] = {"1": 1}
        print("aaaaaa")
        return ""

        # session = SessionDb(
        #     id=uuid4(),
        #     create_at=dt.datetime.now(),
        # )

        # try:
        #     payload: dict[str, Any] = jwt.decode(
        #         token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        #     )
        #     token_data = TokenPayload(**payload)
        # except (jwt.JWTError, ValidationError):
        #     raise

        # user: Optional[UserDb] = await crud_user.get(db, id=token_data.sub)
        # if not user:
        #     raise HTTPException(status_code=404, detail="User not found")
        # return user


async def create_service(db: AsyncSession) -> SessionService:
    session_svc = SessionService(db)
    return session_svc


async def get_session_service(
    db: AsyncSession = Depends(get_db),
) -> SessionService:
    session_svc: SessionService = await create_service(db)
    return session_svc


async def get_or_create_session(
    request: Request,
    db: AsyncSession = Depends(get_db),
) -> SessionDb:
    # #
    # session_id: str = request.session.get("surl_session", "")
    # session_db: Optional[SessionDb] = await crud_session.get(
    #     db=db,
    #     id=session_id,
    # )

    # if not session_db:
    #     session_db = await crud_session.create(
    #         db=db,
    #         obj_in=SessionDbCreate(),
    #         commit=True,
    #         # refresh=True,
    #     )
    #     request.session["surl_session"] = str(session_db.id)

    # #
    create_session = False
    if request.session:
        try:
            session_db: Optional[SessionDb] = await crud_session.get(
                db=db,
                id=request.session["surl_session"],
            )
        except Exception:
            create_session = True
        if not session_db:
            create_session = True
    else:
        create_session = True

    if create_session:
        session_db = await crud_session.create(
            db=db,
            obj_in=SessionDbCreate(),
            commit=True,
            # refresh=True,
        )
        request.session["surl_session"] = str(session_db.id)

    return session_db
from flask import abort

from pytz import timezone
from datetime import datetime

from server.model import session
from server.model.notice import Notice
from server.model.user import User
from server.controller.exception import check_exception

# from scr.controller.notify import sendMessage


@check_exception
def create_notice(title, content, user_email):
    new_notice = Notice(title=title,
                        content=content,
                        user_email=user_email,
                        created_at=datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S'))

    session.add(new_notice)
    session.commit()

    # sendMessage(title="새로운 공지사항", body=title)

    return {
            "message": "success"
        }, 201


@check_exception
def get_notice_list(page):
    limit = 10
    offset = page * limit

    notice_list = session.query(Notice, User)\
        .filter(Notice.user_email == User.email)\
        .order_by(Notice.created_at.desc())\
        .limit(limit).offset(offset)

    next_notice = session.query(Notice).limit(1).offset(offset + limit).scalar()

    next_page = True if next_notice else False

    return {
        "notice": [{
            "id": notice.id,
            "title": notice.title,
            "content": notice.content,
            "user_name": user.name,
            "created_at": str(notice.created_at)
        } for notice, user in notice_list],
        "next_page": next_page
    }, 200


@check_exception
def delete_notice(notice_id, user_email):
    del_notice = session.query(Notice).filter(Notice.id == notice_id)

    if not del_notice.scalar():
        abort(404, 'could not find notice matching this id')

    del_notice = del_notice.first()

    if not del_notice.user_email == user_email:
        abort(403, 'could not delete notice created by others')

    session.delete(del_notice)

    session.commit()

    return {
        "message": "success"
    }, 204


@check_exception
def get_detail_notice(notice_id):
    notice = session.query(Notice, User).\
        filter(Notice.user_email == User.email).\
        filter(Notice.id == notice_id)

    if notice.scalar():
        return {
            "notice": {
                "name": notice[0][1].name,
                "created_at": str(notice[0][0].created_at),
                "title": notice[0][0].title,
                "content": notice[0][0].content
            }
        }, 200

    else:
        abort(404, 'could not find notice matching this id')

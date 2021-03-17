from flask import abort

from server.model import Session
from server.model.notice import Notice
from server.model.user import User

# from scr.controller.notify import sendMessage


def create_notice(title, content, user_email):

    new_notice = Notice(title=title, content=content, user_email=user_email)

    Session.add(new_notice)
    Session.commit()

    # sendMessage(title="새로운 공지사항", body=title)

    return 201


def get_notice_list(off_set, limit_num):
    notice_list = Session.query(Notice).order_by(Notice.created_at.desc()).offset(off_set).limit(limit_num)

    if notice_list:
        return {
            "notice": [{
                "id": n.id,
                "title": n.title,
                "content": n.content,
                "user_email": n.user_email,
                "created_at": n.created_at
            } for n in notice_list]
        }, 200
    else:
        return abort(404, 'notice does not exist')


def delete_notice(notice_id):
    del_notice = Session.query(Notice).filter(Notice.id == notice_id).first()

    if del_notice:
        Session.delete(del_notice)

        Session.commit()

        return 204
    else:
        return abort(404, 'could not find notice matching this id')


def get_detail_notice(notice_id):
    notice = Session.query(Notice).filter(Notice.id == notice_id).first()

    if notice:
        user = Session.query(User).filter(User.email == notice.user_email).first()

        return {
            "notice": {
                "name": user.name,
                "created_at": notice.created_at,
                "title": notice.title,
                "content": notice.content
            }
        }, 200

    else:
        return abort(404, 'could not find notice matching this id')

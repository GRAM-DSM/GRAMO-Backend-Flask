from flask import abort

from server.model import session
from server.model.notice import Notice
from server.model.user import User
from server.controller.exception import check_exception

# from scr.controller.notify import sendMessage


@check_exception
def create_notice(title, content, user_email):
    user = session.query(User).filter(User.email == user_email).first()

    new_notice = Notice(title=title,
                        content=content,
                        user_name=user.name)

    session.add(new_notice)
    session.commit()

    # sendMessage(title="새로운 공지사항", body=title)

    return 201


@check_exception
def get_notice_list(off_set, limit_num):
    notice_list = session.query(Notice).order_by(Notice.created_at.desc()).offset(off_set).limit(limit_num)

    return {
        "notice": [{
            "id": n.id,
            "title": n.title,
            "content": n.content,
            "user_name": n.user_name,
            "created_at": str(n.created_at)
        } for n in notice_list]
    }, 200


@check_exception
def delete_notice(notice_id, user_email):
    del_notice = session.query(Notice).filter(Notice.id == notice_id).first()

    if del_notice:
        user = session.query(User).filter(User.email == user_email).first()
        if del_notice.user_name == user.name:
            session.delete(del_notice)

            session.commit()

            return 204
        else:
            abort(403, 'could not delete notice created by others')
    else:
        abort(404, 'could not find notice matching this id')


@check_exception
def get_detail_notice(notice_id):
    notice = session.query(Notice).filter(Notice.id == notice_id).first()
    
    if notice:
        return {
            "notice": {
                "name": notice.user_name,
                "created_at": str(notice.created_at),
                "title": notice.title,
                "content": notice.content
            }
        }, 200

    else:
        abort(404, 'could not find notice matching this id')

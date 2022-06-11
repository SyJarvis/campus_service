# coding: utf-8
from application import db


class OauthMemberBind(db.Model):
    __tablename__ = 'oauth_member_bind'
    __table_args__ = (
        db.Index('idx_type_openid', 'type', 'openid'),
    )

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, nullable=False)
    client_type = db.Column(db.String(20), nullable=False)
    type = db.Column(db.Integer, nullable=False)
    openid = db.Column(db.String(80), nullable=False)
    unionid = db.Column(db.String(100), nullable=False)
    extra = db.Column(db.Text, nullable=False)
    updated_time = db.Column(db.DateTime, nullable=False)
    created_time = db.Column(db.DateTime, nullable=False)

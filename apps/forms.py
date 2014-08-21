# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import (
    StringField,
    PasswordField,
    TextAreaField
)
from wtforms import validators


class moim_pay(Form):
    member = StringField(
        u'참여자',
        [validators.data_required(u'참여자를 입력하시기 바랍니다.')],
        description={'placeholder': u'참여자를 입력하세요.'}
    )
    place = StringField(
        u'장소',
        [validators.data_required(u'장소를 입력하시기 바랍니다.')],
        description={'placeholder': u'장소를 입력하세요.'}
    )
    content = StringField(
        u'지출 내역',
        [validators.data_required(u'지출 내역을 입력하시기 바랍니다.')],
        description={'placeholder': u'지출 내역을 입력하세요.'}
    )
    pay_all = StringField(
        u'총 지출액',
        [validators.data_required(u'총 지출액을 입력하시기 바랍니다.')],
        description={'placeholder': u'총 지출액을 입력하세요.'}
    )

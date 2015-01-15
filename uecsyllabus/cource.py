# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import collections
import enum
import six

Department = enum.Enum("Department", (
    "ELECTRO_COMMUNICATIONS",
    "INFOMATICS_ENGINEERING",
    "INFORMATION_SYSTEMS"))

Graduate = enum.Enum("Graduate", ("MASTER", "DOCTOR",))

CourceBase = collections.namedtuple("Cource", ("department", "evening", "graduate"))
@six.python_2_unicode_compatible
class Cource(CourceBase):

    def __new__(cls, department, evening=False, graduate=False):
        return super(CourceBase, cls).__new__(cls, (department, evening, graduate))

    def __str__(self):
        if self in COURCE_INDEX:
            return COURCE_INDEX[self]


COURCES = (
    (
        Cource(Department.INFOMATICS_ENGINEERING),
        "情報理工学部",
    ),
    (
        Cource(Department.INFOMATICS_ENGINEERING, evening=True),
        "情報理工学部夜間主コース　先端工学基礎課程",
    ),
    (
        Cource(Department.INFOMATICS_ENGINEERING, graduate=Graduate.MASTER),
        "情報理工学研究科（博士前期課程）",
    ),
    (
        Cource(Department.INFOMATICS_ENGINEERING, graduate=Graduate.DOCTOR),
        "情報理工学研究科（博士後期課程）",
    ),
    (
        Cource(Department.ELECTRO_COMMUNICATIONS),
        "電気通信学部",
    ),
    (
        Cource(Department.ELECTRO_COMMUNICATIONS, evening=True),
        "電気通信学部　夜間主コース",
    ),
    (
        Cource(Department.ELECTRO_COMMUNICATIONS, graduate=Graduate.MASTER),
        "電気通信学研究科（博士前期課程）",
    ),
    (
        Cource(Department.ELECTRO_COMMUNICATIONS, graduate=Graduate.DOCTOR),
        "電気通信学研究科（博士後期課程）",
    ),
    (
        Cource(Department.INFORMATION_SYSTEMS, graduate=Graduate.MASTER),
        "情報システム学研究科（博士前期課程）",
    ),
    (
        Cource(Department.INFORMATION_SYSTEMS, graduate=Graduate.DOCTOR),
        "情報システム学研究科（博士後期課程）",
    )
)

COURCE_INDEX = dict(COURCES)

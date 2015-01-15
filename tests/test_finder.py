# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from unittest import TestCase
import six
import uecsyllabus
from uecsyllabus import Department, Cource, Graduate


class FinderTestCase(TestCase):

    def test_list_syllabuses(self):
        finder = uecsyllabus.Finder()
        course = uecsyllabus.Cource(
                uecsyllabus.Department.INFOMATICS_ENGINEERING,
                evening=False,
                graduate=False)

        condition = dict(
            year=2014,
            course=22,
            grade=2,
        )
        syllabuses = finder.search(condition)


class CourceTestCase(TestCase):

    def test_should_to_string(self):
        specs = [
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
        ]

        for spec in specs:
            cource, expected = spec
            self.assertEqual(six.text_type(cource), expected)

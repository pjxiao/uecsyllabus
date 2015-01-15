# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os.path
import logging
import bs4
import six
from unittest import TestCase
from uecsyllabus import html

logger = logging.getLogger(__name__)
HERE_DIR = os.path.dirname(__file__)


class FormTestCase(TestCase):

    def setUp(self):
        logger.debug(html.__file__)
        logger.debug(dir(html))
        with open(os.path.join(HERE_DIR, "pages", "search.html")) as fp:
            docs = bs4.BeautifulSoup(fp)
            form_element = docs.find(id="jikanwariKeywordForm")
            self.form = html.Form.parse(form_element)

    def test_should_fill_values_from_form(self):
        form = self.form

        self.assertEqual(form.fields["_eventId"].value,             "byKeyword")
        self.assertEqual(form.fields["_flowExecutionKey"].value,    "_*****")
        self.assertEqual(form.fields["s_no"].value,                 "0")
        self.assertEqual(form.fields["nendo"].value,                "2014")
        self.assertEqual(form.fields["jikanwariShozokuCode"].value, "21")
        self.assertEqual(form.fields["gakkiKubunCode"].value,       "")
        self.assertEqual(form.fields["kyokanNm"].value,             "")
        self.assertEqual(form.fields["kamokuNm"].value,             "")
        self.assertEqual(form.fields["keyword"].value,              "")
        self.assertEqual(form.fields["nenji"].value,                "")
        self.assertEqual(form.fields["yobi"].value,                 "")
        self.assertEqual(form.fields["jigen"].value,                "")

    def test_should_list_options_from_form(self):
        form = self.form

        expected = [
            html.Option("", "指示なし"),
            html.Option("1", "前学期"),
            html.Option("2", "後学期"),
        ]

        self.assertEqual(form.fields["gakkiKubunCode"].options, expected)

    def test_should_set_action_from_form(self):
        form = self.form
        self.assertEqual(form.action, "/campusweb/campussquare.do")

    def test_should_set_method_from_form(self):
        form = self.form
        self.assertEqual(form.method, html.Method.POST)

    def test_should_covert_to_dict(self):
        form = html.Form()

        form.set("spam", html.Value("ham"))
        form.set("hoge", html.Value("fuga"))
        form.set("foo",  html.Value("bar"))

        self.assertEqual(form.to_dict(), dict(
            spam="ham",
            hoge="fuga",
            foo="bar",
        ))

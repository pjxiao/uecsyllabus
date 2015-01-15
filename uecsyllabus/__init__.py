# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import logging
import six
import bs4
import requests
import collections
from uecsyllabus import html
from uecsyllabus import cource

logger = logging.getLogger(__name__)

DOMAIN = "http://kyoumu.office.uec.ac.jp"

Cource = cource.Cource
Graduate = cource.Graduate
Department = cource.Department


class Syllabus(collections.namedtuple("Syllabus", ("name", "url"))):
    URL_FORMAT = DOMAIN + "/syllabus/{nendo}/{jscd}/{jscd}_{jcd}.html"
    PATTERN = re.compile(r"refer\('(?P<nendo>.*?)','(?P<jscd>.*?)','(?P<jcd>.*?)'\)")
    NAME_INDEX = 5
    REFER_INDEX = 7

    @classmethod
    def from_tr(cls, tr):
        tds = tr.find_all("td")
        refer = tds[cls.REFER_INDEX].find("input").get("onclick")
        return cls(
            tds[cls.NAME_INDEX].text.strip(),
            cls.URL_FORMAT.format(**cls.PATTERN.search(refer).groupdict()))


class Condition(dict):

    CONVERT_TABLE = dict(
        year="nendo",
        course="jikanwariShozokuCode",
        grade="nenji",
    )

    def __init__(self, default, condition):
        for key, value in condition.items():
            default[self.CONVERT_TABLE[key]] = six.text_type(value)

        super(Condition, self).__init__(default)


class Finder(object):

    INDEX_PAGE = DOMAIN + "/campusweb/"
    HEADER = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
    }

    def search(self, condition):
        #return
        session = requests.session()
        r = session.get(self.INDEX_PAGE, headers=self.HEADER, allow_redirects=True)
        doc = bs4.BeautifulSoup(r.text)
        form_elem = doc.find(id="jikanwariKeywordForm")
        form = html.Form.parse(form_elem)

        data = dict(Condition(form.to_dict(), condition))

        r = session.post(DOMAIN + form.action,
                data=data,
                headers=self.HEADER,
                allow_redirects=True)

        doc = bs4.BeautifulSoup(r.text)
        tbl = doc.find("table", attrs={"class":"normal"})
        return map(Syllabus.from_tr, tbl.find("tbody").find_all("tr"))

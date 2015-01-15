import enum
import six
import collections
import logging
import operator

if six.PY2:
    from future_builtins import map, filter

logger = logging.getLogger(__name__)


class Method(enum.Enum):
    GET    = "GET"
    POST   = "POST"
    PUT    = "PUT"
    HEAD   = "HEAD"
    DELETE = "DELETE"

    @classmethod
    def from_string(cls, name):
        name = name.lower()
        if name == "get":    return cls.GET
        if name == "post":   return cls.POST
        if name == "put":    return cls.PUT
        if name == "head":   return cls.HEAD
        if name == "delete": return cls.DELETE


class Option(collections.namedtuple("Option", ("value", "name"))):

    @classmethod
    def from_element(cls, element):
        return cls(element.get("value"), element.contents[0])


class Value(object):

    def __init__(self, value):
        self.value = value


class SelectValue(Value):

    def __init__(self, value, options):
        Value.__init__(self, value)
        self.options = options


def has_name(element):
    return element.get("name") is not None


def has_options(select):
    return len(select.find_all("option")) > 0


def is_selected(option):
    return option.get("selected") is not None


class Form(object):

    def __init__(self, action="", method=None):
        self.fields = {}
        self.action = action
        self.method = method

    def set(self, key, value):
        self.fields[key] = value

    def to_dict(self):
        return dict([(key, value.value) for key, value in self.fields.items()])

    @classmethod
    def parse(cls, element):
        form = Form(action=element.get("action"),
                    method=Method.from_string(element.get("method")))

        for inp in filter(has_name, element.find_all("input")):
            form.set(inp["name"], Value(inp.get("value")))

        for select in filter(has_options,
                        filter(has_name,
                            element.find_all("select"))):
            options = select.find_all("option")
            selected = list(filter(is_selected, options))
            value_element = selected[0] if len(selected) > 0 else options[0]

            value = SelectValue(
                    value_element.get("value"),
                    [Option.from_element(opt) for opt in options])
            form.set(select["name"], value)


        return form

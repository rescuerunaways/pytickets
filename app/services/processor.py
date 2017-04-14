from json import loads, dumps


def process_one(txt):
    return dumps(_convert_one(loads(txt)))


def process_list(txt):
    return dumps(_convert_list(loads(txt)))


def _convert_one(data):
    return list(map(_m, [data["ticket"]]))


def _convert_list(data):
    return list(map(_m, data["tickets"]))


def _m(x):
    return {"id": x["id"], "subject": x["subject"]}

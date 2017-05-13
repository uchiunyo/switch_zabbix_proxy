# coding:utf-8

import json, urllib2, re, sys

class ZabbixAPI:

  def __init__(self, _url):
    self.jsonrpc = "2.0"
    self.id = 1
    self.auth = "null"

    _m = re.match(r"^http.*\/$", _url)
    if _m:
      self.url = _url + "api_jsonrpc.php"
    else:
      self.url = _url + "/api_jsonrpc.php"

  def login(self, _user, _password):
    _method = "user.login"
    _params = {
      "user": _user,
      "password": _password
    }

    res = self.execute(_method, _params)
    self.auth = res

  def execute(self, _method, _params):
    _headers = {"Content-Type":"application/json-rpc"}
    _tmp_body = {
      "jsonrpc": self.jsonrpc,
      "method": _method,
      "params": _params,
      "id": self.id
    }

    if _method != "user.login":
      _tmp_body["auth"] = self.auth

    try:
      _body = json.dumps(_tmp_body)
      
      request = urllib2.Request(self.url, _body, _headers)
      response = json.loads(urllib2.urlopen(request).read())
    except Exception as e:
      print(e)
      sys.exit()

    return response["result"]

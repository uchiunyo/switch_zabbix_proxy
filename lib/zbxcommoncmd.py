def get_hostid(_zbx, _host):
  _params = {
    "output": ["host", "hostid"],
    "filter": {
      "host": [_host]
    },
  }

  result = _zbx.execute("host.get", _params)
  print(result)
  if len(result) == 0 :
    res = None
  else:
    res = result[0]["hostid"]

  return res

def get_hostids(zbx, hostids):
  pass

def get_use_proxy_hostids(_zbx, _proxyid):
  _params = {
    "output": ["host", "hostid"],
    "filter": {
      "proxy_hostid": _proxyid
    },
  }

  _results = _zbx.execute("host.get", _params)
  _res = []

  for _result in _results:
    _res.append(_result["hostid"])

  return _res


def get_templateid():
  pass

def get_templateids():
  pass

def update_hosts(_zbx, _hostids, kv):
  _hosts = []

  for hostid in _hostids:
    _hosts.append({"hostid":hostid},)

  _params = {
    "hosts": _hosts,
  }
  _params.update(kv)

  _zbx.execute("host.massupdate", _params)


def get_proxyid(_zbx, _host):
  _params = {
    "output": ["host", "proxyid"],
    "filter": {
      "host": [_host]
    },
  }

  _result = _zbx.execute("proxy.get", _params)
  print(_result)
  if len(_result) == 0 :
    _res = None
  else:
    _res = _result[0]["proxyid"]

  return _res

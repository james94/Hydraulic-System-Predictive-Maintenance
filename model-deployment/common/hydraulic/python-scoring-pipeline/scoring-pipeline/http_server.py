# Copyright 2020 H2O.ai; Proprietary License;  -*- encoding: utf-8 -*-

import sys
import json
import traceback

from tornado import ioloop
from tornado.options import define, options, parse_command_line
import tornado.httpserver
import tornado.web
import tornado.escape
import pandas as pd
from numpy import nan
from numpy import ma
from scoring_h2oai_experiment_0abac7c4_8993_11ea_ae54_0242ac110002 import Scorer

scoring_module_hash = '0abac7c4-8993-11ea-ae54-0242ac110002'

def _convert(a):
    return a.item() if isinstance(a, np.generic) else a

class HTTPHandler(object):
    def __init__(self):
        self.scorer = Scorer()

    def get_hash(self):
        return scoring_module_hash

    def score(self, row, output_margin=False, pred_contribs=False):
        return self.scorer.score([row['psa_bar'] if row['psa_bar'] != None else None ,
row['psb_bar'] if row['psb_bar'] != None else None ,
row['psc_bar'] if row['psc_bar'] != None else None ,
row['psd_bar'] if row['psd_bar'] != None else None ,
row['pse_bar'] if row['pse_bar'] != None else None ,
row['psf_bar'] if row['psf_bar'] != None else None ,
row['fsa_vol_flow'] if row['fsa_vol_flow'] != None else None ,
row['fsb_vol_flow'] if row['fsb_vol_flow'] != None else None ,
row['tsa_temp'] if row['tsa_temp'] != None else None ,
row['tsb_temp'] if row['tsb_temp'] != None else None ,
row['tsc_temp'] if row['tsc_temp'] != None else None ,
row['tsd_temp'] if row['tsd_temp'] != None else None ,
row['pump_eff'] if row['pump_eff'] != None else None ,
row['vs_vib'] if row['vs_vib'] != None else None ,
row['cool_pwr_pct'] if row['cool_pwr_pct'] != None else None ,
row['eff_fact_pct'] if row['eff_fact_pct'] != None else None ,], output_margin, pred_contribs)

    def score_batch(self, rows, output_margin=False, pred_contribs=False):
        columns = [
            pd.Series([r['psa_bar'] if r['psa_bar'] != None else None for r in rows], name='psa_bar', dtype='float32'),
            pd.Series([r['psb_bar'] if r['psb_bar'] != None else None for r in rows], name='psb_bar', dtype='float32'),
            pd.Series([r['psc_bar'] if r['psc_bar'] != None else None for r in rows], name='psc_bar', dtype='float32'),
            pd.Series([r['psd_bar'] if r['psd_bar'] != None else None for r in rows], name='psd_bar', dtype='float32'),
            pd.Series([r['pse_bar'] if r['pse_bar'] != None else None for r in rows], name='pse_bar', dtype='float32'),
            pd.Series([r['psf_bar'] if r['psf_bar'] != None else None for r in rows], name='psf_bar', dtype='float32'),
            pd.Series([r['fsa_vol_flow'] if r['fsa_vol_flow'] != None else None for r in rows], name='fsa_vol_flow', dtype='float32'),
            pd.Series([r['fsb_vol_flow'] if r['fsb_vol_flow'] != None else None for r in rows], name='fsb_vol_flow', dtype='float32'),
            pd.Series([r['tsa_temp'] if r['tsa_temp'] != None else None for r in rows], name='tsa_temp', dtype='float32'),
            pd.Series([r['tsb_temp'] if r['tsb_temp'] != None else None for r in rows], name='tsb_temp', dtype='float32'),
            pd.Series([r['tsc_temp'] if r['tsc_temp'] != None else None for r in rows], name='tsc_temp', dtype='float32'),
            pd.Series([r['tsd_temp'] if r['tsd_temp'] != None else None for r in rows], name='tsd_temp', dtype='float32'),
            pd.Series([r['pump_eff'] if r['pump_eff'] != None else None for r in rows], name='pump_eff', dtype='float32'),
            pd.Series([r['vs_vib'] if r['vs_vib'] != None else None for r in rows], name='vs_vib', dtype='float32'),
            pd.Series([r['cool_pwr_pct'] if r['cool_pwr_pct'] != None else None for r in rows], name='cool_pwr_pct', dtype='float32'),
            pd.Series([r['eff_fact_pct'] if r['eff_fact_pct'] != None else None for r in rows], name='eff_fact_pct', dtype='float32'),
        ]
        pr = self.scorer.score_batch(pd.concat(columns, axis=1), output_margin, pred_contribs).values
        return pr.tolist()

    def get_target_labels(self):
        labels = self.scorer.get_target_labels()
        if labels is None:
            return []
        else:
            return labels.tolist()

    def get_transformed_column_names(self):
        return self.scorer.get_transformed_column_names()

    def get_column_names(self):
        return self.scorer.get_column_names()

def json_rpc_success(id, result):
    return dict(jsonrpc='2.0', id=id, result=result)


def json_rpc_error(id, code, message):
    return dict(jsonrpc='2.0', id=id, error=dict(code=code, message=message))


def handle_json_rpc_request(api_methods, scoring_handler, request):
    if 'id' not in request:
        return json_rpc_error(0, 1, "Bad request: want 'id' in RPC request.")

    request_id = request['id']

    if 'method' not in request:
        return json_rpc_error(request_id, 1, "Bad request: want 'method' in RPC request.")

    method = request['method']

    if not isinstance(method, str):
        return json_rpc_error(request_id, 1, "Bad request: want string 'method', got {}".format(type(method)))

    if method not in api_methods:
        return json_rpc_error(request_id, 1, "Method not found: {}".format(method))

    if 'params' not in request:
        return json_rpc_error(request_id, 1, "Bad request: want 'params' in RPC request.")

    params = request['params']

    if not isinstance(params, dict):
        return json_rpc_error(request_id, 1, "Bad request: want 'params' by-name, got {}".format(type(params)))

    func = getattr(scoring_handler, method)

    try:
        return json_rpc_success(request_id, func(**params))
    except:
        return json_rpc_error(request_id, 1, traceback.format_exc())


# below RobustEncoder duplicated from h2oaicore.systemutils_more, but can't have pyclient with this import.
import numpy as np


class RobustEncoder(json.JSONEncoder):
    def default(self, obj):
        if np.issubdtype(obj, np.integer):
            return int(obj)
        elif np.issubdtype(obj, np.floating):
            if np.isnan(obj):
                return np.finfo(obj.dtype).max
            else:
                return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif obj is None:
            return "None"
        else:
            return super(RobustEncoder, self).default(obj)


class JSONRPCHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')

    def post(self, *args, **kwargs):
        if not self.request.body:
            self.set_status(400)  # Bad request
            return

        scoring_handler = self.application.scoring_handler
        api_methods = self.application.api_methods

        # decode binary string and encode it with 'unicode_escape' in case there are backslashes in column names
        req = json.loads(self.request.body.decode().encode('unicode_escape'))

        res = handle_json_rpc_request(api_methods, scoring_handler, req)

        self.write(json.dumps(res, allow_nan=False, cls=RobustEncoder))


class Server(tornado.web.Application):
    def __init__(self, scoring_handler):
        self.scoring_handler = scoring_handler
        self.api_methods = set(dir(scoring_handler))
        handlers = [
            (r'/rpc', JSONRPCHandler),
        ]
        super(Server, self).__init__(handlers)


def start_http_server(port):
    scoring_handler = HTTPHandler()
    http_server = tornado.httpserver.HTTPServer(Server(scoring_handler))

    print('HTTP scoring service listening on port {}...'.format(port))
    http_server.listen(port)
    ioloop.IOLoop.instance().start()

define('port', default=9090, help='Port to run scoring server on.', type=int)

def main():
    parse_command_line()
    start_http_server(options.port)

if __name__ == "__main__":
    main()


# Copyright 2020 H2O.ai; Proprietary License;  -*- encoding: utf-8 -*-

import sys

sys.path.append('gen-py')

from h2oai_scoring import ScoringService
from h2oai_scoring.ttypes import Row
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from tornado.options import define, options, parse_command_line
import pandas as pd
from numpy import nan
from numpy import ma
from scoring_h2oai_experiment_0abac7c4_8993_11ea_ae54_0242ac110002 import Scorer

scoring_module_hash = '0abac7c4-8993-11ea-ae54-0242ac110002'

def _convert(a):
    return a.item() if isinstance(a, np.generic) else a


class TCPHandler(object):
    def __init__(self):
        self.scorer = Scorer()

    def get_hash(self):
        return scoring_module_hash

    def score(self, row, output_margin=False, pred_contribs=False):
        return self.scorer.score([
            row.psaBar if hasattr(row, 'psaBar') else None,  # psa_bar
            row.psbBar if hasattr(row, 'psbBar') else None,  # psb_bar
            row.pscBar if hasattr(row, 'pscBar') else None,  # psc_bar
            row.psdBar if hasattr(row, 'psdBar') else None,  # psd_bar
            row.pseBar if hasattr(row, 'pseBar') else None,  # pse_bar
            row.psfBar if hasattr(row, 'psfBar') else None,  # psf_bar
            row.fsaVolFlow if hasattr(row, 'fsaVolFlow') else None,  # fsa_vol_flow
            row.fsbVolFlow if hasattr(row, 'fsbVolFlow') else None,  # fsb_vol_flow
            row.tsaTemp if hasattr(row, 'tsaTemp') else None,  # tsa_temp
            row.tsbTemp if hasattr(row, 'tsbTemp') else None,  # tsb_temp
            row.tscTemp if hasattr(row, 'tscTemp') else None,  # tsc_temp
            row.tsdTemp if hasattr(row, 'tsdTemp') else None,  # tsd_temp
            row.pumpEff if hasattr(row, 'pumpEff') else None,  # pump_eff
            row.vsVib if hasattr(row, 'vsVib') else None,  # vs_vib
            row.coolPwrPct if hasattr(row, 'coolPwrPct') else None,  # cool_pwr_pct
            row.effFactPct if hasattr(row, 'effFactPct') else None,  # eff_fact_pct
        ], output_margin, pred_contribs)

    def score_batch(self, rows, output_margin=False, pred_contribs=False):
        columns = [
            pd.Series([r.psaBar if hasattr(r, 'psaBar') else None for r in rows], name='psa_bar', dtype='float32'),
            pd.Series([r.psbBar if hasattr(r, 'psbBar') else None for r in rows], name='psb_bar', dtype='float32'),
            pd.Series([r.pscBar if hasattr(r, 'pscBar') else None for r in rows], name='psc_bar', dtype='float32'),
            pd.Series([r.psdBar if hasattr(r, 'psdBar') else None for r in rows], name='psd_bar', dtype='float32'),
            pd.Series([r.pseBar if hasattr(r, 'pseBar') else None for r in rows], name='pse_bar', dtype='float32'),
            pd.Series([r.psfBar if hasattr(r, 'psfBar') else None for r in rows], name='psf_bar', dtype='float32'),
            pd.Series([r.fsaVolFlow if hasattr(r, 'fsaVolFlow') else None for r in rows], name='fsa_vol_flow', dtype='float32'),
            pd.Series([r.fsbVolFlow if hasattr(r, 'fsbVolFlow') else None for r in rows], name='fsb_vol_flow', dtype='float32'),
            pd.Series([r.tsaTemp if hasattr(r, 'tsaTemp') else None for r in rows], name='tsa_temp', dtype='float32'),
            pd.Series([r.tsbTemp if hasattr(r, 'tsbTemp') else None for r in rows], name='tsb_temp', dtype='float32'),
            pd.Series([r.tscTemp if hasattr(r, 'tscTemp') else None for r in rows], name='tsc_temp', dtype='float32'),
            pd.Series([r.tsdTemp if hasattr(r, 'tsdTemp') else None for r in rows], name='tsd_temp', dtype='float32'),
            pd.Series([r.pumpEff if hasattr(r, 'pumpEff') else None for r in rows], name='pump_eff', dtype='float32'),
            pd.Series([r.vsVib if hasattr(r, 'vsVib') else None for r in rows], name='vs_vib', dtype='float32'),
            pd.Series([r.coolPwrPct if hasattr(r, 'coolPwrPct') else None for r in rows], name='cool_pwr_pct', dtype='float32'),
            pd.Series([r.effFactPct if hasattr(r, 'effFactPct') else None for r in rows], name='eff_fact_pct', dtype='float32'),
        ]
        pr = self.scorer.score_batch(pd.concat(columns, axis=1), output_margin, pred_contribs).values
        return pr.tolist()

    def get_target_labels(self):
        labels = self.scorer.get_target_labels()
        if labels is None:
            return []
        else:
            return labels.astype(str)

    def get_transformed_column_names(self):
        return self.scorer.get_transformed_column_names()

    def get_column_names(self):
        return self.scorer.get_column_names()

    def get_prediction_column_names(self, output_margin=False, pred_contribs=False):
        return self.scorer.get_pred_columns(output_margin, pred_contribs)

def start_tcp_server(port):
    scoring_handler = TCPHandler()
    server = TServer.TForkingServer(
        ScoringService.Processor(scoring_handler),
        TSocket.TServerSocket(port=port),
        TTransport.TBufferedTransportFactory(),
        TBinaryProtocol.TBinaryProtocolFactory(),
    )
    print('TCP scoring service listening on port {}...'.format(port))
    server.serve()


define('port', default=9090, help='Port to run scoring server on.', type=int)

def main():
    parse_command_line()
    start_tcp_server(options.port)


if __name__ == "__main__":
    main()


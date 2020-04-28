# Copyright 2020 H2O.ai; Proprietary License;  -*- encoding: utf-8 -*-

import sys

sys.path.append('gen-py')

from numpy import nan
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from h2oai_scoring import ScoringService
from h2oai_scoring.ttypes import Row

# -----------------------------------------------------------------
# Name           Type      Range                                   
# -----------------------------------------------------------------
# psa_bar        float32   [155.39154052734375, 180.92271423339844]
# psb_bar        float32   [104.40630340576172, 131.58909606933594]
# psc_bar        float32   [0.8402525186538696, 2.0218727588653564]
# psd_bar        float32   [0.0, 10.207067489624023]               
# pse_bar        float32   [8.365800857543945, 9.978510856628418]  
# psf_bar        float32   [8.321526527404785, 9.85659122467041]   
# fsa_vol_flow   float32   [2.018571615219116, 6.7227067947387695] 
# fsb_vol_flow   float32   [8.857513427734375, 10.366250038146973] 
# tsa_temp       float32   [35.31378173828125, 57.89928436279297]  
# tsb_temp       float32   [40.85940170288086, 61.958465576171875] 
# tsc_temp       float32   [38.24573516845703, 59.42316818237305]  
# tsd_temp       float32   [30.39080047607422, 53.06041717529297]  
# pump_eff       float32   [2361.747314453125, 2740.64111328125]   
# vs_vib         float32   [0.5243666768074036, 0.8390666842460632]
# cool_pwr_pct   float32   [1.0720833539962769, 2.840100049972534] 
# eff_fact_pct   float32   [18.2766170501709, 60.7370491027832]    
# -----------------------------------------------------------------

socket = TSocket.TSocket('localhost', 9090)
transport = TTransport.TBufferedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = ScoringService.Client(protocol)
transport.open()

server_hash = client.get_hash()
print('Scoring server hash: '.format(server_hash))

print('Scoring individual rows...')
row1 = Row()
row1.psaBar = '155.6405792236328'  # psa_bar
row1.psbBar = '104.91106414794922'  # psb_bar
row1.pscBar = '0.862698495388031'  # psc_bar
row1.psdBar = '0.00021100000594742596'  # psd_bar
row1.pseBar = '8.370246887207031'  # pse_bar
row1.psfBar = '8.327606201171875'  # psf_bar
row1.fsaVolFlow = '2.0297765731811523'  # fsa_vol_flow
row1.fsbVolFlow = '8.869428634643555'  # fsb_vol_flow
row1.tsaTemp = '35.32681655883789'  # tsa_temp
row1.tsbTemp = '40.87480163574219'  # tsb_temp
row1.tscTemp = '38.30345153808594'  # tsc_temp
row1.tsdTemp = '30.47344970703125'  # tsd_temp
row1.pumpEff = '2367.347900390625'  # pump_eff
row1.vsVib = '0.5243666768074036'  # vs_vib
row1.coolPwrPct = '1.3104666471481323'  # cool_pwr_pct
row1.effFactPct = '29.127466201782227'  # eff_fact_pct

row2 = Row()
row2.psaBar = '155.80593872070312'  # psa_bar
row2.psbBar = '104.676513671875'  # psb_bar
row2.pscBar = '0.846289336681366'  # psc_bar
row2.psdBar = '0.0001268333289772272'  # psd_bar
row2.pseBar = '8.372203826904297'  # pse_bar
row2.psfBar = '8.340726852416992'  # psf_bar
row2.fsaVolFlow = '2.0819649696350098'  # fsa_vol_flow
row2.fsbVolFlow = '8.857513427734375'  # fsb_vol_flow
row2.tsaTemp = '35.39099884033203'  # tsa_temp
row2.tsbTemp = '40.99454879760742'  # tsb_temp
row2.tscTemp = '38.30345153808594'  # tsc_temp
row2.tsdTemp = '30.426250457763672'  # tsd_temp
row2.pumpEff = '2366.353271484375'  # pump_eff
row2.vsVib = '0.533050000667572'  # vs_vib
row2.coolPwrPct = '1.1132166385650635'  # cool_pwr_pct
row2.effFactPct = '29.12849998474121'  # eff_fact_pct

row3 = Row()
row3.psaBar = '155.72216796875'  # psa_bar
row3.psbBar = '104.45262145996094'  # psb_bar
row3.pscBar = '0.862698495388031'  # psc_bar
row3.psdBar = '0.0001268333289772272'  # psd_bar
row3.pseBar = '8.37225341796875'  # pse_bar
row3.psfBar = '8.321526527404785'  # psf_bar
row3.fsaVolFlow = '2.018571615219116'  # fsa_vol_flow
row3.fsbVolFlow = '8.871089935302734'  # fsb_vol_flow
row3.tsaTemp = '35.36501693725586'  # tsa_temp
row3.tsbTemp = '40.972618103027344'  # tsb_temp
row3.tscTemp = '38.246368408203125'  # tsc_temp
row3.tsdTemp = '30.479700088500977'  # tsd_temp
row3.pumpEff = '2369.710693359375'  # pump_eff
row3.vsVib = '0.5330666899681091'  # vs_vib
row3.coolPwrPct = '1.2421833276748657'  # cool_pwr_pct
row3.effFactPct = '18.52898406982422'  # eff_fact_pct

row4 = Row()
row4.psaBar = '155.6614532470703'  # psa_bar
row4.psbBar = '104.88860321044922'  # psb_bar
row4.pscBar = '1.0673456192016602'  # psc_bar
row4.psdBar = '0.0001231666683452204'  # psd_bar
row4.pseBar = '8.370457649230957'  # pse_bar
row4.psfBar = '8.340726852416992'  # psf_bar
row4.fsaVolFlow = '2.083963394165039'  # fsa_vol_flow
row4.fsbVolFlow = '8.874388694763184'  # fsb_vol_flow
row4.tsaTemp = '35.342918395996094'  # tsa_temp
row4.tsbTemp = '40.87480163574219'  # tsb_temp
row4.tscTemp = '38.246368408203125'  # tsc_temp
row4.tsdTemp = '30.437732696533203'  # tsd_temp
row4.pumpEff = '2366.707275390625'  # pump_eff
row4.vsVib = '0.5243666768074036'  # vs_vib
row4.coolPwrPct = '1.3104666471481323'  # cool_pwr_pct
row4.effFactPct = '19.778200149536133'  # eff_fact_pct

row5 = Row()
row5.psaBar = '156.0113067626953'  # psa_bar
row5.psbBar = '104.676513671875'  # psb_bar
row5.pscBar = '0.846289336681366'  # psc_bar
row5.psdBar = '0.0001268333289772272'  # psd_bar
row5.pseBar = '8.37225341796875'  # pse_bar
row5.psfBar = '8.323202133178711'  # psf_bar
row5.fsaVolFlow = '2.0819649696350098'  # fsa_vol_flow
row5.fsbVolFlow = '8.869428634643555'  # fsb_vol_flow
row5.tsaTemp = '35.384334564208984'  # tsa_temp
row5.tsbTemp = '40.87480163574219'  # tsb_temp
row5.tscTemp = '38.31816482543945'  # tsc_temp
row5.tsdTemp = '30.475400924682617'  # tsd_temp
row5.pumpEff = '2366.707275390625'  # pump_eff
row5.vsVib = '0.5334833264350891'  # vs_vib
row5.coolPwrPct = '1.179900050163269'  # cool_pwr_pct
row5.effFactPct = '29.127466201782227'  # eff_fact_pct

score1 = client.score(row1, pred_contribs=False, output_margin=False)
print(score1)
score2 = client.score(row2, pred_contribs=False, output_margin=False)
print(score2)
score3 = client.score(row3, pred_contribs=False, output_margin=False)
print(score3)
score4 = client.score(row4, pred_contribs=False, output_margin=False)
print(score4)
score5 = client.score(row5, pred_contribs=False, output_margin=False)
print(score5)

print('Scoring multiple rows...')
rows = [row1, row2, row3, row4, row5]
scores = client.score_batch(rows, pred_contribs=False, output_margin=False)
print(scores)

print('Retrieve column names')
print(client.get_column_names())

print('Retrieve transformed column names')
print(client.get_transformed_column_names())

print('Retrieve target labels') # will be not empty only for classification problems
print(client.get_target_labels())

transport.close()



# Copyright 2020 H2O.ai; Proprietary License;  -*- encoding: utf-8 -*-

import pandas as pd
import numpy as np
from numpy import nan
from scipy.special._ufuncs import expit
from scoring_h2oai_experiment_0abac7c4_8993_11ea_ae54_0242ac110002 import Scorer

#
# The format of input record to the Scorer.score() method is as follows:
#

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


#
# Create a singleton Scorer instance.
# For optimal performance, create a Scorer instance once, and call score() or score_batch() multiple times.
#
scorer = Scorer()


#
# To score one row at a time, use the Scorer.score() method (this can seem slow due to one-time overhead):
#

print('---------- Score Row ----------')
print(scorer.score([
    '155.6405792236328',  # psa_bar
    '104.91106414794922',  # psb_bar
    '0.862698495388031',  # psc_bar
    '0.00021100000594742596',  # psd_bar
    '8.370246887207031',  # pse_bar
    '8.327606201171875',  # psf_bar
    '2.0297765731811523',  # fsa_vol_flow
    '8.869428634643555',  # fsb_vol_flow
    '35.32681655883789',  # tsa_temp
    '40.87480163574219',  # tsb_temp
    '38.30345153808594',  # tsc_temp
    '30.47344970703125',  # tsd_temp
    '2367.347900390625',  # pump_eff
    '0.5243666768074036',  # vs_vib
    '1.3104666471481323',  # cool_pwr_pct
    '29.127466201782227',  # eff_fact_pct
]))
print(scorer.score([
    '155.80593872070312',  # psa_bar
    '104.676513671875',  # psb_bar
    '0.846289336681366',  # psc_bar
    '0.0001268333289772272',  # psd_bar
    '8.372203826904297',  # pse_bar
    '8.340726852416992',  # psf_bar
    '2.0819649696350098',  # fsa_vol_flow
    '8.857513427734375',  # fsb_vol_flow
    '35.39099884033203',  # tsa_temp
    '40.99454879760742',  # tsb_temp
    '38.30345153808594',  # tsc_temp
    '30.426250457763672',  # tsd_temp
    '2366.353271484375',  # pump_eff
    '0.533050000667572',  # vs_vib
    '1.1132166385650635',  # cool_pwr_pct
    '29.12849998474121',  # eff_fact_pct
]))
print(scorer.score([
    '155.72216796875',  # psa_bar
    '104.45262145996094',  # psb_bar
    '0.862698495388031',  # psc_bar
    '0.0001268333289772272',  # psd_bar
    '8.37225341796875',  # pse_bar
    '8.321526527404785',  # psf_bar
    '2.018571615219116',  # fsa_vol_flow
    '8.871089935302734',  # fsb_vol_flow
    '35.36501693725586',  # tsa_temp
    '40.972618103027344',  # tsb_temp
    '38.246368408203125',  # tsc_temp
    '30.479700088500977',  # tsd_temp
    '2369.710693359375',  # pump_eff
    '0.5330666899681091',  # vs_vib
    '1.2421833276748657',  # cool_pwr_pct
    '18.52898406982422',  # eff_fact_pct
]))
print(scorer.score([
    '155.6614532470703',  # psa_bar
    '104.88860321044922',  # psb_bar
    '1.0673456192016602',  # psc_bar
    '0.0001231666683452204',  # psd_bar
    '8.370457649230957',  # pse_bar
    '8.340726852416992',  # psf_bar
    '2.083963394165039',  # fsa_vol_flow
    '8.874388694763184',  # fsb_vol_flow
    '35.342918395996094',  # tsa_temp
    '40.87480163574219',  # tsb_temp
    '38.246368408203125',  # tsc_temp
    '30.437732696533203',  # tsd_temp
    '2366.707275390625',  # pump_eff
    '0.5243666768074036',  # vs_vib
    '1.3104666471481323',  # cool_pwr_pct
    '19.778200149536133',  # eff_fact_pct
]))
print(scorer.score([
    '156.0113067626953',  # psa_bar
    '104.676513671875',  # psb_bar
    '0.846289336681366',  # psc_bar
    '0.0001268333289772272',  # psd_bar
    '8.37225341796875',  # pse_bar
    '8.323202133178711',  # psf_bar
    '2.0819649696350098',  # fsa_vol_flow
    '8.869428634643555',  # fsb_vol_flow
    '35.384334564208984',  # tsa_temp
    '40.87480163574219',  # tsb_temp
    '38.31816482543945',  # tsc_temp
    '30.475400924682617',  # tsd_temp
    '2366.707275390625',  # pump_eff
    '0.5334833264350891',  # vs_vib
    '1.179900050163269',  # cool_pwr_pct
    '29.127466201782227',  # eff_fact_pct
]))


#
# To score a batch of rows, use the Scorer.score_batch() method (much faster than repeated one-row scoring):
#
print('---------- Score Frame ----------')
columns = [
    pd.Series(['155.6405792236328', '155.80593872070312', '155.72216796875', '155.6614532470703', '156.0113067626953', '156.0288543701172', '155.62217712402344', '155.86865234375', '156.0288543701172', '155.80593872070312', '156.0113067626953', '155.56646728515625', '155.72216796875', '155.56646728515625', '156.0288543701172'], name='psa_bar', dtype='float32'),
    pd.Series(['104.91106414794922', '104.676513671875', '104.45262145996094', '104.88860321044922', '104.676513671875', '104.91106414794922', '104.85285949707031', '104.93064880371094', '104.45262145996094', '104.93362426757812', '104.45262145996094', '104.85285949707031', '104.676513671875', '104.85285949707031', '104.67247772216797'], name='psb_bar', dtype='float32'),
    pd.Series(['0.862698495388031', '0.846289336681366', '0.862698495388031', '1.0673456192016602', '0.846289336681366', '1.0673456192016602', '0.8686583042144775', '0.8402525186538696', '0.8838516473770142', '0.846289336681366', '0.8838516473770142', '1.0683131217956543', '1.0683131217956543', '0.8686583042144775', '0.8402525186538696'], name='psc_bar', dtype='float32'),
    pd.Series(['0.00021100000594742596', '0.0001268333289772272', '0.0001268333289772272', '0.0001231666683452204', '0.0001268333289772272', '0.0001231666683452204', '4.333333345130086e-05', '1.766666719049681e-05', '2.350000067963265e-05', '0.00010083333472721279', '2.350000067963265e-05', '0.00010083333472721279', '0.0001231666683452204', '0.00012599999899975955', '9.983333438867703e-05'], name='psd_bar', dtype='float32'),
    pd.Series(['8.370246887207031', '8.372203826904297', '8.37225341796875', '8.370457649230957', '8.37225341796875', '8.367691993713379', '8.370457649230957', '8.367691993713379', '8.372654914855957', '8.373360633850098', '8.372654914855957', '8.372654914855957', '8.367691993713379', '8.373360633850098', '8.372654914855957'], name='pse_bar', dtype='float32'),
    pd.Series(['8.327606201171875', '8.340726852416992', '8.321526527404785', '8.340726852416992', '8.323202133178711', '8.340726852416992', '8.322537422180176', '8.323202133178711', '8.340726852416992', '8.322537422180176', '8.328641891479492', '8.336845397949219', '8.327606201171875', '8.336845397949219', '8.336845397949219'], name='psf_bar', dtype='float32'),
    pd.Series(['2.0297765731811523', '2.0819649696350098', '2.018571615219116', '2.083963394165039', '2.0819649696350098', '3.22739839553833', '2.063558340072632', '3.22739839553833', '2.0297765731811523', '2.078838348388672', '2.083963394165039', '3.22739839553833', '2.078838348388672', '2.018571615219116', '2.0819649696350098'], name='fsa_vol_flow', dtype='float32'),
    pd.Series(['8.869428634643555', '8.857513427734375', '8.871089935302734', '8.874388694763184', '8.869428634643555', '8.874388694763184', '8.861194610595703', '8.874388694763184', '8.87533187866211', '8.874388694763184', '8.866281509399414', '8.857513427734375', '8.866281509399414', '8.866281509399414', '8.867395401000977'], name='fsb_vol_flow', dtype='float32'),
    pd.Series(['35.32681655883789', '35.39099884033203', '35.36501693725586', '35.342918395996094', '35.384334564208984', '35.32476806640625', '35.39099884033203', '35.32681655883789', '35.36501693725586', '35.342918395996094', '35.33021545410156', '35.32681655883789', '35.355934143066406', '35.355934143066406', '35.32476806640625'], name='tsa_temp', dtype='float32'),
    pd.Series(['40.87480163574219', '40.99454879760742', '40.972618103027344', '40.87480163574219', '40.87480163574219', '40.91365051269531', '40.87480163574219', '40.96274948120117', '41.00728225708008', '40.91365051269531', '41.00728225708008', '40.96274948120117', '40.979984283447266', '41.00728225708008', '40.96274948120117'], name='tsb_temp', dtype='float32'),
    pd.Series(['38.30345153808594', '38.30345153808594', '38.246368408203125', '38.246368408203125', '38.31816482543945', '38.24891662597656', '38.34861755371094', '38.34028244018555', '38.31908416748047', '38.34028244018555', '38.24573516845703', '38.34028244018555', '38.31908416748047', '38.34861755371094', '38.31121826171875'], name='tsc_temp', dtype='float32'),
    pd.Series(['30.47344970703125', '30.426250457763672', '30.479700088500977', '30.437732696533203', '30.475400924682617', '30.475400924682617', '30.414283752441406', '30.475400924682617', '30.417400360107422', '30.470550537109375', '30.417400360107422', '30.475400924682617', '30.417400360107422', '30.47344970703125', '30.479415893554688'], name='tsd_temp', dtype='float32'),
    pd.Series(['2367.347900390625', '2366.353271484375', '2369.710693359375', '2366.707275390625', '2366.707275390625', '2367.16650390625', '2369.710693359375', '2368.343505859375', '2366.41064453125', '2369.017333984375', '2366.353271484375', '2369.710693359375', '2367.16650390625', '2366.707275390625', '2366.353271484375'], name='pump_eff', dtype='float32'),
    pd.Series(['0.5243666768074036', '0.533050000667572', '0.5330666899681091', '0.5243666768074036', '0.5334833264350891', '0.5306166410446167', '0.5334833264350891', '0.5306166410446167', '0.5334833264350891', '0.5243666768074036', '0.531166672706604', '0.5334833264350891', '0.5296666622161865', '0.5306166410446167', '0.5295833349227905'], name='vs_vib', dtype='float32'),
    pd.Series(['1.3104666471481323', '1.1132166385650635', '1.2421833276748657', '1.3104666471481323', '1.179900050163269', '1.3594167232513428', '1.2421833276748657', '1.2561166286468506', '1.179900050163269', '1.3594167232513428', '1.3594167232513428', '1.3594167232513428', '1.1132166385650635', '1.179900050163269', '1.2976833581924438'], name='cool_pwr_pct', dtype='float32'),
    pd.Series(['29.127466201782227', '29.12849998474121', '18.52898406982422', '19.778200149536133', '29.127466201782227', '19.58085060119629', '18.52898406982422', '18.52898406982422', '18.52898406982422', '19.01026725769043', '19.271133422851562', '19.58085060119629', '19.01026725769043', '18.52898406982422', '29.12849998474121'], name='eff_fact_pct', dtype='float32'),
]
df = pd.concat(columns, axis=1)
print(scorer.score_batch(df))

##  Recommended workflow with datatable (fast and consistent with training):
import datatable as dt
dt.Frame(df).to_csv("test.csv")          # turn above dummy frame into a CSV (for convenience)
test_dt = dt.fread("test.csv", na_strings=['', '?', 'None', 'nan', 'NA', 'N/A', 'unknown', 'inf', '-inf', '1.7976931348623157e+308', '-1.7976931348623157e+308'])           # parse test set CSV file into datatable (with consistent NA handling)
preds_df = scorer.score_batch(test_dt)   # make predictions (pandas frame)
dt.Frame(preds_df).to_csv("preds.csv")   # save pandas frame to CSV using datatable


#
# The following lines demonstrate how to obtain per-feature prediction contributions per row. These can be
# very helpful in interpreting the model's predictions for individual observations (rows).
# Note that the contributions are in margin space (link space), so for binomial models the application of the
# final logistic function is omitted, while for multinomial models, the application of the final softmax function is
# omitted and for regression models the inverse link function is omitted (such as exp/square/re-normalization/etc.).
# This ensures that we can provide per-feature contributions that add up to the model's prediction.
# To simulate the omission of the transformation from margin/link space back to the probability or target space,
# and to get the predictions in the margin/link space, enable the output_margin flag. To get the prediction
# contributions, set pred_contribs=True. Note that you cannot provide both flags at the same time.
#

print('---------- Get Per-Feature Prediction Contributions for Row ----------')
print(scorer.score([
    '155.6405792236328',  # psa_bar
    '104.91106414794922',  # psb_bar
    '0.862698495388031',  # psc_bar
    '0.00021100000594742596',  # psd_bar
    '8.370246887207031',  # pse_bar
    '8.327606201171875',  # psf_bar
    '2.0297765731811523',  # fsa_vol_flow
    '8.869428634643555',  # fsb_vol_flow
    '35.32681655883789',  # tsa_temp
    '40.87480163574219',  # tsb_temp
    '38.30345153808594',  # tsc_temp
    '30.47344970703125',  # tsd_temp
    '2367.347900390625',  # pump_eff
    '0.5243666768074036',  # vs_vib
    '1.3104666471481323',  # cool_pwr_pct
    '29.127466201782227',  # eff_fact_pct
], pred_contribs=True))


print('---------- Get Per-Feature Prediction Contributions for Frame ----------')
pred_contribs = scorer.score_batch(df, pred_contribs=True, fast_approx=True)  # per-feature prediction contributions
print(pred_contribs)


#
# The following lines demonstrate how to perform feature transformations without scoring.
# You can use this capability to transform input rows and fit models on the transformed frame
#   using an external ML tool of your choice, e.g. Sparkling Water or H2O.
#

#
# To transform a batch of rows (without scoring), use the Scorer.fit_transform_batch() method:
# This method fits the feature engineering pipeline on the given training frame, and applies it on the validation set,
# and optionally also on a test set.
#

# Transforms given datasets into enriched datasets with Driverless AI features')
#    train - for model fitting (do not use parts of this frame for parameter tuning)')
#    valid - for model parameter tuning')
#    test  - for final model testing (optional)')

print('---------- Transform Frames ----------')

# The target column 'cool_cond_y' has to be present in all provided frames.
df['cool_cond_y'] = pd.Series(['3', '3', '3', '100', '20', '3', '20', '100', '100', '100', '20', '20', '3', '3', '100'], dtype='int32')

#  For demonstration only, do not use the same frame for train, valid and test!
train_munged, valid_munged, test_munged = \
  scorer.fit_transform_batch(train_frame=df, valid_frame=df, test_frame=df)
print(train_munged)  # for model fitting (use entire frame, no cross-validation)
print(valid_munged)  # for model validation (parameter tuning)
print(test_munged)   # for final pipeline testing (one time)

#
# To retrieve the original feature column names, use the Scorer.get_column_names() method:
# This method retrieves the input column names 
#

print('---------- Retrieve column names ----------')
print(scorer.get_column_names())

#
# To retrieve the transformed column names, use the Scorer.get_transformed_column_names() method:
# This method retrieves the transformed column names
#

print('---------- Retrieve transformed column names ----------')
print(scorer.get_transformed_column_names())


#!/usr/bin/env bash

set -o pipefail
set -ex

#
# This example script demonstrates how to communicate with the Driverless AI Scoring Service via HTTP.
# The protocol used is JSON-RPC 2.0.
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

echo "Scoring individual rows..."

curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id": 1,
  "method": "score",
  "params": {
    "row": {
      "psa_bar": "155.86865234375",
      "psb_bar": "104.91106414794922",
      "psc_bar": "1.0658478736877441",
      "psd_bar": "0.0",
      "pse_bar": "8.370246887207031",
      "psf_bar": "8.321526527404785",
      "fsa_vol_flow": "2.018571615219116",
      "fsb_vol_flow": "8.87533187866211",
      "tsa_temp": "35.32476806640625",
      "tsb_temp": "40.96274948120117",
      "tsc_temp": "38.30345153808594",
      "tsd_temp": "30.426250457763672",
      "pump_eff": "2369.710693359375",
      "vs_vib": "0.5306166410446167",
      "cool_pwr_pct": "1.1132166385650635",
      "eff_fact_pct": "29.071916580200195"
    }
  }
}
EOF
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id": 2,
  "method": "score",
  "params": {
    "row": {
      "psa_bar": "155.72216796875",
      "psb_bar": "104.91106414794922",
      "psc_bar": "1.0673456192016602",
      "psd_bar": "2.350000067963265e-05",
      "pse_bar": "8.367691993713379",
      "psf_bar": "8.322537422180176",
      "fsa_vol_flow": "2.0297765731811523",
      "fsb_vol_flow": "8.87533187866211",
      "tsa_temp": "35.319183349609375",
      "tsb_temp": "40.96274948120117",
      "tsc_temp": "38.24573516845703",
      "tsd_temp": "30.414283752441406",
      "pump_eff": "2366.353271484375",
      "vs_vib": "0.5243666768074036",
      "cool_pwr_pct": "1.2976833581924438",
      "eff_fact_pct": "29.12849998474121"
    }
  }
}
EOF
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id": 3,
  "method": "score",
  "params": {
    "row": {
      "psa_bar": "155.86865234375",
      "psb_bar": "104.67247772216797",
      "psc_bar": "0.8574901819229126",
      "psd_bar": "0.0001268333289772272",
      "pse_bar": "8.370457649230957",
      "psf_bar": "8.322537422180176",
      "fsa_vol_flow": "2.0297765731811523",
      "fsb_vol_flow": "8.870305061340332",
      "tsa_temp": "35.33021545410156",
      "tsb_temp": "40.97774887084961",
      "tsc_temp": "38.31121826171875",
      "tsd_temp": "30.470550537109375",
      "pump_eff": "2368.343505859375",
      "vs_vib": "0.5243666768074036",
      "cool_pwr_pct": "1.1132166385650635",
      "eff_fact_pct": "19.01026725769043"
    }
  }
}
EOF
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id": 4,
  "method": "score",
  "params": {
    "row": {
      "psa_bar": "155.56646728515625",
      "psb_bar": "104.93362426757812",
      "psc_bar": "0.8402525186538696",
      "psd_bar": "9.983333438867703e-05",
      "pse_bar": "8.372654914855957",
      "psf_bar": "8.321526527404785",
      "fsa_vol_flow": "3.22739839553833",
      "fsb_vol_flow": "8.866281509399414",
      "tsa_temp": "35.355934143066406",
      "tsb_temp": "40.972618103027344",
      "tsc_temp": "38.31816482543945",
      "tsd_temp": "30.437732696533203",
      "pump_eff": "2367.347900390625",
      "vs_vib": "0.5296666622161865",
      "cool_pwr_pct": "1.179900050163269",
      "eff_fact_pct": "29.071916580200195"
    }
  }
}
EOF
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id": 5,
  "method": "score",
  "params": {
    "row": {
      "psa_bar": "155.56646728515625",
      "psb_bar": "104.8831558227539",
      "psc_bar": "1.0673456192016602",
      "psd_bar": "0.0001268333289772272",
      "pse_bar": "8.372654914855957",
      "psf_bar": "8.321526527404785",
      "fsa_vol_flow": "2.0819649696350098",
      "fsb_vol_flow": "8.869428634643555",
      "tsa_temp": "35.32681655883789",
      "tsb_temp": "40.97774887084961",
      "tsc_temp": "38.31908416748047",
      "tsd_temp": "30.470550537109375",
      "pump_eff": "2366.707275390625",
      "vs_vib": "0.5306166410446167",
      "cool_pwr_pct": "1.2561166286468506",
      "eff_fact_pct": "29.071916580200195"
    }
  }
}
EOF

echo "Scoring multiple rows..."

curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id": 1,
  "method": "score_batch",
  "params": {
    "rows": [
      {
        "psa_bar": "155.86865234375",
        "psb_bar": "104.91106414794922",
        "psc_bar": "1.0658478736877441",
        "psd_bar": "0.0",
        "pse_bar": "8.370246887207031",
        "psf_bar": "8.321526527404785",
        "fsa_vol_flow": "2.018571615219116",
        "fsb_vol_flow": "8.87533187866211",
        "tsa_temp": "35.32476806640625",
        "tsb_temp": "40.96274948120117",
        "tsc_temp": "38.30345153808594",
        "tsd_temp": "30.426250457763672",
        "pump_eff": "2369.710693359375",
        "vs_vib": "0.5306166410446167",
        "cool_pwr_pct": "1.1132166385650635",
        "eff_fact_pct": "29.071916580200195"
      },
      {
        "psa_bar": "155.72216796875",
        "psb_bar": "104.91106414794922",
        "psc_bar": "1.0673456192016602",
        "psd_bar": "2.350000067963265e-05",
        "pse_bar": "8.367691993713379",
        "psf_bar": "8.322537422180176",
        "fsa_vol_flow": "2.0297765731811523",
        "fsb_vol_flow": "8.87533187866211",
        "tsa_temp": "35.319183349609375",
        "tsb_temp": "40.96274948120117",
        "tsc_temp": "38.24573516845703",
        "tsd_temp": "30.414283752441406",
        "pump_eff": "2366.353271484375",
        "vs_vib": "0.5243666768074036",
        "cool_pwr_pct": "1.2976833581924438",
        "eff_fact_pct": "29.12849998474121"
      },
      {
        "psa_bar": "155.86865234375",
        "psb_bar": "104.67247772216797",
        "psc_bar": "0.8574901819229126",
        "psd_bar": "0.0001268333289772272",
        "pse_bar": "8.370457649230957",
        "psf_bar": "8.322537422180176",
        "fsa_vol_flow": "2.0297765731811523",
        "fsb_vol_flow": "8.870305061340332",
        "tsa_temp": "35.33021545410156",
        "tsb_temp": "40.97774887084961",
        "tsc_temp": "38.31121826171875",
        "tsd_temp": "30.470550537109375",
        "pump_eff": "2368.343505859375",
        "vs_vib": "0.5243666768074036",
        "cool_pwr_pct": "1.1132166385650635",
        "eff_fact_pct": "19.01026725769043"
      },
      {
        "psa_bar": "155.56646728515625",
        "psb_bar": "104.93362426757812",
        "psc_bar": "0.8402525186538696",
        "psd_bar": "9.983333438867703e-05",
        "pse_bar": "8.372654914855957",
        "psf_bar": "8.321526527404785",
        "fsa_vol_flow": "3.22739839553833",
        "fsb_vol_flow": "8.866281509399414",
        "tsa_temp": "35.355934143066406",
        "tsb_temp": "40.972618103027344",
        "tsc_temp": "38.31816482543945",
        "tsd_temp": "30.437732696533203",
        "pump_eff": "2367.347900390625",
        "vs_vib": "0.5296666622161865",
        "cool_pwr_pct": "1.179900050163269",
        "eff_fact_pct": "29.071916580200195"
      },
      {
        "psa_bar": "155.56646728515625",
        "psb_bar": "104.8831558227539",
        "psc_bar": "1.0673456192016602",
        "psd_bar": "0.0001268333289772272",
        "pse_bar": "8.372654914855957",
        "psf_bar": "8.321526527404785",
        "fsa_vol_flow": "2.0819649696350098",
        "fsb_vol_flow": "8.869428634643555",
        "tsa_temp": "35.32681655883789",
        "tsb_temp": "40.97774887084961",
        "tsc_temp": "38.31908416748047",
        "tsd_temp": "30.470550537109375",
        "pump_eff": "2366.707275390625",
        "vs_vib": "0.5306166410446167",
        "cool_pwr_pct": "1.2561166286468506",
        "eff_fact_pct": "29.071916580200195"
      }
    ]
  }
}
EOF

echo "Get the input columns"
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id":1,
  "method":"get_column_names",
  "params":{}
}
EOF

echo "Get the transformed columns"
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id":1,
  "method":"get_transformed_column_names",
  "params":{}
}
EOF

echo "Get the target labels"
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id":1,
  "method":"get_target_labels",
  "params":{}
}
EOF
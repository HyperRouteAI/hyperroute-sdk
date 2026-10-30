import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError

ROOT=Path(__file__).resolve().parents[2]
API=json.loads((ROOT/'contract/openapi.json').read_text())
FIX=json.loads((ROOT/'contract/fixtures.json').read_text())


def validator(name):
    return Draft202012Validator({'$ref':'#/components/schemas/'+name,'components':API['components']})


def test_full_evidence_has_a_real_typed_contract():
    value=copy.deepcopy(FIX['full_recommendation'])
    validator('FullRecommendation').validate(value)
    value['best']['evidence']['probes'][0]['score']='not a score'
    with pytest.raises(ValidationError):validator('FullRecommendation').validate(value)


def test_unrated_and_missing_evidence_are_explicit():
    value=copy.deepcopy(FIX['full_recommendation'])
    for key in ['capability','band','cap_lcb','rank']:value['best'][key]=None
    value['best']['unrated']=True
    value['best']['evidence']=None
    validator('FullRecommendation').validate(value)
    del value['best']['evidence']
    with pytest.raises(ValidationError):validator('FullRecommendation').validate(value)


def test_job_terminal_states_require_payloads():
    value={'job':'job-1','state':'done','lane':'recommend','position':None,'eta_ms':0}
    with pytest.raises(ValidationError):validator('RecommendationJob').validate(value)
    value['result']=FIX['recommendation']
    validator('RecommendationJob').validate(value)
    value={'job':'job-1','state':'error','lane':'recommend','position':None,'eta_ms':0,'error':'failed'}
    validator('RecommendationJob').validate(value)


def test_native_instruction_is_typed():
    value=copy.deepcopy(FIX['min_recommendation'])
    value['verdict']='use_native'
    value['instruction']={'variant':'quick','prompt':'Answer briefly.','max_searches':3,'tools':['web_search'],
        'alternatives':[{'variant':'deep','prompt':None,'max_searches':None,'tools':None,'cap_lcb':0.71}]}
    validator('MinRecommendation').validate(value)
    value['instruction']['alternatives'][0]['cap_lcb']='high'
    with pytest.raises(ValidationError):validator('MinRecommendation').validate(value)
    del value['instruction']['alternatives']
    with pytest.raises(ValidationError):validator('MinRecommendation').validate(value)

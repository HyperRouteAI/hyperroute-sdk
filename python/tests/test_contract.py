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

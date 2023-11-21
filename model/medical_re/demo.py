import model.medical_re
import json

from model_re import medical_re

model4s,model4po=medical_re.load_model()
text='据报道,新冠肺炎患者经常会发热，咳嗽，少部分患者会胸闷乏力，其病因包括：1.自身免疫系统缺陷\n2.人传人。'
res=medical_re.get_triples(text,model4s,model4po)
print(json.dumps(res,ensure_ascii=False,indent=True))
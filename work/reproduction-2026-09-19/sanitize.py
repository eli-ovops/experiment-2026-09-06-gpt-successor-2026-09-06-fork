import json,pathlib,re,urllib.parse,hashlib
root=pathlib.Path('outputs/reproduction-2026-09-19'); src=pathlib.Path('work/reproduction-2026-09-19/chatgpt-2026-09-19-163657-browser-sanitized.har')
d=json.loads(src.read_text()); cid='6aae49a9-e7dc-83ee-b66f-fbc1183ff1d6'
def url(v):
 p=urllib.parse.urlsplit(v); path=re.sub(r'[0-9a-f]{8}-[0-9a-f-]{27,}',lambda m:m[0] if m[0]==cid else '[REDACTED-ID]',p.path,flags=re.I)
 return urllib.parse.urlunsplit((p.scheme,p.hostname or '',path,urllib.parse.urlencode([(k,'REDACTED') for k,v in urllib.parse.parse_qsl(p.query)]),''))
allowed={'content-type','content-length','date','x-request-id','request-id','x-oai-request-id','cf-ray','s-cf-origin-ttfb-msec','s-cf-quic-rtt-msec','s-cf-tcp-rtt-msec','s-sa-server-ttfb-msec'}
def headers(h):return [x for x in h if x['name'].lower() in allowed]
entries=[]; rows=[]
for e in d['log']['entries']:
 q=e['request']; a=e['response']; c=a['content']
 n={k:e[k] for k in ['startedDateTime','time','timings']}
 n['request']={'method':q['method'],'url':url(q['url']),'httpVersion':q['httpVersion'],'cookies':[],'headers':headers(q['headers']),'queryString':[{'name':x['name'],'value':'REDACTED'} for x in q.get('queryString',[])],'headersSize':q['headersSize'],'bodySize':q['bodySize']}
 n['response']={'status':a['status'],'statusText':a['statusText'],'httpVersion':a['httpVersion'],'cookies':[],'headers':headers(a['headers']),'content':{k:c[k] for k in ['size','mimeType','compression'] if k in c},'redirectURL':'','headersSize':a['headersSize'],'bodySize':a['bodySize']}
 n['cache']={}; n['comment']='Additional sanitization: bodies, cookies, non-allowlisted headers, query values, unrelated UUIDs and extension metadata omitted. Timings/statuses unchanged.'
 entries.append(n)
 if urllib.parse.urlsplit(q['url']).path=='/backend-api/f/conversation':rows.append({'startUTC':e['startedDateTime'],'status':a['status'],'totalMs':e['time'],'timings':e['timings'],'requestIdentifiers':[h for h in a['headers'] if h['name'].lower() in {'x-oai-request-id','x-request-id','request-id','cf-ray'}]})
out={'log':{'version':'1.2','creator':{'name':'Chrome HAR export + privacy allowlist sanitization','version':'1'},'entries':entries}}
p=root/'chatgpt-2026-09-19-sanitized.har'; p.write_text(json.dumps(out,ensure_ascii=False,indent=2))
(root/'request-details.json').write_text(json.dumps(rows,indent=2))
print(json.dumps({'entries':len(entries),'output_bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'main_request':rows},indent=2))

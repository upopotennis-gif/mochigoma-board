#!/usr/bin/env python3
"""持ち駒検討ボードを作る。
  app.html            … ページ本体（Claude のアーティファクトにもそのまま出せる形）
  source/plans.json   … 先生の名前が入った最初のデータ（公開しない）
  合言葉              … ~/jikanwari-navi/source/staff_password.txt（時間割ナビ教員用と同じ。公開しない）
出力: index.html（app.html を包んだもの）、data.enc.js（plans.json を合言葉で暗号化）
"""
import base64, json, os, pathlib, time
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

ROOT = pathlib.Path(__file__).parent
ITER = 200_000
b64 = lambda b: base64.b64encode(b).decode()

payload = json.loads((ROOT / 'source' / 'plans.json').read_text(encoding='utf-8'))
pw = (pathlib.Path.home() / 'jikanwari-navi' / 'source' / 'staff_password.txt').read_text(encoding='utf-8').strip()
salt, iv = os.urandom(16), os.urandom(12)
key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITER).derive(pw.encode())
ct = AESGCM(key).encrypt(iv, json.dumps(payload, ensure_ascii=False, separators=(',', ':')).encode(), None)
enc = {'salt': b64(salt), 'iv': b64(iv), 'iter': ITER, 'ct': b64(ct), 'ids': [p['id'] for p in payload['plans']]}
(ROOT / 'data.enc.js').write_text('window.ENC = ' + json.dumps(enc) + ';\n', encoding='utf-8')

ver = time.strftime('%Y%m%d%H%M')
app = (ROOT / 'app.html').read_text(encoding='utf-8')
head = ('<!doctype html><html lang="ja"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="robots" content="noindex,nofollow">'
        '<style>:root{color-scheme:light}body{margin:0;font:14px system-ui}img{max-width:100%}[hidden]{display:none!important}</style>'
        f'</head><body><script src="data.enc.js?v={ver}"></script>\n')
(ROOT / 'index.html').write_text(head + app + '\n</body></html>\n', encoding='utf-8')
print('ok', ver, 'plans:', len(payload['plans']))

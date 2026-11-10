# 持ち駒検討ボード

国語科の次年度の持ち駒（誰がどの授業を何コマ持つか）を、案をいくつも作って点検・見比べするページ。同僚と使う。

- 公開URL: https://upopotennis-gif.github.io/mochigoma-board/
- リポジトリ: upopotennis-gif/mochigoma-board（公開。push は SSH）
- Claude のアーティファクト版（共有保存つき）: https://claude.ai/artifact/UtUa4BuShQDPhtrQpE5bRD … app.html をそのまま公開したもの

## 作り
- `app.html` … ページ本体。直すのはここ。先生の名前は入れない（授業の一覧＝教育課程だけ）
- `source/plans.json` … 先生の名前が入った最初のデータ（公開しない。.gitignore 済み）
- `build.py` … app.html を包んで `index.html` を作り、plans.json を合言葉で暗号化して `data.enc.js` に書く
- 合言葉は時間割ナビ教員用と同じ（`~/jikanwari-navi/source/staff_password.txt`）。チャットに書き写さない
- GitHub版は「合言葉でみんなの案とつなぐ」で同期（2026-11-10 本人の希望）。保存先は喫茶レジ・戦績ノートと同じ Firebase kissa-register（匿名認証）の `events/mg-<合言葉から作った番号>/state/board`。案は端末で AES-GCM の暗号にしてから送る（保存先に名前は平文で残らない）。同じ案を同時に動かすと後の保存で上書き
- つながない端末は localStorage だけに保存。「書き出す／読み込む」でも受け渡せる
- 合言葉を変えると保存場所も変わる（前の合言葉でつないだ案は新しい場所に出ない。各端末でつなぎ直すと、その端末に残っている案が新しい場所へ送られる）

## 更新
`python3 build.py` → `git add -A && git commit -m "<何を直したか>" && git push`
index.html と data.enc.js は生成物なので手で直さない。

## データの出どころ
最初の案「R8（2026年度）現行」は Classroom（2026_国語科_教員）の「R8年度時間割案・講師時間数」（2026 時間割案.pdf、R8年度国語科講師時間数）から転記。

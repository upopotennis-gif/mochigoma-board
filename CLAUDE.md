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
- GitHub版は各自の端末（localStorage）に保存。案の受け渡しは「書き出す／読み込む」

## 更新
`python3 build.py` → `git add -A && git commit -m "<何を直したか>" && git push`
index.html と data.enc.js は生成物なので手で直さない。

## データの出どころ
最初の案「R8（2026年度）現行」は Classroom（2026_国語科_教員）の「R8年度時間割案・講師時間数」（2026 時間割案.pdf、R8年度国語科講師時間数）から転記。

# はちおうじ往来（公開手順）
1. GitHubにリポジトリ `hachioji` を作り、このフォルダの中身（`_build` を除く）をすべてアップロード → Settings > Pages で公開。
   公開URLは https://leben-k.github.io/hachioji/ を想定（canonical・sitemap.xml・robots.txt に設定済み）。
2. unei.html の「運営者」欄（運営者名・ハンドルネーム）を入力。
3. 広告枠：`data-slot` の付いた枠内の `slot-placeholder` のdivを、アフィリエイトのコードに置き換え
   （aタグに rel="nofollow sponsored noopener" target="_blank" を付ける）。
4. 連絡先フォームの送信先は Formspree（xeaowndg）設定済み。公開後にテスト送信を1回行う。
5. 店名・施設名・開催時期は代表例です。公開前に公式情報で確認してください。

`_build/` はページ再生成用（python3 gen.py → python3 check.py）。公開時は不要です。

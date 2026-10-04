# はちおうじ往来（公開手順）
1. GitHubにリポジトリ `hachioji` を作り、このフォルダの中身（`_build` を除く。`ads.js` を含む）をすべてアップロード → Settings > Pages で公開。
   公開URLは https://leben-k.github.io/hachioji/ を想定（canonical・sitemap.xml・robots.txt に設定済み）。
2. unei.html の「運営者」欄（運営者名・ハンドルネーム）を入力。
3. 広告枠：広告はHTMLに直接貼らず、Googleスプレッドシート（「ウェブに公開」したCSV）から `ads.js` が読み込んで表示します。
   `ads.js` の `SHEET_CSV_URL` に公開CSVのURLを設定し、管理シート（hachioji_ads_sheet.xlsx）の枠ID（ad1〜ad6、furusato1〜furusato3）ごとに広告コードを貼り、表示を ON にします。OFF／空欄の枠は自動で非表示になります。
4. 連絡先フォームの送信先は Formspree（xeaowndg）設定済み。公開後にテスト送信を1回行う。
5. 店名・施設名・開催時期は代表例です。公開前に公式情報で確認してください。

`_build/` はページ再生成用（python3 gen.py → python3 check.py）。公開時は不要です。

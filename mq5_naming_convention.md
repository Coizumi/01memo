# 🚀 MQL5 命名規則（Naming Convention）仕様書

本仕様書は、EA（Expert Advisor）開発におけるコードの整合性と可読性を維持するための標準ルールです。

### 1. 基本方針
* **原則**: 意味が明確な英単語を使用し、省略形は一般的（`TP`, `SL`, `Pos`, `Vol`等）なものに限定する。
* **記法**: 原則として `PascalCase`（大文字開始）をベースとし、スコープごとに接頭辞や記法を使い分ける。

---

### 2. 識別子ごとの命名ルール

| 分類 | 記法 | ルール・例 | 補填された統一仕様 |
| :--- | :--- | :--- | :--- |
| **入力パラメータ** | `PascalCase` | `EAName`, `MagicNum` | `input`修飾子の変数はすべて大文字開始。 |
| **グローバル変数** | `PascalCase` | `FixedLots`, `BuyTPValue` | 入力値から計算・加工された保持用変数は、末尾に `Val` または `Value` を付与。 |
| **ローカル変数** | `lowerCamelCase` | `currentBarTime`, `orderCount` | 内部処理用変数は小文字開始。`c_symbol`等の記法は廃止し `symbol` 等に統一。 |
| **関数名** | `PascalCase` | `NewOrder`, `LossCut` | 動詞から開始し、処理内容を明確にする。 |
| **クラスインスタンス** | `PascalCase` | `Trade`, `AcctInfo` | MQL5標準ライブラリのインスタンスは一目で役割がわかる名称にする。 |
| **定数 / マクロ** | `UPPER_CASE` | `MAX_ORDERS`, `DEFAULT_LOT` | `#define` や `const` はすべて大文字とアンダースコア。 |

---

### 3. 詳細仕様と整合性の補填

コード内で不整合（揺れ）が見られた箇所を、以下のルールで統一・定義します。

#### A. 内部変数の接頭辞ルール（Reconciled）
ソースコード内で `c_symbol` (current) や `on_chart_spread` (snake_case) が混在していましたが、以下のように統一します。
* **`current...`**: 現在のティックやバーから取得した動的な値（例: `currentPrice`, `currentBalance`）。
* **`is...`**: `bool`型のフラグ変数（例: `isOutOfMoney`, `isOrderStopped`）。

#### B. 通貨・ポイント変換の命名統一
`Points`, `Value`, `Rate` の使い分けを明確化します。
* **`...Points`**: ユーザー入力の整数値（Pips/Points単位）。
* **`...Value`**: 内部計算で使用する `_Point` 乗算後の実数値。
* **`...Rate` / `...Pct`**: 比率やパーセンテージ（例: `TargetLossPct`）。

#### C. 関数名の役割定義
* **`Check...`**: `bool`型を返し、条件の成否を確認する（例: `CheckMoneyForTrade`）。
* **`Get...` / `Calculate...`**: 値を取得・計算して返す。
* **`On...`**: MQL5標準イベントハンドラ（例: `OnInit`, `OnTick`）。

---

### 4. 命名例の比較（Before ➔ After）

整合性を補填した修正後のイメージです。

| 箇所 | 修正前（コード内の揺れ） | 修正後（統一仕様） | 理由 |
| :--- | :--- | :--- | :--- |
| グローバル | `SymMag`, `FixedLots` | (維持) | PascalCaseで統一されているため。 |
| ローカル | `c_symbol`, `c_balance` | `symbol`, `currentBalance` | `c_`接頭辞を廃止し、意味を明確化。 |
| ローカル | `on_chart_spread` | `chartSpread` | `snake_case`を排除し`lowerCamelCase`へ。 |
| ローカル | `pf_ls` | `floatingLossPct` | 略語を避け、単位（％）を明示。 |
| 関数 | `Lunar` | `CheckTargetProfit` | 処理内容（目標利益確認）が推測可能な名称へ。 |

---

### 5. ディレクトリ・ファイル命名
* **ファイル名**: `PascalCase` を使用。
    * `SearchLightCfd.mq5` （アンダースコアを排除し、単語を繋げる）
* **バージョン管理**: 末尾に `_v7` 形式で付与。

---


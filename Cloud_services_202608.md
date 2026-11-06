# 主要クラウドサービスの動向（2026年8月）

> **対象時点：2026年8月21日**  
> 本稿は各社の直近の決算発表と公式リリースをもとに、主要クラウドの変化を整理したものです。四半期・会計年度の区切りは各社で異なります。

## 1. Amazon Web Services（AWS）の動向

- **大きな変化**
  - AWSの2026年第2四半期売上高は422億ドルで前年同期比37%増、営業利益は166億ドルでした。売上成長率は18四半期ぶりの高水準で、AI需要がインフラ利用の拡大につながっています。[Amazonの2026年Q2決算](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Second-Quarter-Results/default.aspx)
  - 生成AIは「モデルを呼び出す」段階から、業務を実行する**エージェントを本番運用する**段階へ移っています。6月のAWS Summit New Yorkでは、Amazon Bedrock AgentCoreに組織内データ・Web・有料情報源への接続、運用時の問題分析、統制機能を追加しました。[AWS公式発表](https://aws.amazon.com/blogs/aws/top-announcements-of-the-aws-summit-in-new-york-2026/)
  - Bedrock Managed Knowledge BaseやWeb Searchのように、RAG、検索、ガバナンスをマネージドで組み合わせる機能が増えています。AIアプリの差別化点はモデルそのものだけでなく、社内データの接続、権限管理、監査可能性へと移りつつあります。

- **小さな変化**
  - AgentCoreは7月時点で9リージョンに一般提供され、エージェント作成時のログ設定も標準化が進みました。[AgentCoreリリースノート](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html)
  - AI向けデータセンター投資が大きく、Amazon全体の直近12か月のフリーキャッシュフローは76億ドルの流出です。クラウド利用者側でも、GPU・推論利用量、データ転送、検索・ツール実行をまとめて可視化するFinOpsが重要になります。[Amazonの2026年Q2決算](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Second-Quarter-Results/default.aspx)

---

## 2. Google Cloud Platform（GCP）の動向

- **大きな変化**
  - Alphabetの2026年第2四半期では、Google Cloud売上高が前年同期比82%増となりました。会社はAIインフラストラクチャとAIソリューションの需要を主因に挙げており、Gemini EnterpriseはFortune 100の約90%で採用されています。[Alphabetの2026年Q2発表](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm)
  - Google Cloud Next '26で掲げた「Agentic Data Cloud」を具体化し、8月にはデータベースの初期構築を支援するOnboarding Agentと、監視・障害対応を支援するObservability Agentを公開しました。AlloyDB、Cloud SQL、Spannerなどで、運用作業の自動化を狙います。[Google Cloud公式ブログ](https://cloud.google.com/blog/products/databases/deep-dive-on-new-ai-powered-database-agents)
  - Googleは3月にクラウド／AIセキュリティ企業Wizの買収を完了しました。Wizは他社クラウドも対象とするため、GCPは自社クラウドへの囲い込みだけでなく、マルチクラウドの可視化・保護でも競争力を強めています。[Googleによる買収完了発表](https://abc.xyz/investor/news/news-details/2026/Google-Completes-Acquisition-of-Wiz-2026-ta7OaU2uA0/default.aspx)

- **小さな変化**
  - Gemini Enterpriseでは、従量課金版が一般提供され、利用量と月額上限をコンソールで管理できるようになりました。AIを部門単位の固定ライセンスだけで導入するのではなく、小規模な業務実験から利用量ベースで広げやすくなっています。[Gemini Enterpriseリリースノート](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes)
  - エージェント／MCPサーバーのカタログ、送信先の許可・拒否ポリシー、トレースやメトリクスも整備されています。MCP連携は便利な反面、権限の過剰付与や意図しない外部実行のリスクがあるため、接続先・ID・監査ログを設計に含める必要があります。[Gemini Enterpriseリリースノート](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes)

---

## 3. その他のサービス

- **Microsoft Azure**
  - Microsoftの2026年度第4四半期（2026年6月期）では、Microsoft Cloud売上高は593億ドル（前年同期比27%増）、Azureおよびその他クラウドサービスは43%増でした。Azureの年間売上高は初めて1,000億ドルを超えています。[Microsoftの2026年度Q4決算](https://www.sec.gov/Archives/edgar/data/789019/000119312526323632/msft-ex99_1.htm)
  - Microsoft Foundryを中心に、GitHubで作成したエージェントを展開し、最適なモデルを選び、TeamsやMicrosoft 365から利用する一連の基盤を打ち出しています。外部モデルもAzureのデータ所在地・企業統制のもとで扱う方針であり、既存のMicrosoft 365、Entra ID、Windows／SQL Server資産を持つ企業にとって導入経路が明確です。[Microsoft Build 2026の発表](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/)

- **Oracle Cloud Infrastructure（OCI）**
  - Oracleの2026年度第4四半期のクラウド売上高は99億ドル（47%増）、うちIaaSは58億ドル（93%増）でした。既存データベースや基幹業務アプリケーションを持つ企業のAI・クラウド移行需要を取り込んでいます。[Oracleの2026年度Q4決算](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Record-Q4-and-FY-2026-Results-Driven-by-Cloud-Infrastructure--Cloud-Applications/)
  - 同社の契約残高（RPO）は6,380億ドルまで拡大しました。一方で、急速なインフラ投資により2026年度のフリーキャッシュフローはマイナス237億ドルです。OCIの急成長は選択肢の広がりを示す一方、長期契約、リージョン、必要GPU容量を早めに確認する重要性も示しています。[Oracleの2026年度Q4決算](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Record-Q4-and-FY-2026-Results-Driven-by-Cloud-Infrastructure--Cloud-Applications/)

---

## まとめ

- **大きな潮流**：クラウド各社の競争軸は、生成AIの提供から、エージェントの本番実行、社内データとの接続、ID・権限・監査までを一体で提供することへ移っています。
- **小さな変化**：従量課金、ログ／トレース、MCPの接続制御、データ所在地の指定といった運用機能が急速に製品化されています。PoCだけでなく、費用上限・監査・障害時の停止手順を最初から定義する必要があります。
- **インフラ面の共通課題**：AI需要を背景に各社は大規模なデータセンター投資を続けています。利用者にとっては、単価比較だけでなく、必要なリージョンでのGPU供給、予約・コミットメント、ネットワーク費用、サービス上限を比較することが重要です。
- **日本企業における選択の目安**：
  - AWS：幅広いIaaS／PaaSとBedrock中心の、モデル選択肢を保ったエージェント基盤
  - Azure：Microsoft 365、Entra ID、既存Windows・SQL Server資産との統合
  - GCP：データ分析基盤、Gemini、Google Workspaceを横断したAI・データ活用
  - OCI：Oracle Database／業務アプリケーションを起点としたクラウド移行と高性能IaaS

2026年8月時点の最大のテーマは、**「AIを使えるか」ではなく、「AIエージェントを安全に業務へ接続し、費用と品質を継続的に運用できるか」**です。単一クラウドへの集約かマルチクラウドかという二択ではなく、データの所在、既存ID、必要なAIモデル、運用責任の境界を基準にサービスを組み合わせる局面に入っています。


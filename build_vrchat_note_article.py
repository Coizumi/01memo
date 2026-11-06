from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_BREAK

OUT = r"D:\dev\01memo\VRChat_自作小物をアバターに取り入れる手順_Note記事原稿.docx"

NAVY = "233B53"
BLUE = "2878B5"
SKY = "EAF4FB"
PALE = "F5F7F9"
GOLD = "E0A12B"
GRAY = "66717C"
BLACK = "202428"
WHITE = "FFFFFF"

def set_font(run, size=11, bold=False, color=BLACK, italic=False):
    run.font.name = "Yu Gothic"
    run._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), "Yu Gothic")
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = RGBColor.from_string(color)

def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = tcPr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tcPr.append(shd)
    shd.set(qn("w:fill"), fill)

def cell_margins(cell, top=120, start=150, bottom=120, end=150):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcMar = tcPr.first_child_found_in("w:tcMar")
    if tcMar is None:
        tcMar = OxmlElement("w:tcMar")
        tcPr.append(tcMar)
    for m, v in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tcMar.find(qn(f"w:{m}"))
        if node is None:
            node = OxmlElement(f"w:{m}")
            tcMar.append(node)
        node.set(qn("w:w"), str(v)); node.set(qn("w:type"), "dxa")

def keep_with_next(p):
    p.paragraph_format.keep_with_next = True

def add_p(doc, text="", size=11, bold=False, color=BLACK, italic=False, after=7, before=0, align=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.line_spacing = 1.25
    if align is not None: p.alignment = align
    r = p.add_run(text); set_font(r, size, bold, color, italic)
    return p

def add_h(doc, text, level=1):
    p = doc.add_paragraph(style=f"Heading {level}")
    p.add_run(text)
    keep_with_next(p)
    return p

def add_bullet(doc, text, level=0):
    p = doc.add_paragraph(style="List Bullet" if level == 0 else "List Bullet 2")
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.2
    r = p.add_run(text); set_font(r, 10.5)
    return p

def add_step(doc, num, title, body):
    t = doc.add_paragraph()
    t.paragraph_format.space_before = Pt(10); t.paragraph_format.space_after = Pt(3)
    t.paragraph_format.keep_with_next = True
    r = t.add_run(f"STEP {num}  {title}"); set_font(r, 13, True, BLUE)
    add_p(doc, body, 10.8, after=7)

def add_callout(doc, label, text, fill=SKY, accent=BLUE):
    table = doc.add_table(rows=1, cols=1)
    table.autofit = False; table.columns[0].width = Inches(6.5)
    cell = table.cell(0,0); shade(cell, fill); cell_margins(cell, 160, 190, 160, 190)
    p = cell.paragraphs[0]; p.paragraph_format.space_after = Pt(3)
    r = p.add_run(label); set_font(r, 10, True, accent)
    p2 = cell.add_paragraph(); p2.paragraph_format.space_after = Pt(0); p2.paragraph_format.line_spacing = 1.2
    r2 = p2.add_run(text); set_font(r2, 10.5)
    add_p(doc, "", after=2)

def add_image_placeholder(doc, caption):
    table = doc.add_table(rows=1, cols=1)
    table.autofit = False; table.columns[0].width = Inches(6.5)
    c = table.cell(0,0); shade(c, PALE); cell_margins(c, 260, 180, 260, 180)
    p = c.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("IMAGE  |  画像挿入ポイント"); set_font(r, 10, True, GRAY)
    p2 = c.add_paragraph(); p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r2 = p2.add_run(caption); set_font(r2, 9.5, False, GRAY)
    add_p(doc, "", after=3)

def add_check(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(.12); p.paragraph_format.space_after = Pt(4)
    r = p.add_run("□  " + text); set_font(r, 10.5)

doc = Document()
sec = doc.sections[0]
sec.top_margin = Inches(.8); sec.bottom_margin = Inches(.75)
sec.left_margin = Inches(1); sec.right_margin = Inches(1)
sec.header_distance = Inches(.35); sec.footer_distance = Inches(.35)

styles = doc.styles
normal = styles["Normal"]
normal.font.name = "Yu Gothic"; normal._element.rPr.rFonts.set(qn("w:eastAsia"), "Yu Gothic")
normal.font.size = Pt(11); normal.font.color.rgb = RGBColor.from_string(BLACK)
normal.paragraph_format.space_after = Pt(7); normal.paragraph_format.line_spacing = 1.25
for i, size in [(1,17),(2,14),(3,12)]:
    s = styles[f"Heading {i}"]
    s.font.name = "Yu Gothic"; s._element.rPr.rFonts.set(qn("w:eastAsia"), "Yu Gothic")
    s.font.size = Pt(size); s.font.bold = True
    s.font.color.rgb = RGBColor.from_string(BLUE if i < 3 else NAVY)
    s.paragraph_format.space_before = Pt(16 if i==1 else 11)
    s.paragraph_format.space_after = Pt(7 if i==1 else 5)
    s.paragraph_format.keep_with_next = True
for sty in ["List Bullet", "List Bullet 2"]:
    s=styles[sty]; s.font.name="Yu Gothic"; s._element.rPr.rFonts.set(qn("w:eastAsia"),"Yu Gothic")
    s.font.size=Pt(10.5)

# Header / footer
hp = sec.header.paragraphs[0]
hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
hr = hp.add_run("VRChat アバター改変ガイド | Note記事原稿"); set_font(hr, 8.5, False, GRAY)
fp = sec.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
fr = fp.add_run("2026年7月版  |  公開前に公式ドキュメントの更新をご確認ください"); set_font(fr, 8, False, GRAY)

# Editorial cover
add_p(doc, "BEGINNER'S CREATION GUIDE", 10, True, GOLD, after=28, align=WD_ALIGN_PARAGRAPH.CENTER)
add_p(doc, "VRChatで自作の小物を\nアバターに取り入れる手順", 27, True, NAVY, after=12, align=WD_ALIGN_PARAGRAPH.CENTER)
add_p(doc, "Blenderなどで作ったアクセサリーをUnityへ読み込み、\n位置合わせ・追従設定・テスト・アップロードまで進める初心者向けガイド", 12.5, False, GRAY, after=30, align=WD_ALIGN_PARAGRAPH.CENTER)
add_callout(doc, "この記事でできること", "帽子、メガネ、バッジ、手持ち風アクセサリーなどの「動かない小物」を、アバターの頭・胸・手などに追従させてVRChatへ持ち込めるようになります。", "FFF7E6", GOLD)
add_p(doc, "想定読者：Unityでアバターを一度アップロードしたことがある方／初めて小物改変に挑戦する方", 9.5, False, GRAY, after=4, align=WD_ALIGN_PARAGRAPH.CENTER)
add_p(doc, "所要時間の目安：30〜60分（モデリング時間を除く）", 9.5, True, BLUE, after=8, align=WD_ALIGN_PARAGRAPH.CENTER)
doc.add_page_break()

add_h(doc, "はじめに：小物追加は「置く」＋「追従させる」", 1)
add_p(doc, "自作した小物をVRChatへ持ち込む作業は、難しそうに見えて基本はシンプルです。Unityのアバタープロジェクトへモデルとテクスチャを読み込み、アバターの体に合うよう調整し、追従させたいボーンの子にします。最後にSDKでテストしてアップロードすれば完了です。")
add_callout(doc, "この記事の前提", "ここでは「すでにアップロードできるアバターがUnityのSceneにある」状態から始めます。小物はボーンや揺れを持たない静的なメッシュを想定しています。衣装の着せ替えやスキニング済み小物は別の工程が必要です。")

add_h(doc, "準備するもの", 1)
for x in [
    "VRChat Creator Companion（VCC）で作成・管理したAvatarプロジェクト",
    "VRChat対応のUnity（バージョンはVCCと公式ページで確認）",
    "VRChat SDK - Avatars（VCCのAvatarテンプレートに含まれます）",
    "アップロード可能なVRChat.comアカウント（New User以上）",
    "小物モデル（例：FBX）とテクスチャ画像（例：PNG）",
    "改変前のUnityプロジェクトのバックアップ"
]: add_bullet(doc, x)
add_callout(doc, "重要", "2026年7月の公式案内では対応Unityは2022.3.22f1です。ただし対応バージョンは将来変わる可能性があります。Unity Hubから任意の最新版を入れるのではなく、VCC経由で開くのが安全です。", "FFF0F0", "B64B4B")

add_h(doc, "全体の流れ", 1)
for i,x in enumerate(["プロジェクトをバックアップ","小物データをAssetsへ読み込む","マテリアルを整える","Sceneへ置いてサイズと位置を合わせる","追従先ボーンの子にする","SDKで確認・ローカルテスト","問題がなければアップロード"],1):
    add_p(doc, f"{i}.  {x}", 10.8, bold=(i in [1,6,7]), color=NAVY, after=3)

add_h(doc, "手順", 1)
add_step(doc, 1, "プロジェクトをバックアップする", "VCCのProjects画面で対象プロジェクトのメニューからバックアップを作成するか、Unityを閉じた状態でプロジェクトフォルダーを複製します。アバター改変では、参照切れや設定の上書きが起きても戻せる状態を先に作るのが鉄則です。")
add_callout(doc, "バックアップ名の例", "AvatarName_backup_2026-07-17 のように日付を入れておくと、どの状態へ戻せるか分かりやすくなります。")

add_step(doc, 2, "小物モデルとテクスチャを読み込む", "Projectウィンドウの Assets 配下に Props/小物名 のようなフォルダーを作り、FBXとテクスチャをドラッグ＆ドロップします。素材を小物単位でまとめておくと、後から削除・差し替えしやすくなります。")
add_image_placeholder(doc, "Projectウィンドウ：Assets/Props/MyAccessory にFBX・Textures・Materialsが並んでいる画面")
add_p(doc, "読み込み後はFBXを選択し、Inspectorで次を確認します。", 10.5, bold=True)
for x in ["向きが正しいか（上下・前後が逆になっていないか）","Scale Factorが極端な値になっていないか","不要なAnimationやCamera、Lightが含まれていないか","法線が崩れて表示が黒くなっていないか"]: add_bullet(doc,x)

add_step(doc, 3, "マテリアルを整える", "テクスチャが自動で割り当てられない場合はMaterialを新規作成し、Base Mapなど該当欄へ画像を設定します。小物のRendererにMaterialをドラッグして見た目を確認してください。")
add_callout(doc, "Quest／Android対応の注意", "PC向けシェーダーがAndroidで使えるとは限りません。Quest対応を行う場合は、VRChatのAndroid向け制限に合うシェーダーとテクスチャ設定を選び、Androidへ切り替えて別途ビルド確認します。")

add_step(doc, 4, "Sceneに置いて位置・回転・大きさを合わせる", "Projectから小物FBXまたはPrefabをHierarchyへドラッグします。Sceneビューでアバターを見ながら、TransformのPosition・Rotation・Scaleを調整します。最初は小物をアバター直下に置き、見た目を合わせてからボーンへ移すと作業しやすくなります。")
add_image_placeholder(doc, "Sceneビュー：帽子などの小物をアバターに重ね、Move／Rotate／Scaleツールで調整している画面")
add_callout(doc, "コツ", "正面だけでなく、横・後ろ・上からも確認します。メガネや帽子は少しのめり込みが目立つため、アバターを回転させずSceneビュー側を回して確認すると基準を保ちやすくなります。")

add_step(doc, 5, "追従させたいボーンの子にする", "HierarchyでアバターのArmatureを開き、追従させたいボーンへ小物をドラッグして子にします。頭の小物ならHead、胸元ならChestまたはUpperChest、手に固定するならHandが基本です。子にした後で位置がずれた場合は、Sceneビューで再調整します。")
add_image_placeholder(doc, "Hierarchy：Armature > Hips > Spine > Chest > Neck > Head の配下に小物が入っている画面")
add_h(doc, "よく使う追従先", 2)
for x in ["帽子・メガネ・イヤリング：Head（耳専用ボーンがある場合は構造を確認）","ネックレス・胸バッジ：Chest または UpperChest","背負い物：Chest または UpperChest","手に固定する小物：LeftHand / RightHand","腰のポーチ：Hips"]: add_bullet(doc,x)
add_callout(doc, "注意：手に持つ表現", "Handの子にすると小物は常に手へ固定されます。「必要なときだけ表示」「左右の手を切り替える」「ワールドへ置く」といった動作には、Expression Menu、Animator、Constraintsなど追加設定が必要です。", "FFF7E6", GOLD)

add_step(doc, 6, "不要なコンポーネントと負荷を確認する", "小物に不要なCamera、Light、Audio Source、スクリプトなどが付いていないかInspectorで確認します。メッシュ、マテリアル、テクスチャ、ポリゴン数はアバター全体のPerformance Rankへ加算されます。SDKの表示だけでなく、見た目と負荷のバランスを取りましょう。")
for x in ["使っていないMaterialスロットを減らす","見えない面や過剰なポリゴンを削減する","大きすぎるテクスチャを必要な解像度へ下げる","透明表現を必要最小限にする","同じ小物をHierarchyへ重複配置していないか確認する"]: add_check(doc,x)

add_step(doc, 7, "SDK Control Panelでエラーを確認する", "Unity上部メニューから VRChat SDK > Show Control Panel を開き、Builderタブの警告とエラーを確認します。赤いエラーがある場合は内容を読み、原因を直してから次へ進みます。黄色の警告も、意図したものか確認してください。")
add_image_placeholder(doc, "VRChat SDK Control Panel：BuilderタブでAvatar Performanceと警告一覧を確認している画面")

add_step(doc, 8, "ローカルテストする", "公開前に Build & Test を使い、VRChat内で自分だけが見られるローカルテストを行います。頭や手を動かし、小物が正しく追従するか、視界を遮らないか、身体へ大きくめり込まないかを確認します。アップロード権限がまだなくても、公式案内ではローカルテストは可能です。")
for x in ["立ち姿・しゃがみ・ジャンプで位置が破綻しない","左右を向いたときに頭の小物がずれない","一人称視点を邪魔しない","ミラーで表裏や色がおかしくない","他の衣装や髪と大きく干渉しない"]: add_check(doc,x)

add_step(doc, 9, "アップロードしてVRChatで確認する", "問題がなければSDK Control PanelからBuild & Publishへ進み、名称・説明・サムネイル・公開範囲を確認してアップロードします。既存アバターを更新する場合は、Blueprint IDを意図せず切り離していないかも確認してください。")
add_callout(doc, "公開範囲", "自分だけで使う場合はPrivateのままにします。第三者が使える形で公開・配布・販売する場合は、アバター本体、小物、テクスチャ、フォントなどすべての利用規約と権利関係を別途確認してください。", "FFF0F0", "B64B4B")

add_h(doc, "発展：小物をもっと自然に見せる", 1)
add_h(doc, "揺れを付けたい", 2)
add_p(doc, "チェーン、房飾り、ストラップなどにボーンが入っている場合はVRC PhysBoneで二次動作を付けられます。PhysBoneはボーンの連なりを動かす仕組みです。Root Transform、揺れの強さ、制限、Colliderとの当たり方を小さな値から調整し、必ずテストしてください。")
add_callout(doc, "初心者へのおすすめ", "まずは静的な状態で位置と追従を完成させ、そのコピーにPhysBoneを追加すると、問題の切り分けが簡単です。")
add_h(doc, "メニューでオン／オフしたい", 2)
add_p(doc, "小物GameObjectのActive状態を切り替えるAnimation Clipを作り、FX Animator、Expression Parameters、Expressions Menuへ登録します。パラメーター容量やAnimator構成に影響するため、既存の衣装メニューと重複しない名前を使ってください。")
add_h(doc, "複数の場所へ持ち替えたい", 2)
add_p(doc, "Constraintで親を切り替える、または位置ごとの小物を用意して表示を切り替える方法があります。設定量が増えるため、まずはHeadやHandへの固定で基本動作を確認してから挑戦するのがおすすめです。")

add_h(doc, "うまくいかないときのチェック", 1)
issues = [
    ("小物が巨大／極小", "FBXの単位とScale Factor、Hierarchy上の親オブジェクトのScaleを確認。TransformのScaleを極端な値でごまかさず、可能なら制作ソフト側の単位も整える。"),
    ("動くと置いていかれる", "小物がアバターのボーン配下にあるか確認。Scene直下やアバター直下では、目的の部位の動きに追従しない。"),
    ("ピンク色になる", "MaterialのShaderが見つからない、または対象プラットフォームで非対応。対応シェーダーへ差し替える。"),
    ("片面が消える", "法線が逆、または片面描画。制作ソフトで法線を修正するのが基本。両面描画は負荷との兼ね合いで判断する。"),
    ("アップロードできない", "ConsoleとSDK Control Panelの赤いエラーを上から確認。VRChat.comアカウント、Trust Rank、ログイン状態も確認する。"),
    ("Questでだけ見えない", "Android向けShader・テクスチャ・制限に適合しているか、Androidビルドを作成しているか確認する。")
]
table = doc.add_table(rows=1, cols=2)
table.autofit=False
widths=[Inches(1.65), Inches(4.85)]
for i,w in enumerate(widths): table.columns[i].width=w
for i,txt in enumerate(["症状","確認するポイント"]):
    c=table.rows[0].cells[i]; c.width=widths[i]; shade(c,NAVY); cell_margins(c)
    r=c.paragraphs[0].add_run(txt); set_font(r,10,True,WHITE)
for symptom, fix in issues:
    cells=table.add_row().cells
    for i,(txt,w) in enumerate(zip([symptom,fix],widths)):
        cells[i].width=w; cell_margins(cells[i]); cells[i].vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
        if len(table.rows)%2==0: shade(cells[i],PALE)
        r=cells[i].paragraphs[0].add_run(txt); set_font(r,9.5,i==0)

add_h(doc, "公開前チェックリスト", 1)
for x in [
    "改変前のバックアップを残した",
    "小物が目的のボーン配下にある",
    "正面・横・後ろから位置を確認した",
    "不要なCamera・Light・スクリプトがない",
    "SDKの赤いエラーを解消した",
    "Build & Testで動作確認した",
    "一人称視点を邪魔しない",
    "Performance Rankを確認した",
    "PC／Androidなど対象プラットフォームごとに確認した",
    "利用規約と公開範囲を確認した"
]: add_check(doc,x)

add_h(doc, "まとめ", 1)
add_p(doc, "自作小物をアバターへ入れる基本は、①Assetsへ読み込む、②見た目を整える、③位置を合わせる、④追従先ボーンの子にする、⑤SDKでテストする、の5段階です。最初から揺れやメニュー切替まで盛り込まず、まずは静的な小物を正しく追従させるところまで完成させると、トラブルを切り分けやすくなります。")
add_p(doc, "自分で作った小物が、頭や手の動きに合わせてVRChatの中で動く瞬間は格別です。小さなアクセサリーから始めて、少しずつ表現の幅を広げてみてください。", 11, True, NAVY)

add_h(doc, "記事に添えるハッシュタグ例", 2)
add_p(doc, "#VRChat  #VRChat初心者  #アバター改変  #Unity  #3Dモデリング  #VRC技術記事", 10.5, False, BLUE)

add_h(doc, "参考：公式ドキュメント", 1)
sources = [
    ("VRChat Creation - Creating Your First Avatar", "https://creators.vrchat.com/avatars/creating-your-first-avatar/"),
    ("VRChat Creation - Getting Started", "https://creators.vrchat.com/sdk/"),
    ("VRChat Creation - Current Unity Version", "https://creators.vrchat.com/sdk/upgrade/current-unity-version/"),
    ("VRChat Creation - Avatar Components", "https://creators.vrchat.com/avatars/avatar-components/"),
    ("VRChat Creation - PhysBones", "https://creators.vrchat.com/common-components/physbones/"),
    ("VRChat Creation - Avatars", "https://creators.vrchat.com/avatars/")
]
for title,url in sources:
    p=doc.add_paragraph(style="List Bullet")
    r=p.add_run(title+"\n"); set_font(r,9.5,True,NAVY)
    r2=p.add_run(url); set_font(r2,8.5,False,GRAY)
add_p(doc, "※画面構成、対応Unity、SDK仕様、アップロード条件は更新されることがあります。公開前・作業前に上記公式ページで最新情報をご確認ください。", 9, False, GRAY, italic=True)

doc.core_properties.title = "VRChatで自作の小物をアバターに取り入れる手順"
doc.core_properties.subject = "Note.com掲載用記事原稿"
doc.core_properties.author = ""
doc.core_properties.keywords = "VRChat, Unity, アバター改変, 小物"
doc.save(OUT)
print(OUT)

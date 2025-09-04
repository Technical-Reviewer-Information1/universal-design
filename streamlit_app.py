import streamlit as st
import plotly.graph_objects as go
import plotly.express as px


def main():
    st.title("ユニバーサルデザインを体験しよう！")
    st.caption("Created by Dit-Lab.(Daiki ITO)")
    st.caption("Supported by Tomoaki ATSUMI")
    
    # ステップ1: はじめに
    show_introduction()
    
    st.divider()
    
    # ステップ2: デザイン比較クイズ
    show_design_quiz()
    
    st.divider()
    
    # ステップ3: シミュレーション
    show_simulation()
    
    st.divider()
    
    # ステップ4: バリアフリーとユニバーサルデザインの違い
    show_difference_explanation()
    
    st.divider()
    
    # ステップ5: 7原則のまとめ
    show_seven_principles()
    


def show_introduction():
    st.header("ステップ1: はじめに - あなたの身の回りにもある「使いやすさ」のデザイン 💡")
    
    st.markdown("""
    **ユニバーサルデザインとは何か？**
    
    ユニバーサルデザインとは、年齢、性別、国籍、障がいの有無などにかかわらず、
    すべての人が使いやすいことを目指すデザインの考え方です。
    
    特別な人のためのものではなく、実は私たちの身近なところにたくさんあります。
    一緒にその世界をのぞいてみましょう！
    """)
    
    # エキスパンダーで身近な例を表示
    with st.expander("身近なユニバーサルデザインの例を見てみよう"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("🚪 **自動ドア**")
            st.write("手がふさがっていても、車椅子でも、誰でも楽に通れます")
            
            st.markdown("📱 **スマートフォンの音声入力**")
            st.write("文字入力が苦手な人も、音声で操作できます")
            
        with col2:
            st.markdown("🚉 **駅のピクトグラム**")
            st.write("言語が違っても、絵を見れば意味がわかります")
            
            st.markdown("✂️ **左右どちらでも使えるハサミ**")
            st.write("利き手に関係なく使えるデザインです")


def show_design_quiz():
    st.header("ステップ2: どっちがユニバーサル？ - デザイン比較クイズ 🤔")
    
    st.subheader("比べてみよう！みんなに優しいデザイン")
    st.write("2つのデザインを比べて、より多くの人にとって使いやすいのはどちらか考えてみましょう。")
    
    # 第1問
    st.subheader("【第1問】Webサイトのボタン")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**デザインA**")
        st.markdown("""
        <div style="background-color: #87CEEB; color: white; padding: 10px; text-align: center; border-radius: 5px; font-size: 12px;">
        クリックしてください
        </div>
        """, unsafe_allow_html=True)
        st.caption("背景: 水色、文字: 白、小さい文字")
    
    with col2:
        st.markdown("**デザインB**")
        st.markdown("""
        <div style="background-color: #191970; color: white; padding: 15px; text-align: center; border-radius: 5px; font-size: 16px; font-weight: bold;">
        クリックしてください
        </div>
        """, unsafe_allow_html=True)
        st.caption("背景: 紺色、文字: 白、大きい文字")
    
    question1 = st.radio("どちらのデザインが見やすいですか？", ("デザインA", "デザインB"), key="q1")
    
    if st.button("第1問の答えを確認", key="ans1"):
        if question1 == "デザインB":
            st.success("正解！ ✅")
        else:
            st.info("答え：デザインB")
        
        st.markdown("""
        **解説：** 色のコントラストをはっきりさせ、文字を大きくすることで、
        視力が弱い方や高齢者だけでなく、明るい屋外でスマートフォンを見る人にとっても
        見やすくなります。これはアクセシビリティ（情報の得やすさ）を高める工夫です。
        """)
    
    st.markdown("---")
    
    # 第2問
    st.subheader("【第2問】施設の案内表示")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**デザインA**")
        st.markdown("""
        <div style="border: 2px solid #333; padding: 20px; text-align: center; background-color: white;">
        <h3 style="margin: 0; color: #333;">Toilet</h3>
        </div>
        """, unsafe_allow_html=True)
        st.caption("英語のみの表示")
    
    with col2:
        st.markdown("**デザインB**")
        st.markdown("""
        <div style="border: 2px solid #333; padding: 20px; text-align: center; background-color: white;">
        <h3 style="margin: 0; color: #333;">トイレ</h3>
        <div style="font-size: 30px;">🚻</div>
        </div>
        """, unsafe_allow_html=True)
        st.caption("日本語 + ピクトグラム")
    
    question2 = st.radio("海外から来た旅行者にも分かりやすいのは？", ("デザインA", "デザインB"), key="q2")
    
    if st.button("第2問の答えを確認", key="ans2"):
        if question2 == "デザインB":
            st.success("正解！ ✅")
        else:
            st.info("答え：デザインB")
        
        st.markdown("""
        **解説：** ピクトグラム（絵文字）を使うことで、その言語が読めない人や、
        文字を認識しにくい子どもでも、一目で意味を理解できます。
        言葉の壁を越えるユニバーサルデザインの代表例です。
        """)


def show_simulation():
    st.header("ステップ3: もし、あなたが…？ - 視点を変えるシミュレーション 👓")
    
    st.subheader("いろいろな「見え方」「使い方」を体験する")
    st.write("いつもと同じWebページも、見る人や状況によって使いやすさが変わります。プルダウンで状況を選んで、見え方の違いを体験してみてください。")
    
    # サンプルWebページコンテンツ
    st.markdown("### サンプルWebページ")
    
    situation = st.selectbox("あなたの状況を選んでください", 
                           ["通常の見え方", "色の見え方が少し違うかも", "ちょっと視力が落ちてきたかも"])
    
    if situation == "通常の見え方":
        st.markdown("""
        <div style="padding: 20px; border: 1px solid #ddd; border-radius: 10px; background-color: white;">
        <h4 style="color: black;">商品購入ページ</h4>
        <p style="color: black;"><span style="color: red; font-weight: bold;">注意！</span> この商品の在庫が残り少なくなっています。</p>
        <p style="color: black;">この商品は<span style="color: green; font-weight: bold;">緑色のボタン</span>から購入できます。</p>
        <button style="background-color: green; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">購入する</button>
        </div>
        """, unsafe_allow_html=True)
        
    elif situation == "色の見え方が少し違うかも":
        st.markdown("""
        <div style="padding: 20px; border: 1px solid #ddd; border-radius: 10px; background-color: white;">
        <h4 style="color: black;">商品購入ページ</h4>
        <p style="color: black;"><span style="color: #8B4513; font-weight: bold;">注意！</span> この商品の在庫が残り少なくなっています。</p>
        <p style="color: black;">この商品は<span style="color: #8B4513; font-weight: bold;">ボタン</span>から購入できます。</p>
        <button style="background-color: #8B4513; color: white; padding: 10px 20px; border: none; border-radius: 5px;">購入する</button>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("""
        **解説：** 色だけで情報を伝えると、一部の人には区別がつきにくいことがあります。
        「太字にする」「下線を引く」「アイコンを使う」など、色以外の要素を加えることが大切です。
        """)
        
    elif situation == "ちょっと視力が落ちてきたかも":
        st.markdown("""
        <div style="padding: 20px; border: 1px solid #ddd; border-radius: 10px; background-color: white;">
        <h4 style="color: black; font-size: 12px; opacity: 0.7;">商品購入ページ</h4>
        <p style="color: black; font-size: 10px; opacity: 0.7;"><span style="color: red; font-weight: bold;">注意！</span> この商品の在庫が残り少なくなっています。</p>
        <p style="color: black; font-size: 10px; opacity: 0.7;">この商品は<span style="color: green; font-weight: bold;">緑色のボタン</span>から購入できます。</p>
        <button style="background-color: green; color: white; padding: 5px 10px; border: none; border-radius: 5px; font-size: 10px;">購入する</button>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("""
        **解説：** 誰もがいつでもくっきり文字が見えるわけではありません。
        利用者が自分で文字サイズを簡単に変更できる機能は、とても重要なアクセシビリティです。
        """)


def show_difference_explanation():
    st.header("ステップ4: 「バリアフリー」と「ユニバーサルデザイン」の違いって？")
    
    # 分かりやすい比較表を追加
    st.markdown("""
    ### 🤔 どちらも「使いやすくする」けれど、考え方が違います
    """)
    
    # 比較表をHTMLで作成（ダークテーマ対応）
    st.markdown("""
    <div style="margin: 20px 0;">
        <table style="width: 100%; border-collapse: collapse; font-size: 16px; background-color: white;">
            <tr style="background-color: #f0f2f6;">
                <th style="padding: 15px; border: 2px solid #333; text-align: center; color: black;"></th>
                <th style="padding: 15px; border: 2px solid #333; text-align: center; background-color: #ffe6cc; color: black;">🔧 バリアフリー</th>
                <th style="padding: 15px; border: 2px solid #333; text-align: center; background-color: #e6ffe6; color: black;">🌟 ユニバーサルデザイン</th>
            </tr>
            <tr>
                <td style="padding: 15px; border: 1px solid #333; font-weight: bold; background-color: #f8f9fa; color: black;">考え方</td>
                <td style="padding: 15px; border: 1px solid #333; background-color: white; color: black;">問題が<strong>起きてから</strong>解決</td>
                <td style="padding: 15px; border: 1px solid #333; background-color: white; color: black;">最初から問題が<strong>起きないように</strong>設計</td>
            </tr>
            <tr>
                <td style="padding: 15px; border: 1px solid #333; font-weight: bold; background-color: #f8f9fa; color: black;">対象</td>
                <td style="padding: 15px; border: 1px solid #333; background-color: white; color: black;">特定の人（困っている人）</td>
                <td style="padding: 15px; border: 1px solid #333; background-color: white; color: black;">すべての人（誰でも）</td>
            </tr>
            <tr>
                <td style="padding: 15px; border: 1px solid #333; font-weight: bold; background-color: #f8f9fa; color: black;">費用</td>
                <td style="padding: 15px; border: 1px solid #333; background-color: white; color: black;">後から改修するので<strong>高い</strong></td>
                <td style="padding: 15px; border: 1px solid #333; background-color: white; color: black;">最初から設計するので<strong>効率的</strong></td>
            </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🏠 身近な例で比べてみよう！")
    
    # より分かりやすい例を3つのカラムで表示
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="padding: 15px; border: 2px solid #ddd; border-radius: 10px; height: 280px;">
        <h4 style="text-align: center; color: #666;">😓 問題のある設計</h4>
        <div style="text-align: center; margin: 20px 0;">
        🏢<br>
        |||||||<br>
        |||||||<br>
        |||||||<br>
        </div>
        <p style="text-align: center; font-size: 14px;">階段だけの入り口<br>→ 車椅子の人は入れない</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="padding: 15px; border: 2px solid #ff9800; border-radius: 10px; height: 280px; background-color: #fff3e0;">
        <h4 style="text-align: center; color: #f57f17;">🔧 バリアフリー</h4>
        <div style="text-align: center; margin: 20px 0;">
        🏢<br>
        ||||||| 〜〜〜<br>
        ||||||| 〜〜<br>
        ||||||| 〜<br>
        </div>
        <p style="text-align: center; font-size: 14px;"><strong>後から</strong>スロープを追加<br>→ 車椅子の人も入れるように</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="padding: 15px; border: 2px solid #4caf50; border-radius: 10px; height: 280px; background-color: #f1f8e9;">
        <h4 style="text-align: center; color: #2e7d32;">🌟 ユニバーサルデザイン</h4>
        <div style="text-align: center; margin: 20px 0;">
        🏢<br>
        〜〜〜〜〜<br>
        〜〜〜〜<br>
        〜〜〜<br>
        </div>
        <p style="text-align: center; font-size: 14px;"><strong>最初から</strong>緩やかなスロープ<br>→ みんなが楽に入れる</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 📱 スマホアプリの例でも見てみよう")
    
    # インタラクティブな例を追加
    example_choice = st.radio(
        "どちらのアプリが使いやすいですか？",
        ["アプリA: 後から改善", "アプリB: 最初から配慮"]
    )
    
    if example_choice == "アプリA: 後から改善":
        st.markdown("""
        <div style="border: 2px solid #ff9800; border-radius: 10px; padding: 20px; background-color: #fff3e0;">
        <h4 style="color: #f57f17;">📱 アプリA (バリアフリー的アプローチ)</h4>
        <p style="color: black;"><strong>最初:</strong> 英語のみでリリース</p>
        <p style="color: black;"><strong>問題発生:</strong> 「日本語がないから使えない」という苦情</p>
        <p style="color: black;"><strong>対応:</strong> 後から日本語翻訳機能を追加</p>
        <p style="color: black;">💸 <strong>結果:</strong> 翻訳作業に時間とコストがかかる</p>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        st.markdown("""
        <div style="border: 2px solid #4caf50; border-radius: 10px; padding: 20px; background-color: #f1f8e9;">
        <h4 style="color: #2e7d32;">📱 アプリB (ユニバーサルデザインアプローチ)</h4>
        <p style="color: black;"><strong>企画段階:</strong> 「世界中の人が使うかも」と考える</p>
        <p style="color: black;"><strong>設計:</strong> 最初から多言語対応で設計</p>
        <p style="color: black;"><strong>リリース:</strong> 英語・日本語・中国語などに対応済み</p>
        <p style="color: #2e7d32;">✨ <strong>結果:</strong> より多くの人がすぐに使える</p>
        </div>
        """, unsafe_allow_html=True)
    
    # まとめ
    st.markdown("---")
    st.markdown("""
    ### 🎯 つまり...
    
    - **バリアフリー**: 「困っている人がいるから助けよう」→ **優しい後付け対応**
    - **ユニバーサルデザイン**: 「みんなが使えるものを作ろう」→ **賢い最初の設計**
    
    どちらも大切ですが、ユニバーサルデザインの方が効率的で、より多くの人が恩恵を受けられます！
    """)


def show_seven_principles():
    st.header("ステップ5: まとめ - ユニバーサルデザインの7原則")
    
    st.subheader("「みんなのためのデザイン」7つのヒント")
    st.write("ユニバーサルデザインには、デザインを進める上での7つの指針（原則）があります。")
    
    principles = [
        {
            "title": "1. 公平性",
            "description": "誰にでも公平に利用できること",
            "example": "例: 自動ドア",
            "icon": "⚖️"
        },
        {
            "title": "2. 自由度",
            "description": "使い方を選べること",
            "example": "例: 左右どちらの手でも使えるハサミ",
            "icon": "🔄"
        },
        {
            "title": "3. 単純性",
            "description": "使い方が直感的にわかること",
            "example": "例: スイッチの絵表示",
            "icon": "💡"
        },
        {
            "title": "4. 分かりやすさ",
            "description": "必要な情報がすぐに伝わること",
            "example": "例: 駅の案内ピクトグラム",
            "icon": "🔍"
        },
        {
            "title": "5. 安全性",
            "description": "ミスしても危険につながらないこと",
            "example": "例: アイロンの自動電源オフ機能",
            "icon": "🛡️"
        },
        {
            "title": "6. 省体力",
            "description": "少ない力で楽に使えること",
            "example": "例: レバー式のドアノブ",
            "icon": "💪"
        },
        {
            "title": "7. 空間性",
            "description": "誰でもアクセスしやすく、十分な広さがあること",
            "example": "例: 多機能トイレ",
            "icon": "🏠"
        }
    ]
    
    # 3列のレイアウトで7原則を表示
    for i in range(0, len(principles), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(principles):
                principle = principles[i + j]
                with col:
                    st.markdown(f"""
                    <div style="border: 2px solid #4CAF50; border-radius: 10px; padding: 15px; margin: 10px 0; text-align: center; background-color: #f8fff8;">
                        <div style="font-size: 30px;">{principle['icon']}</div>
                        <h4 style="color: #2E7D32; margin: 10px 0;">{principle['title']}</h4>
                        <p style="margin: 8px 0; font-size: 14px;">{principle['description']}</p>
                        <p style="margin: 8px 0; font-size: 12px; color: #666;"><em>{principle['example']}</em></p>
                    </div>
                    """, unsafe_allow_html=True)
    
    st.markdown("""
    ---
    🎉 **この考え方は、モノ作りだけでなく、情報伝達やサービスなど、あらゆる場面で活かすことができます。**
    
    ユニバーサルデザインを意識することで、より多くの人にとって使いやすい世界を作っていけるのです！
    """)
    
    # フォントサイズ体験を7原則の後に追加
    show_font_size_experience()


def show_font_size_experience():
    st.markdown("### 体験してみよう: フォントサイズの違い")
    
    font_size = st.slider("フォントサイズを調整してください", 12, 24, 16)
    
    sample_text = "このテキストの読みやすさはどうですか？"
    
    st.markdown(f"""
    <p style="color: black; font-size: {font_size}px; line-height: 1.6; padding: 20px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9;">
    {sample_text}
    </p>
    """, unsafe_allow_html=True)
    
    if font_size >= 20:
        st.success("大きなフォントサイズ！視力に不安がある人にも読みやすいサイズです。")
    elif font_size >= 16:
        st.info("標準的なサイズ。多くの人にとって読みやすいサイズです。")
    else:
        st.warning("小さなフォントサイズ。一部の人には読みづらいかもしれません。")


if __name__ == "__main__":
    st.set_page_config(
        page_title="ユニバーサルデザイン体験アプリ",
        page_icon="♿",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    main()
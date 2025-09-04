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
    
    # 追加の工夫: インタラクティブなチャート
    show_accessibility_visualization()


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
        <h4>商品購入ページ</h4>
        <p><span style="color: red; font-weight: bold;">注意！</span> この商品の在庫が残り少なくなっています。</p>
        <p>この商品は<span style="color: green; font-weight: bold;">緑色のボタン</span>から購入できます。</p>
        <button style="background-color: green; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">購入する</button>
        </div>
        """, unsafe_allow_html=True)
        
    elif situation == "色の見え方が少し違うかも":
        st.markdown("""
        <div style="padding: 20px; border: 1px solid #ddd; border-radius: 10px; background-color: white;">
        <h4>商品購入ページ</h4>
        <p><span style="color: #8B4513; font-weight: bold;">注意！</span> この商品の在庫が残り少なくなっています。</p>
        <p>この商品は<span style="color: #8B4513; font-weight: bold;">ボタン</span>から購入できます。</p>
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
        <h4 style="font-size: 12px; opacity: 0.7;">商品購入ページ</h4>
        <p style="font-size: 10px; opacity: 0.7;"><span style="color: red; font-weight: bold;">注意！</span> この商品の在庫が残り少なくなっています。</p>
        <p style="font-size: 10px; opacity: 0.7;">この商品は<span style="color: green; font-weight: bold;">緑色のボタン</span>から購入できます。</p>
        <button style="background-color: green; color: white; padding: 5px 10px; border: none; border-radius: 5px; font-size: 10px;">購入する</button>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("""
        **解説：** 誰もがいつでもくっきり文字が見えるわけではありません。
        利用者が自分で文字サイズを簡単に変更できる機能は、とても重要なアクセシビリティです。
        """)


def show_difference_explanation():
    st.header("ステップ4: 「バリアフリー」と「ユニバーサルデザイン」の違いって？")
    
    st.subheader("考え方の違いを知ろう")
    
    tab1, tab2 = st.tabs(["バリアフリー", "ユニバーサルデザイン"])
    
    with tab1:
        st.markdown("### 「障壁（バリア）を取り除く」")
        
        # 簡単な図解をPlotlyで作成
        fig = go.Figure()
        
        # 階段
        fig.add_trace(go.Scatter(
            x=[1, 2, 3, 4], y=[0, 1, 2, 3], mode='lines+markers',
            name='階段（既存）', line=dict(color='gray', width=8),
            marker=dict(size=12, color='gray')
        ))
        
        # 後付けスロープ
        fig.add_trace(go.Scatter(
            x=[0.5, 4.5], y=[0, 3], mode='lines+markers',
            name='後付けスロープ', line=dict(color='orange', width=6, dash='dash'),
            marker=dict(size=10, color='orange')
        ))
        
        fig.update_layout(
            title="バリアフリーのアプローチ",
            xaxis_title="",
            yaxis_title="高さ",
            showlegend=True,
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        **バリアフリーは、後から障壁を取り除くアプローチです。**
        
        例えば、「階段しかないから、車椅子の人のためにスロープを付け加えよう」という発想です。
        特定の誰かのための改善策と言えます。
        """)
    
    with tab2:
        st.markdown("### 「はじめから障壁を作らない」")
        
        # 簡単な図解をPlotlyで作成
        fig = go.Figure()
        
        # 最初からのスロープ
        fig.add_trace(go.Scatter(
            x=[0, 4], y=[0, 3], mode='lines+markers',
            name='緩やかなスロープ', line=dict(color='green', width=8),
            marker=dict(size=12, color='green')
        ))
        
        fig.update_layout(
            title="ユニバーサルデザインのアプローチ",
            xaxis_title="",
            yaxis_title="高さ",
            showlegend=True,
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        **ユニバーサルデザインは、計画の最初から多様な人々を想定するアプローチです。**
        
        「車椅子の人、ベビーカーを押す人、荷物が重い人…みんなが楽だから、
        最初からゆるやかなスロープにしよう」という発想です。
        みんなのためのデザインと言えます。
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


def show_accessibility_visualization():
    st.markdown("---")
    st.header("おまけ: アクセシビリティの重要度を可視化")
    
    st.write("日常生活でのアクセシビリティニーズを、年代別に可視化してみました。")
    
    # 年代別のアクセシビリティニーズデータ
    age_groups = ['10代', '20代', '30代', '40代', '50代', '60代', '70代以上']
    visual_needs = [10, 15, 25, 40, 55, 70, 85]
    mobility_needs = [5, 10, 15, 25, 35, 50, 70]
    cognitive_needs = [20, 15, 20, 25, 30, 40, 50]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='視覚サポート',
        x=age_groups,
        y=visual_needs,
        marker_color='lightblue'
    ))
    
    fig.add_trace(go.Bar(
        name='移動サポート',
        x=age_groups,
        y=mobility_needs,
        marker_color='lightgreen'
    ))
    
    fig.add_trace(go.Bar(
        name='認知サポート',
        x=age_groups,
        y=cognitive_needs,
        marker_color='lightcoral'
    ))
    
    fig.update_layout(
        title='年代別アクセシビリティニーズ（想定値）',
        xaxis_title='年代',
        yaxis_title='サポートが必要な人の割合（%）',
        barmode='group',
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("""
    **ポイント:** 年齢を重ねるにつれて、何らかのサポートが必要になる可能性は誰にでもあります。
    ユニバーサルデザインは、特定の人のためだけではなく、将来の自分自身のためでもあるのです。
    """)
    
    # インタラクティブな体験
    st.markdown("### 体験してみよう: フォントサイズの違い")
    
    font_size = st.slider("フォントサイズを調整してください", 12, 24, 16)
    
    sample_text = "このテキストの読みやすさはどうですか？"
    
    st.markdown(f"""
    <p style="font-size: {font_size}px; line-height: 1.6; padding: 20px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9;">
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
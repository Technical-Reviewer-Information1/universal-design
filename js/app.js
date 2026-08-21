(function () {
  'use strict';
  const $ = id => document.getElementById(id);

  /* ===== STEP 1 ピクトグラム ===== */
  const P = '#123a6b';
  const PICTOS = [
    { nm: '非常口', svg: '<rect x="6" y="6" width="52" height="58" fill="none" stroke="' + P + '" stroke-width="3"/><circle cx="30" cy="20" r="5" fill="' + P + '"/><path d="M30 26 L22 40 L28 40 L24 58 M30 26 L40 34 L46 30 M28 40 L36 54" stroke="' + P + '" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M64 20 L64 50 L86 50" stroke="' + P + '" stroke-width="3" fill="none"/><path d="M70 35 L86 35 M80 29 L86 35 L80 41" stroke="' + P + '" stroke-width="3" fill="none"/>' },
    { nm: 'お手洗い', svg: '<circle cx="30" cy="14" r="7" fill="' + P + '"/><path d="M22 24 h16 l5 22 h-6 l-1 20 h-12 l-1 -20 h-6 z" fill="' + P + '"/><circle cx="68" cy="14" r="7" fill="' + P + '"/><path d="M60 24 h16 l7 24 h-7 l0 18 h-16 l0 -18 h-7 z" fill="' + P + '"/>' },
    { nm: '車いす使用者用設備', svg: '<circle cx="42" cy="14" r="7" fill="' + P + '"/><circle cx="42" cy="48" r="20" fill="none" stroke="' + P + '" stroke-width="4"/><path d="M38 24 v18 h18 l8 16 h8" stroke="' + P + '" stroke-width="5" fill="none" stroke-linecap="round"/>' },
    { nm: '禁煙', svg: '<circle cx="48" cy="36" r="28" fill="none" stroke="#c0392b" stroke-width="5"/><rect x="26" y="32" width="40" height="9" fill="' + P + '"/><line x1="28" y1="56" x2="68" y2="16" stroke="#c0392b" stroke-width="5"/>' },
    { nm: '飲料水', svg: '<path d="M34 8 h28 l-4 44 a10 10 0 0 1 -20 0 z" fill="none" stroke="' + P + '" stroke-width="3"/><path d="M36 28 h24 l-3 24 a8 8 0 0 1 -18 0 z" fill="' + P + '"/><path d="M20 40 q6 -14 12 0" stroke="' + P + '" stroke-width="3" fill="none"/>' },
    { nm: '無線LAN（Wi-Fi）', svg: '<path d="M18 34 a34 34 0 0 1 60 0" stroke="' + P + '" stroke-width="5" fill="none"/><path d="M28 44 a22 22 0 0 1 40 0" stroke="' + P + '" stroke-width="5" fill="none"/><path d="M38 54 a11 11 0 0 1 20 0" stroke="' + P + '" stroke-width="5" fill="none"/><circle cx="48" cy="62" r="4" fill="' + P + '"/>' }
  ];
  function drawPictos() {
    $('pictoBox').innerHTML = PICTOS.map((p, i) =>
      '<div class="p" data-i="' + i + '"><svg viewBox="0 0 96 70" role="img" aria-label="ピクトグラム">' + p.svg + '</svg>' +
      '<div class="nm">？</div></div>').join('');
    $('pictoBox').querySelectorAll('.p').forEach(el => el.addEventListener('click', () => {
      el.classList.add('open');
      el.querySelector('.nm').textContent = PICTOS[+el.dataset.i].nm;
      const open = $('pictoBox').querySelectorAll('.p.open').length;
      const n = $('pictoNote');
      n.className = 'note ' + (open === PICTOS.length ? 'ok' : 'info');
      n.innerHTML = open === PICTOS.length
        ? '日本語が読めない人でも、これらの意味はほとんど伝わります。これが<strong>「特定の言語に依らず、視覚的に情報を伝えることができる」</strong>ということです。'
        : open + ' / ' + PICTOS.length + ' 個。言葉を見る前に、何を表しているか考えてみましょう。';
    }));
  }
  function drawTermTable() {
    $('termTable').innerHTML = '<thead><tr><th>ことば</th><th>意味</th></tr></thead><tbody>' +
      '<tr style="background:var(--warn-bg)"><td><strong>ピクトグラム</strong></td><td>文字を使わずに情報を伝える案内用図記号。公共施設の案内表示や標識。</td></tr>' +
      '<tr><td>インフォグラフィックス</td><td>情報を図やグラフと組み合わせて、視覚的・効果的に伝えたもの。</td></tr>' +
      '<tr><td>シグニファイア</td><td>一目でどう操作すればよいかを示す手がかり。丸い投入口＝ペットボトル用など。</td></tr>' +
      '<tr><td>アイコン</td><td>ものごとを簡単な絵柄で記号化したもの。画面上の操作を分かりやすく示す。</td></tr></tbody>';
  }

  /* ===== 共通のクイズ描画 ===== */
  function quiz(boxId, noteId, items, tailHTML) {
    let ans = {};
    const box = $(boxId);
    box.innerHTML = items.map((b, i) => {
      const long = b.ch.some(c => c.length > 14);
      return '<div' + (i ? ' style="margin-top:16px;padding-top:14px;border-top:1px solid var(--line)"' : '') + '>' +
        '<p class="pq">【' + b.k + '】　' + b.q + '</p>' +
        '<div class="choice4' + (long ? ' v' : '') + '" data-i="' + i + '">' + b.ch.map((c, j) =>
          '<button class="btn" data-i="' + i + '" data-c="' + c + '" style="text-align:' + (long ? 'left' : 'center') + '">' +
          '⓪①②③④⑤'[j] + '　' + c + '</button>').join('') +
        '</div><div class="note" id="' + boxId + 'fb' + i + '" hidden></div></div>';
    }).join('');
    box.querySelectorAll('button[data-c]').forEach(btn => btn.addEventListener('click', () => {
      const i = +btn.dataset.i, b = items[i], ok = btn.dataset.c === b.a;
      const row = box.querySelector('.choice4[data-i="' + i + '"]');
      row.classList.add('locked');
      [...row.children].forEach(x => { if (x.dataset.c === b.a) x.classList.add('correct'); else if (x === btn) x.classList.add('wrong'); });
      const fb = $(boxId + 'fb' + i);
      fb.hidden = false; fb.className = 'note ' + (ok ? 'ok' : 'ng');
      fb.innerHTML = (ok ? '正解。' : '正解は <strong>' + b.a + '</strong>。') + b.why;
      ans[i] = ok;
      const done = Object.keys(ans).length, right = Object.values(ans).filter(Boolean).length;
      const n = $(noteId);
      n.className = 'note ' + (done === items.length ? (right === done ? 'ok' : 'warn') : 'info');
      n.innerHTML = done + ' / ' + items.length + ' 問（正解 ' + right + ' 問）' + (done === items.length ? '<br>' + tailHTML : '');
    }));
    $(noteId).className = 'note info';
    $(noteId).textContent = '0 / ' + items.length + ' 問';
  }

  /* ===== STEP 2 ===== */
  const UD = [
    { t: '階段しかなかった入口に、あとからスロープを設置した。', a: 'バリアフリー', why: 'すでにある障壁（段差）を取り除く工夫です。' },
    { t: 'はじめから段差のない建物として設計した。', a: 'ユニバーサルデザイン', why: '最初から誰にとっても障壁がないように設計しています。' },
    { t: 'シャンプーの容器の側面にギザギザをつけ、目を閉じていてもリンスと区別できるようにした。', a: 'ユニバーサルデザイン', why: '誰にとっても分かりやすく、はじめから使いやすく設計されています。' },
    { t: '駅のホームに点字ブロックを追加した。', a: 'バリアフリー', why: '目の不自由な人にとっての障壁を取り除く工夫です。' },
    { t: '右利きでも左利きでも使えるはさみを作った。', a: 'ユニバーサルデザイン', why: 'はじめからどちらの人でも使えるように設計されています。' }
  ];
  let udAns = {};
  function drawUD() {
    $('udBox').innerHTML = UD.map((u, i) =>
      '<div class="udrow"><div class="q">' + u.t + '</div>' +
      '<div class="choice4" data-i="' + i + '" style="grid-template-columns:1fr 1fr">' +
      '<button class="btn" data-i="' + i + '" data-c="バリアフリー" style="text-align:center">バリアフリー</button>' +
      '<button class="btn" data-i="' + i + '" data-c="ユニバーサルデザイン" style="text-align:center">ユニバーサルデザイン</button></div>' +
      '<div class="note" id="udfb' + i + '" hidden style="margin-top:8px"></div></div>').join('');
    $('udBox').querySelectorAll('button[data-c]').forEach(b => b.addEventListener('click', () => {
      const i = +b.dataset.i, u = UD[i], ok = b.dataset.c === u.a;
      const row = $('udBox').querySelector('.choice4[data-i="' + i + '"]');
      row.classList.add('locked');
      [...row.children].forEach(x => { if (x.dataset.c === u.a) x.classList.add('correct'); else if (x === b) x.classList.add('wrong'); });
      const fb = $('udfb' + i); fb.hidden = false; fb.className = 'note ' + (ok ? 'ok' : 'ng');
      fb.innerHTML = '<strong>' + u.a + '</strong>　' + u.why;
      udAns[i] = ok;
      const done = Object.keys(udAns).length, right = Object.values(udAns).filter(Boolean).length;
      const n = $('udNote');
      n.className = 'note ' + (done === UD.length ? (right === done ? 'ok' : 'warn') : 'info');
      n.innerHTML = done + ' / ' + UD.length + ' 問（正解 ' + right + ' 問）' +
        (done === UD.length ? '<br>見分け方は「<strong>あとから取り除いた</strong>のか、<strong>はじめから障壁がない</strong>のか」です。' : '');
    }));
    $('udNote').className = 'note info'; $('udNote').textContent = '0 / ' + UD.length + ' 問';
  }

  /* ===== STEP 4 アクセシビリティ実験 ===== */
  function lum(rgb) {
    const f = c => { c /= 255; return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); };
    return 0.2126 * f(rgb[0]) + 0.7152 * f(rgb[1]) + 0.0722 * f(rgb[2]);
  }
  function drawDemo() {
    const fs = +$('fsz').value, ct = +$('ctr').value;
    $('fszV').textContent = fs; $('ctrV').textContent = ct;
    const bg = [255, 255, 255];
    const g = Math.round(255 - (255 - 21) * (ct / 100));
    const fg = [g, g, g];
    const L1 = lum(bg), L2 = lum(fg);
    const ratio = (Math.max(L1, L2) + 0.05) / (Math.min(L1, L2) + 0.05);
    $('ratioV').textContent = ratio.toFixed(1) + ' : 1';
    const alt = $('altOn').checked, mv = $('movieOnly').checked;
    $('demoBox').style.fontSize = (fs / 100) + 'rem';
    $('demoBox').innerHTML = mv
      ? '<div class="img" style="padding:34px">▶ 動画のみ<br><span style="font-size:.8em">（音声・文字による説明はありません）</span></div>'
      : '<p style="color:rgb(' + fg.join(',') + ')"><strong>文化祭のお知らせ</strong></p>' +
        '<p style="color:rgb(' + fg.join(',') + ')">10月18日（土）10時から、本校体育館で文化祭を行います。入場は無料です。</p>' +
        '<div class="img">' + (alt ? '［画像］代替テキスト：「文化祭のポスター。日時と場所が書かれている」' : '［画像］（代替テキストなし）') + '</div>';
    const n = $('a11yNote');
    const problems = [];
    if (ratio < 4.5) problems.push('コントラスト比が <strong>' + ratio.toFixed(1) + ':1</strong> しかなく、目安の4.5:1を下回っています');
    if (!alt) problems.push('画像に<strong>代替テキストがない</strong>ので、画面読み上げソフトでは内容が伝わりません');
    if (mv) problems.push('<strong>動画だけ</strong>では、音が聞こえない人・動画を見られない環境の人に情報が届きません');
    if (fs < 85) problems.push('文字が小さく、読みにくい人がいます');
    n.className = 'note ' + (problems.length ? 'ng' : 'ok');
    n.innerHTML = problems.length
      ? '<strong>気づいた問題：</strong><br>・' + problems.join('<br>・')
      : 'このページはアクセシビリティの基本を満たしています（十分なコントラスト・代替テキスト・読める文字サイズ・動画以外の手段）。';
  }

  /* ===== STEP 5 ===== */
  const UD7 = [
    { n: '第1原則', t: '公平性', d: '誰にでも公平に使える。', ex: '自動ドア、多目的トイレ' },
    { n: '第2原則', t: '柔軟性', d: '使う上で自由度が高い。', ex: '右利きでも左利きでも使えるはさみ' },
    { n: '第3原則', t: '単純性', d: '使い方が簡単ですぐに分かる。', ex: 'ボタンが1つだけの機器' },
    { n: '第4原則', t: '分かりやすさ', d: '必要な情報がすぐに理解できる。', ex: 'ピクトグラム、多言語表示', hi: true },
    { n: '第5原則', t: '安全性', d: 'うっかりミスが危険につながらない。', ex: 'ロックを解除してから給湯するポット' },
    { n: '第6原則', t: '体への負担の少なさ', d: '無理な姿勢や強い力を必要としない。', ex: 'センサー式ドア、レバー式の蛇口' },
    { n: '第7原則', t: 'スペースの確保', d: '近づいて使えるだけの大きさと広さ。', ex: '広い通路、低い位置の券売機' }
  ];
  function drawUD7() {
    $('ud7Box').innerHTML = UD7.map(u =>
      '<div' + (u.hi ? ' class="hi"' : '') + '><span class="n">' + u.n + '</span><strong>' + u.t + '</strong>　' + u.d +
      '<br><span class="small" style="color:var(--muted)">例：' + u.ex + '</span></div>').join('');
  }

  function init() {
    drawPictos(); drawTermTable(); drawUD(); drawUD7();
    quiz('q1Box', 'q1Note', [
      { k: 'ア', q: '情報や注意を示すために使われる案内記号を何というか。',
        ch: ['インフォグラフィックス', 'ピクトグラム', 'シグニファイア', 'アイコン'], a: 'ピクトグラム',
        why: '公共施設の案内表示などで使われる、文字を使わない図記号です。' },
      { k: 'イ', q: '文字の代わりに視覚的な図記号で表現すると、どうなるか。',
        ch: ['特定の言語に依らず、視覚的に情報を伝えることができる', '細かい装飾を多用し、デザイン性を重視している', '情報の蓄積や検索を効率化し、整理しやすい形にする', '視認性を意図的に下げることで、情報を目立ちにくくする'],
        a: '特定の言語に依らず、視覚的に情報を伝えることができる',
        why: 'STEP 1 で体験したとおり、言葉が分からなくても意味が伝わります。視認性が高く、素早く伝えられるのも利点です。' }
    ], '本文の答えは【ア】①　【イ】⓪ です。');
    quiz('q2Box', 'q2Note', [
      { k: 'ウ', q: 'バリアフリーとユニバーサルデザインの説明として適当なものは',
        ch: ['バリアフリーは「デザインにおける視覚的魅力を重視する」、ユニバーサルデザインは「見た目より機能を重視する」', 'バリアフリーは「はじめから障壁がないように設計する」、ユニバーサルデザインは「障がいを取り除く」', 'バリアフリーは「障がいを取り除く」、ユニバーサルデザインは「はじめから障壁がないように設計する」', 'バリアフリーは「物理的な障壁に焦点を当てる」、ユニバーサルデザインは「誰にとっても使いやすいことに焦点を当てる」'],
        a: 'バリアフリーは「障がいを取り除く」、ユニバーサルデザインは「はじめから障壁がないように設計する」',
        why: '①は2つが入れかわっています。③はもっともらしいですが、本文の定義としては②が正解です。' }
    ], '本文の答えは【ウ】② です。');
    quiz('q3Box', 'q3Note', [
      { k: 'エ', q: '利用者が使いやすいか、分かりやすいかを示す尺度は',
        ch: ['ユニバーサルデザイン', 'アクセシビリティ', 'ユーザビリティ', 'ユーザエクスペリエンス（UX）'], a: 'ユーザビリティ',
        why: '「使いやすさ」の尺度がユーザビリティです。' },
      { k: 'オ', q: '幅広い人々が情報やサービスへアクセスしやすいかを示す尺度は',
        ch: ['ユニバーサルデザイン', 'アクセシビリティ', 'ユーザビリティ', 'ユーザエクスペリエンス（UX）'], a: 'アクセシビリティ',
        why: '「近づきやすさ・利用しやすさ」の尺度がアクセシビリティです。' },
      { k: 'カ', q: 'ユーザビリティと関係の深いものは',
        ch: ['足の不自由な方や高齢者のために、手すりやスロープを設置する', '路線図を作成する際に、見分けにくい路線に明度差を利用した網掛けを使う', '視覚に障がいをもっている人に対して、音声読み上げ機能を提供する', 'スマートフォンにおいて、片手でも文字の入力をしやすいようにフリック入力を提供する'],
        a: 'スマートフォンにおいて、片手でも文字の入力をしやすいようにフリック入力を提供する',
        why: '⓪はバリアフリー、①はカラーユニバーサルデザイン、②はアクセシビリティの例です。③は「使いやすさ」を高めるユーザインタフェースの工夫なので、ユーザビリティと関係が深いといえます。' }
    ], '本文の答えは【エ】②　【オ】①　【カ】③ です。');
    quiz('q4Box', 'q4Note', [
      { k: 'キ', q: 'Webページにおけるアクセシビリティ対応として適当でないものは',
        ch: ['画像の内容を言葉で説明した代替テキストを設定する', 'Webページの文字サイズをユーザが調整できる機能を追加する', 'すべての情報を動画のみで提供し、音声や文字による説明を用意しない', '色のコントラストに配慮し、背景と文字が見やすいように工夫する'],
        a: 'すべての情報を動画のみで提供し、音声や文字による説明を用意しない',
        why: '動画だけでは、目や耳が不自由な人・通信量を節約したい人などに情報が届きません。ほかの3つはいずれも正しい対応です。' }
    ], '本文の答えは【キ】② です。');
    quiz('q5Box', 'q5Note', [
      { k: 'ク', q: '「必要な情報が簡単に理解できる」という原則に適する例は',
        ch: ['ロックを解除してから給湯するポット', '交通施設や商業施設などで使われているピクトグラム', '右利きでも左利きでも使えるはさみ', '人の動きを感知して自動的に開閉するセンサー式ドア'],
        a: '交通施設や商業施設などで使われているピクトグラム',
        why: '⓪は誤操作を防ぐ第5原則（安全性）、②は第2原則（柔軟性）、③は体への負担を減らす工夫です。ピクトグラムは情報が一目で理解できるので、この原則の例になります。' }
    ], '本文の答えは【ク】① です。');
    ['fsz', 'ctr'].forEach(i => $(i).addEventListener('input', drawDemo));
    ['altOn', 'movieOnly'].forEach(i => $(i).addEventListener('change', drawDemo));
    drawDemo();
    $('uaTable').innerHTML = '<thead><tr><th>ことば</th><th>意味</th><th>例</th></tr></thead><tbody>' +
      '<tr><td><strong>ユーザビリティ</strong></td><td>利用者が使いやすいか、分かりやすいかを示す尺度</td><td>片手で入力しやすいフリック入力</td></tr>' +
      '<tr><td><strong>アクセシビリティ</strong></td><td>幅広い人々が情報やサービスへアクセスしやすいかを示す尺度</td><td>音声読み上げ機能、代替テキスト</td></tr>' +
      '<tr><td>ユニバーサルデザイン</td><td>誰もが使えるようにはじめから設計する考え方</td><td>段差のない建物、多目的トイレ</td></tr>' +
      '<tr><td>ユーザエクスペリエンス（UX）</td><td>使ったときに得られる体験や満足感全体</td><td>買い物のしやすさ、使った後の印象</td></tr></tbody>';
    window.Terms.glossary($('glossBox'), ['ピクトグラム', 'ユニバーサルデザイン', 'バリアフリー', 'ユーザビリティ', 'アクセシビリティ', 'ユーザインタフェース', '情報格差', 'インフォグラフィックス']);
    Worksheet.make('wsBox', {
      name: 'universal-design',
      fields: [
        { id: 'u1', label: '① 取り上げるもの', hint: '案内表示、券売機、ドア、階段、Webサイトなど。', rows: 2, ph: '例：昇降口の掲示板' },
        { id: 'u2', label: '② いま、だれにとって使いやすいか', hint: '想定されている利用者。', rows: 2, ph: '例：立って読める、日本語が読める、視力のよい生徒' },
        { id: 'u3', label: '③ だれが、どう困るか', hint: '車いす・低身長・色覚特性・外国につながる人・けが人・急いでいる人など。', rows: 3,
          ph: '例：車いすの生徒には上段が見えない／赤と緑で色分けされていて見分けにくい人がいる' },
        { id: 'u4', label: '④ 改善案', hint: '「だれか」を助けるだけでなく、みんなが使いやすくなる案に。', rows: 3,
          ph: '例：重要な掲示は目の高さの帯に集める／色だけでなく記号と文字も添える' },
        { id: 'u5', label: '⑤ その案の効果を、どう確かめるか', hint: '確かめ方まで書けると探究になる。', rows: 2,
          ph: '例：改善前後で「掲示に気づいた人」の割合をアンケートで比べる' }
      ],
      build: function (v, e) {
        return '<h4>ユニバーサルデザイン改善シート</h4><dl>' +
          '<dt>① 取り上げるもの</dt><dd>' + e(v.u1) + '</dd>' +
          '<dt>② いま使いやすい人</dt><dd>' + e(v.u2) + '</dd>' +
          '<dt>③ 困る人と、その理由</dt><dd>' + e(v.u3) + '</dd>' +
          '<dt>④ 改善案</dt><dd>' + e(v.u4) + '</dd>' +
          '<dt>⑤ 効果の確かめ方</dt><dd>' + e(v.u5) + '</dd></dl>';
      },
      note: '「特定のだれかのための工夫」が「みんなに便利」になっている例を探すと、UDの考え方がつかめます。'
    });

    window.Terms.attach();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();

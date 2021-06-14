# Common README

## About

* CommonはPythonとPygame Zeroの基本を学ぶための教材です

## Steps

### Step 01: Python と Pygame Zeroの始まり

* Windowを出してみよう
  * `WIDTH`と`HEIGHT`を変えてみよう
* 関数(`def draw():`)とは?
  * `draw`関数はPygame Zeroの関数で、1秒間に60回呼ばれます
　* `def draw():`の次の行には半角スペースが4つあります
    * これはインデントと呼ばれます
    * インデントはプログラムの階層のように扱われます
    * `def`の次の行は常に1つ下の階層になります
    * 後で出てくる`for`や`while`や`if`も1つ下の階層をとります
* Windowの中を赤にしてみよう
  * タプルとは？`screen.fill((255, 0, 0))`のようになぜ括弧が２つあるのか？
* `print`を使ってみよう
  * `print(1)`とするとコンソールに`1`と表示されます
  * `print(255, 0, 0)`と`print((255, 0, 0))`は何が違うのだろう？

#### 課題

  * Windowの中身を青で塗ってみよう
  * コンソールに`hello`と表示してみよう
  * `draw`関数の中に`print`で文字を表示するとどうなるだろう？

### Step 02: キャラクターを表示してみよう

  * Actorを1つ表示してみよう

#### 課題

  * Actorを回転させてみよう
    * ヒント: `a.angle`
  * Actorの位置を変えてみよう
    * ヒント: `a.pos`や`a.x`, `a.y`
  * 複数のActorを表示してみよう
  * 背景を白にしてみよう

### Step 03: Pythonについて

* 変数と型
  * int
  * float
  * str
  * printと%の使い方
* `if`構文とは？
* `for`構文とは？
* `list`（リスト）とはなんだろう？
  * listを使って複数の文字列を格納してみよう
  * `for`を使ってlistの中身を全て表示してみよう
  * index（インデックス）を使ってlistの中身を表示してみよう
  * index（インデックス）を使ってlistの中身を変更してみよう
  * 2次元listを使ってみよう
* `dictionary`（辞書とはなんだろう）？
  * `dictionary`を使って複数の文字列を格納してみよう
  * `for`を使ってdictionaryの中身を全て表示してみよう
  * key（キー）を使ってlistの中身を表示してみよう
  * key（キー）を使ってlistの中身を変更してみよう

#### 課題

* `a=3`の時に`print`と`%`をうまく使って左から0埋めで`0003`と表示してみよう
* `array`を作って、`for`を使ってそのarrayに1から100までの整数を格納してみよう
* 1から100まで格納したarrayを列挙（巡回）して、全ての数字を表示してみよう
* `dictionary`にいくつかのkey - valueペアを代入しよう
* その`dictionary`を列挙（巡回）して、全てのkey - valueペアを`print`してみよう


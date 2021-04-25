# README

* このrepoはPygame Zeroを使ってPythonを学びながらゲームプログラミングを楽しむためのものです
* 現在以下のコンテンツがあります
  * TBD: [虫取りシューティングゲーム](./bug_shooting/)
    * 画面情報から襲ってくる虫を倒して畑を守るシューティングゲーム
    * Pythonの基本が学べます
  * [パイプゲーム](./pipe/)
    * スタート地点からゴール地点までパイプをつなぐパズルゲーム
    * Pythonの基本と再帰・経路探索が学べます
  * TBD: [食料配達ゲーム](./food_delivery/)
    * 画面上の全ての家に食料を配達するドットイーター型アクションゲーム

## 共通セットアップ手順

* Python 3の最新版をインストール(2021/4/25現在3.9.4)
  * <https://www.python.org/downloads/>からダウンロードしインストール
* PyCharmのCimmunity版インストール
  * <https://www.jetbrains.com/ja-jp/pycharm/download/>からダウンロードしインストール

## Apple Silicon搭載Macの注意事項

* Pygame Zeroで使用するPygameは現状ではApple Silicon搭載のMacではNativeでは動きません
* 以下の手順でIntel版のPython3をインストールしてください
  * <https://www.python.org/downloads/mac-osx/>より"macOS 64-bit Intel installer"を選択・ダウンロードし、インストール
* PyCharmはNativeで動きます

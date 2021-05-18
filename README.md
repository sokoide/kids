# README

* このrepoはPygame Zeroを使ってPythonを学びながらゲームプログラミングを楽しむためのものです
* 現在以下のコンテンツがあります
  * TBD: [シューティングゲーム](./shooting/)
    * ギャラクシアンのような画面上方から襲ってくるシューティングゲーム
    * Python/Pygame Zeroの基本とsin/cos波によるエイリアンの動かし方が学べます
  * TBD: [ゲーム](./doteat/)
    * パックマンのようなドットイーター型アクションゲーム
  * [パイプゲーム](./pipe/)
    * スタート地点からゴール地点までパイプをつなぐパズルゲーム
    * Python/Pygame Zeroの基本と再帰・経路探索が学べます

## 共通セットアップ手順

* Python 3の最新版をインストール(2021/4/25現在3.9.4)
  * <https://www.python.org/downloads/>からダウンロードしインストール
* PyCharmのCommunity版インストール
  * <https://www.jetbrains.com/ja-jp/pycharm/download/>からダウンロードしインストール

## Apple Silicon搭載Macの注意事項

* Pygame Zeroで使用するPygameは現状ではApple Silicon搭載のMacではNativeでは動きません
* 以下の手順でIntel版のPython3をインストールしてください
  * <https://www.python.org/downloads/mac-osx/>より"macOS 64-bit Intel installer"を選択・ダウンロードし、インストール
* PyCharmはNativeで動きます

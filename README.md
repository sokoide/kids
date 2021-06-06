# README

* このrepoはPygame Zeroを使ってPythonを学びながらゲームプログラミングを楽しむためのものです
* 現在以下のコンテンツがあります
  * [ここからはじめよう](./common/)
    * 全てのゲームに共通のPythonのとPygame Zeroの基本が学べます
  * [シューティングゲーム](./shooting/)
    * ギャラクシアンのような画面上方のエイリアンを撃って倒すシューティングゲーム
    * Pygameの基本的な開発の流れが学べます
    * 通常ミサイル、3-wayミサイル、レーザーなどの作り方が学べます
  * [パイプゲーム](./pipe/)
    * スタート地点からゴール地点までパイプをつなぐパズルゲーム
    * Python/Pygame Zeroの基本と再帰・経路探索が学べます
  * TBD: [ドットイーティングゲーム](./doteat/)
    * パックマンのようなドットイーター型アクションゲーム
  * TBD: [ジャンプスクロールゲーム](./flappy/)
    * フラッピーバードのようなジャンプしながらスクロールしていくゲーム

## 共通セットアップ手順

* Python 3の最新版をインストール(2021/6/5現在3.9.5)
  * <https://www.python.org/downloads/>からダウンロードしインストール
* PyCharmのCommunity版インストール
  * <https://www.jetbrains.com/ja-jp/pycharm/download/>からダウンロードしインストール

## Apple Silicon搭載Macの注意事項

* Pygame Zeroで使用するPygameは現状ではApple Silicon搭載のMacではNativeでは動きません
* 以下の手順でIntel版のPython3をインストールしてください
  * <https://www.python.org/downloads/mac-osx/>より"macOS 64-bit Intel installer"を選択・ダウンロードし、インストール
* PyCharmはNativeで動きます

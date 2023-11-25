# Local_Chat_Messenger
## 注意点
- Macのターミナルで操作をしているのでLinuxのパスと異なります。
## 課題
- Pythonのソケット通信とfakerパッケージを使用して、クライアントサーバ間で情報をやりとりするシンプルなアプリケーションを作成
  - クライアントの作成
    - ユーザーから入力を受け取り、その入力をサーバに送信するクライアントを作成します。
    - ユーザーの入力は、例えばコマンドラインから受け取るものとします。
    - クライアントは、ユーザーからの入力を待ち、入力があったらそれをサーバに送信します。
  - サーバーの作成
    - クライアントからのメッセージを受け取り、それに対する応答を送り返すサーバを作成します。
    - サーバは、受け取ったメッセージに基づいて何らかの応答を生成し、それをクライアントに送り返します。
  - fakerパッケージの利用
    - fakerは、様々な種類の偽データを生成することができます
    - この課題では、サーバ側で faker を使って偽のランダムな文字列やメッセージを生成します。
    - サーバからの応答を模擬するためのもので、実際の応答がない場合やテストの際に役立ちます。

## 課題前の準備
- TCPとUDP通信のやり方、fork、fakerパッケージの動きなどを作成して確認する。
- testブランチを作成し上記の作業を行う。
- test作業を終えてからmainブランチに戻り課題のブランチを作成する。

## 学習の目的
- パイプやソケットなどのプロセス間通信がどのように機能するかを学ぶ
- プロセスがローカル上で互いに通信できるようになるかを学ぶ
- オペレーティングシステムのソケットAPIを使用してアプリケーションがどのようにデータを送信するかを学ぶ

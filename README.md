# LocalChatMessenger

## Overview
ローカルでソケット通信を行うスクリプトです。サーバは、クライアントから送信されたメッセージを受け取り、Fakerによって作成されたランダムなテキストをクライアントへ送り返します。コンピュータサイエンス学習サービス[Recursion](https://recursionist.io/)のアウトプットプロジェクト（Local Chat Messenger）として取り組みました。
<br />

## Pre Installation
* スクリプトを実行するには、[Faker](https://pypi.org/project/Faker/0.7.4/)のインストールが必要です。
	```zsh
	pip install Faker
	```
<br />

## Learning Matter
* ソケット通信
	* server
		* socket() → bind() → listen() → accept() → receive()/send() → close()
	* clinet
		* socket() → connect() → receive()/send() → close()
	* AF_UNIX
	* SOCK_STREAM
* 例外処理
	* try, except, finally
<br />

## Reference
* [今更ながらソケット通信に入門する（Pythonによる実装例付き）](https://qiita.com/t_katsumura/items/a83431671a41d9b6358f)
* [Pythonの例外処理（try, except, else, finally）](https://note.nkmk.me/python-try-except-else-finally/)
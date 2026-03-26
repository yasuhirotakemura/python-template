1. インストール・準備
まずは、どのバージョンが利用可能かを確認し、インストールします。 
インストール可能なリストを表示
bash
pyenv install --list
Use code with caution.

特定のバージョンをインストール
bash
pyenv install 3.14.3
Use code with caution.

インストール済みのバージョンを一覧表示
bash
pyenv versions
Use code with caution.

※ 現在適用されているバージョンには * が付きます。 
2. バージョンの切り替え（重要）
pyenv には「場所」に応じた3種類の切り替え方法があります。
特定のディレクトリ内だけで使う（推奨）
bash
pyenv local 3.14.3
Use code with caution.

※ そのディレクトリに .python-version ファイルが作成され、そこに入ると自動で切り替わります。
PC全体（ユーザー環境全体）で使う
bash
pyenv global 3.14.3
Use code with caution.

今のシェル（ターミナル）画面だけで使う
bash
pyenv shell 3.14.3
Use code with caution.

3. 確認・メンテナンス
現在使っているバージョンを確認
bash
pyenv version
Use code with caution.

不要になったバージョンを削除
bash
pyenv uninstall 3.10.4
Use code with caution.

pyenv自体のアップデート (公式の pyenv-update プラグインがある場合)
bash
pyenv update
Use code with caution.

 

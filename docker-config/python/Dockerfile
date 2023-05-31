# ベースイメージの指定
FROM python:3.9

# ソースコードを配置する作業ディレクトリを作成
WORKDIR /src

# ソースコードをDockerイメージにコピー
COPY . /src

# 必要なパッケージのインストール
RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
RUN pip install bash moviepy

# コンテナ内でのデフォルトのコマンド
CMD ["python"]


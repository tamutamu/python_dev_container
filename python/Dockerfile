FROM python:3.8-slim-buster

# パッケージのインストール
RUN apt-get update && apt-get install -y \
    tzdata \
		procps \
		sudo \
		libopencv-dev \
		vim \
 && rm -rf /var/lib/apt/lists/*

# 環境変数の定義
ENV TZ=Asia/Tokyo
ENV USER dev
ENV HOMEDIR /home/${USER}

# Pythonがpyc filesとdiscへ書き込むことを防ぐ
ENV PYTHONDONTWRITEBYTECODE 1

# Pythonが標準入出力をバッファリングすることを防ぐ
ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT true

# 一般権限のユーザーを追加
RUN useradd -m ${USER} --uid 1000
RUN gpasswd -a ${USER} sudo
RUN echo "${USER}:password" | chpasswd

# sudo with no password
RUN echo "Defaults:${USER} !env_reset" > /etc/sudoers && \
		echo "${USER}    ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Pipenvをインストール
RUN pip install --upgrade pip \
 && pip install pipenv

COPY scripts/ /opt/bin/
RUN chmod +x /opt/bin/ -R

RUN cat /opt/bin/.bashrc  >> ${HOMEDIR}/.bashrc

# ユーザーの切替
USER ${USER}

RUN mkdir ${HOMEDIR}/app
RUN mkdir ${HOMEDIR}/.vscode-server

WORKDIR ${HOMEDIR}/app


ENTRYPOINT ["/opt/bin/entrypoint.sh"]
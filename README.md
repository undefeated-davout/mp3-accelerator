# mp3-accelerator

## 使い方

## 起動

※ffmpegがインストールされているマシンであれば以下のdocker compose upは不要

```bash
docker compose up -d

# コンテナにログイン
docker exec -it mp3-accelerator.app bash
```

### 準備

- data/inputにmp3を配置する

以下を実行する

```bash
# 例：2.0倍速に変換する時
python app/mp3-accelerator.py 2.0
```

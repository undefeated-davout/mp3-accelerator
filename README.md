# mp3-converter

## 起動

※ffmpeg、ffmpeg-normalizeがインストールされているマシンであれば以下のdocker compose upは不要

```bash
docker compose up -d

# コンテナにログイン
docker exec -it mp3-converter.app bash
```

## 準備

- data/inputにmp3を配置する

## 実行

```bash
# 例：2.0倍速に変換するとき
python app/mp3-accelerator.py 2.0

# 例：正規化するとき
python app/mp3-normalizer.py
```

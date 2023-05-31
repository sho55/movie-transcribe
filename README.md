# movie-transcribe
Make audioFile from VideoFile with Python

## How to Start

1.build containers.
```bash
docker compose up -d
```

2.after build docker containers.
```bash
docker exec -it [CONTAINERID]　bash
```

3.Edit VideoPath and made audioName in ___movie_to_audio.py___

```bash
video_path = "/path/to/movieData"
audio_file = "./path/to/audioDataName"
```

4. Use Python Script.
```bash
$ python movie_to_audio.py
```

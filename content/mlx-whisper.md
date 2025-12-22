---
title: "mlx-whisper"
date: 2025-12-21 21:30
author: "C. Ross Jam"
status: published
---

Link parkin’: [mlx-whisper][1]

> Speech recognition with Whisper in MLX. Whisper is a set of open
> source speech recognition models from OpenAI, ranging from 39
> million to 1.5 billion parameters. 

I had been experimenting with transcription and diarization using
[WhisperX][4]. This turned out to be pretty slow on an M2 MacBook. mlx-whisper
is pretty honking fast, although it only does transcription. I think
diarization can be addressed by complementary application of
[pyannote.audio][2].

> pyannote.audio is an open-source toolkit written in Python for
> speaker diarization. Based on PyTorch machine learning framework, it
> comes with state-of-the-art pretrained models and pipelines, that
> can be further finetuned to your own data for even better
> performance. 

Thought I’d mentioned mlx-whisper ahead of [parakeet-mlx][3]. In any
event, I’ve actually put it to the test a little bit for
retrocast. The processing rate is quite acceptable for high-quality
transcription. However, this needs some serious benchmarking to
confirm. [moonshine][5] is also in the mix.


[1]: https://github.com/ml-explore/mlx-examples/tree/main/whisper
[2]: https://github.com/pyannote/pyannote-audio
[3]: {filename}/parakeet-mlx.md
[4]: https://github.com/m-bain/whisperX
[5]: https://github.com/moonshine-ai/moonshine



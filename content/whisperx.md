---
title: "whisperX"
date: 2025-12-11 19:44
author: "C. Ross Jam"
status: published
---

Link parkin’: [whisperX][1]

> This repository provides fast automatic speech recognition (70x
> realtime with large-v2) with word-level timestamps and speaker
> diarization. 
> 
> - ⚡️ Batched inference for 70x realtime transcription using whisper large-v2
> - 🪶 faster-whisper backend, requires <8GB gpu memory for large-v2 with beam_size=5
> - 🎯 Accurate word-level timestamps using wav2vec2 alignment
> - 👯‍♂️ Multispeaker ASR using speaker diarization from pyannote-audio (speaker ID labels)
> - 🗣️ VAD preprocessing, reduces hallucination & batching with no WER degradation
>
> Whisper is an ASR model developed by OpenAI, trained on a large
> dataset of diverse audio. Whilst it does produces highly accurate
> transcriptions, the corresponding timestamps are at the
> utterance-level, not per word, and can be inaccurate by several
> seconds. OpenAI's whisper does not natively support batching. 
> 

[retrocast][2] is my personal RAG "auditionware" project for
investigating with podcast episodes. It’s meant to combine:

- agentic coding
- AI-powered search
- AI-powered UX

So far, the agentic coding has accelerated my ability to implement
features. Recently, [episode archiving][3] was completed. Next up:
generating transcripts for full-text and embedding search.

Looks like whisperX fits the bill for a first crack at ASR for retrocast.

[1]: https://github.com/m-bain/whisperX
[2]: https://github.com/crossjam/retrocast
[3]: https://github.com/crossjam/retrocast/pull/38



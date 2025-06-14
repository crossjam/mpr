Title: The MLX and mlx-lm Projects
Date: 2025-06-08
Author: C. Ross Jam
Status: published

Have to take a moment to recommend the [MLX][1] project.

> MLX is a NumPy-like array framework designed for efficient and
> flexible machine learning on Apple silicon, brought to you by Apple
> machine learning research. 

> The Python API closely follows NumPy with a few exceptions. MLX also
> has a fully featured C++ API which closely follows the Python API. 

But ultimately it’s the application of MLX in the [`mlx-lm`][2] CLI
tool that’s really impressive. I’ve been able to use `mlx-lm` to run
LLM model weights from Hugging Face in easy one liners. There’s a
great Hugging Face [MLX Community][3] that works exceptionally hard to
convert the latest open weight models into the MLX format. `mlx-lm`
also supports using GGUF files directly which blows open the space of
available models. Based on [an HF overview article][4] here’s an
example:


``` console
$ uv tool install mlx-lm
$ uv tool install 'huggingface_hub[cli]'
#
# You'll need to
# 1) Accept terms and conditions for the Mistral model for your account on the HF site
# 2) Create an HF token in your account to login with from the cli
#
$ huggingface-cli login
...
$ mlx_lm.chat --model mistralai/Mistral-7B-Instruct-v0.2
... lots of downloading of model weights ...
[INFO] Starting chat session with mistralai/Mistral-7B-Instruct-v0.2.
The command list:
- 'q' to exit
- 'r' to reset the chat
- 'h' to display these commands
>> hello
Hello! How can I help you today? If you have any questions or need
assistance with something, feel free to ask. I'm here to help. If you
just want to chat or share some thoughts, that's fine too. Let me know
what's on your mind. :) 
>> Who is your maker
I don't have a maker in the traditional sense, as I am an artificial
intelligence and don't have a physical body or a creator. I was
designed and developed by a team of engineers and computer
scientists. If you have any other questions or need help with
something, just let me know! :) 
>>
>> /bye
Goodbye! It was nice chatting with you. If you have any other
questions or need assistance in the future, don't hesitate to
ask. Have a great day! :) 
>> q
$ 
```

I have a 3 year old 24 Gb M2 MacBook Pro so I don’t get the best
tokens per second output. Still impressive how easy it is to run a
decent sized LLM with little to no development needed. There’s even a
[handy plugin][5] for Simon Willison’s [llm][6] tool. 

Messing around with LLMs is almost cookie cutter at this point.

[1]: https://ml-explore.github.io/mlx/build/html/index.html
[2]: https://github.com/ml-explore/mlx-lm
[3]: https://huggingface.co/mlx-community
[4]: https://huggingface.co/docs/hub/en/mlx
[5]: https://github.com/simonw/llm-mlx
[6]: https://llm.datasette.io/

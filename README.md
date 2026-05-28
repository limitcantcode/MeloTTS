# MeloTTS (inference)

Inference-only library for multi-lingual text-to-speech: English, Spanish, French, Chinese (with mixed EN), Japanese, and Korean.

Requires **Python 3.12+**.

## Install

```bash
pip install -e .
```

For Japanese, download the MeCab dictionary once:

```bash
python -m unidic download
```

## API

```python
from melo import TTS

model = TTS(language="EN", device="auto")
speaker_ids = model.hps.data.spk2id

model.tts_to_file(
    "Did you ever hear a folk tale about a giant turtle?",
    speaker_ids["EN-US"],
    "output.wav",
    speed=1.0,
)
```

`tts_to_file` returns the audio as a NumPy array when `output_path` is omitted.

Supported `language` values: `EN`, `ES`, `FR`, `ZH`, `JP`, `KR`.

Local checkpoint (place `config.json` next to the checkpoint):

```python
model = TTS(
    language="EN",
    config_path="/path/to/config.json",
    ckpt_path="/path/to/checkpoint.pth",
)
```

## License

MIT. See [LICENSE](LICENSE).

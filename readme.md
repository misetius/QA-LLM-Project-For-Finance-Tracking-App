This project provides a framework to **experiment with different multimodal large language models (LLMs)** to evaluate their ability to read and extract information from images of receipts. The goal is to identify the most suitable model for a separate [finance tracking project](https://github.com/misetius/finance-tracking-app).

It focuses on testing **accuracy, hallucinations, latency, and edge-case handling**.

## Models tested in this project

LLM models tested in this project were Qwen 3 VL, Ministral 3 and Gemma 4. Models were run with Ollama.

## How to run tests

Tests will take quite long to run. Atleast on my computer running the full test suite for one model took half an hour.


Before testing you need to have ollama running preferably on docker at address localhost:11434 from the ollama docs in here https://docs.ollama.com/docker is guide for how to setup ollama with model.

After setup you can run the tests when in root of the project with this command:

```
pytest --model "$MODEL" 
```


## Results from current tests

### Latency
 
| Model | Cold Latency  | Warm Latency  |
|---|---|---|
| gemma4 | 82.10 s | 73.22 s |
| ministral-3 | 204.13 s | 60.16 s |
| qwen3-vl | 312.26 s | 781.55 s |
 
### Classification Metrics
 
| Malli | TP | FP | FN | TN | Recall | Precision | Accuracy | F1 Score |
|---|---|---|---|---|---|---|---|---|
| gemma4 | 3 | 1 | 5 | 2 | 0.38 | 0.75 | 0.45 | 0.50 |
| ministral-3 | 4 | 2 | 4 | 1 | 0.50 | 0.67 | 0.45 | 0.57 |
| qwen3-vl | 3 | 2 | 5 | 1 | 0.38 | 0.60 | 0.36 | 0.46 |
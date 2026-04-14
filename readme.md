This project provides a framework to **experiment with different multimodal large language models (LLMs)** to evaluate their ability to read and extract information from images of receipts. The goal is to identify the most suitable model for a separate [finance tracking project](https://github.com/misetius/finance-tracking-app).

It focuses on testing **accuracy, hallucinations, latency, and edge-case handling**.

## Models tested in this project

LLM models tested in this project were Qwen 2.5 VL, Ministral 3 and Gemma 4. Models were run with Ollama.

## How to run tests

Tests will take quite long to run. Atleast on my computer running the full test suite for one model took half an hour.

After copying the project tests can be run with the help of the script provided in this way:

```
./run_and_test_model.sh <model_you_want_to_test>
```

The setup for llm takes quite long so if model is already running you can also just use pytest like this while in root of the project:

```
pytest tests/ --model <MODEL> 
```



## Results from current tests

Still in development
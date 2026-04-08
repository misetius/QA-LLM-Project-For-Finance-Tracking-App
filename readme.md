This project provides a framework to **experiment with different multimodal large language models (LLMs)** to evaluate their ability to read and extract information from images of receipts. The goal is to identify the most suitable model for a separate [finance tracking project](https://github.com/misetius/finance-tracking-app).

It focuses on testing **accuracy, hallucinations, latency, and edge-case handling**.

## Models tested in this project

LLM models tested in this project were Qwen 2.5 VL, Pixtral and Gemma 3. 

## How to run tests

After copying the project tests can be run with the help of the script provided in this way:

```
./run_and_test_model.sh <model_you_want_to_test>
```

The setup for llm takes quite long so if already have model running you can also just use pytest like this while in root of the project:

```
pytest tests/
```
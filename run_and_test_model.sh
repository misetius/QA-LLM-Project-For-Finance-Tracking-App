#!/usr/bin/env bash
set -e


if [ -z "$1" ]; then
  echo "Usage: $0 <model_name>"
  exit 1
fi

MODEL=$1

docker pull ollama/ollama:latest

docker rm -f ollama > /dev/null 2>&1 || true

docker run -d --name ollama -p 11434:11434 ollama/ollama:latest

echo "Waiting for Ollama to start..."
until curl -s http://localhost:11434/api/tags > /dev/null 2>&1; do
  sleep 1
done
echo "Ollama is ready."


echo "Pulling model: $MODEL..."
docker exec ollama ollama pull "$MODEL"


python -m pytest tests/accurary-tests/test_llm_model.py --model "$MODEL" 
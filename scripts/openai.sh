#!/bin/bash

source .env
OPENAI_API_KEY="${OPENAI_API_KEY}"

# -> ... allexport alternative
# set -a  # Enable automatic export of variables
# source .env 
# set +a  # Disable automatic export

if [[ -z "$OPENAI_API_KEY" ]]; then
    echo "Error: OPENAI_API_KEY environment variable is not set. Please configure it."
    exit 1
fi

prompt="What year is it?"

curl -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d '{
            "model": "gpt-4",
            "messages": [
                {"role": "system", "content": "Provide a factual answer. Do not engage in conversation."},
                {"role": "user", "content": "'"$prompt"'" }
            ]
        }' \
    'https://api.openai.com/v1/chat/completions'  | \
    jq -r '.choices[0].message.content'  # Extract response using jq


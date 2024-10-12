#!/bin/bash

set -ex

export OPENAI_BASE_URL=
export OPENAI_API_KEY=

nohup python ./gradio_app.py &

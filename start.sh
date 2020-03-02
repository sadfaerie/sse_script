#!/bin/bash
nohup python src/sse_script/sse_collect.py >/dev/null 2>&1 &
python src/sse_script/sse_query.py
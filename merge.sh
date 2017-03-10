#!/bin/bash
ffmpeg -f concat -i files.txt -c copy all.ts

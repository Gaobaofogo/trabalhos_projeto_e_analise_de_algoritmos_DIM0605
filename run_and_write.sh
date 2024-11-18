#!/bin/sh

echo "Choose the file: "
read filename

echo "j30/j30$filename.sm   $(python main.py --file ./data/data/j30/j30$filename.sm)" >>"./data/alg_result.txt"
echo "j60/j60$filename.sm   $(python main.py --file ./data/data/j60/j60$filename.sm)" >>"./data/alg_result.txt"
echo "j90/j90$filename.sm   $(python main.py --file ./data/data/j90/j90$filename.sm)" >>"./data/alg_result.txt"
echo "j120/j120$filename.sm   $(python main.py --file ./data/data/j120/j120$filename.sm)" >>"./data/alg_result.txt"
echo "" >>"./data/alg_result.txt"

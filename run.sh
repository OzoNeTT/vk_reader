#! /bin/sh

docker build . --tag reader_vk
docker kill reader_vk_cont
docker rm reader_vk_cont
docker run -itd --name reader_vk_cont reader_vk python ./reader/reader.py

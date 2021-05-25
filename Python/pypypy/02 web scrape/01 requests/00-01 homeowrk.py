import requests

url = "https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md"

response01 = requests.get(url)

homework_response = response01.text

homework_saving = open("homework_01.txt", "w")
homework_saving.write(homework_response)
homework_saving.close()

response02 = requests.get("https://res.pandateacher.com/2019-01-12-15-29-33.png")
homework_pic_response = response02.content
homework_pic_saving = open("homework_pic.png", "wb")
homework_pic_saving.write(homework_pic_response)
homework_pic_saving.close()

response03 = requests.get("https://static.pandateacher.com/Over%20The%20Rainbow.mp3")
homework_mp3_response = response03.content
homework_mp3_saving = open("homework_mp3.mp3", "wb")
homework_mp3_saving.write(homework_mp3_response)
homework_mp3_saving.close()
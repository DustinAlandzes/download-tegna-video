#3 - 27
#http://kens-vh.akamaihd.net/i/video/2529388/2529388_,350,640,1000,2000,.mp4.csmil/segment14_3_av.ts
import requests

folder = "parts"
files = []

# download segments 3 - 27
for num in range(3, 27):
  filename = "{}/segment{}_3_av.ts".format(folder, num)
  with open(filename, 'wb') as handle:
    url = "http://kens-vh.akamaihd.net/i/video/2529388/2529388_,350,640,1000,2000,.mp4.csmil/segment{}_3_av.ts".format(num)
    response = requests.get(url, stream=True)

    print("downloaded {}".format(filename))

    for block in response.iter_content(1024):
        handle.write(block)

    files.append(filename)


# put file names in files.txt
filename = "files.txt"
with open(filename, 'w+') as handle:
    for file in files:
        handle.write("file '{}'\r\n".format(file))

print("created files.txt")

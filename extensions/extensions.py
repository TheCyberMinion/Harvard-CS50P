file_type = {

    "gif" : "image/gif",
    "jpg" : "image/jpeg",
   "jpeg" : "image/jpeg",
    "png" : "image/png",
    "pdf" : "application/pdf",
    "zip" : "application/zip",
    "txt" : "text/plain"
}

filename = str(input("What is the file name: ")).strip().lower()
x = filename.split(".")[-1]

if x in file_type:
    print(file_type[x])
else:
    print("application/octet-stream")

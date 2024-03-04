# Prompt the user for the name of a file
extension = input("Filename: ")

# Outputs that file’s media type if the file’s name ends, case-insensitively, in any of some suffixes
if extension.endswith(".gif"):
    print("image/gif")
elif extension.endswith(".jpg" or "jpeg"):
    print("image/jpeg")
elif extension.endswith(".png"):
    print("image/png")
elif extension.endswith(".pdf"):
    print("application/pdf")
elif extension.endswith(".txt"):
    print("text/plain")
elif extension.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
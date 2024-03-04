# Prompt the user for the name of a file
extension = input("Filename: ")

# Outputs that file’s media type if the file’s name ends, case-insensitively, in any of some suffixes
match extension.endswith(""):
    case ".gif":
        print("image/gif")
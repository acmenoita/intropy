# Dictionary associating file extensions with content types
media_types = {
    '.gif': 'image/gif',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.pdf': 'application/pdf',
    '.txt': 'text/plain',
    '.zip': 'application/zip'
}

# Ask the user to provide a file name
file_name = input('File name: ').strip().lower()

#Identify the file by separating from the last period
#If an extension is found, use it; otherwise, assume the files has no extension
if '.' in file_name:
    extension = file_name[file_name.rfind('.'):]
else:
    extension = ''

# Output the corresponding media type or the default one
media_type = media_types.get(extension, 'application/octet-stream')
print(media_type)
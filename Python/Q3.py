import zipfile

# 瞬殺する記述
def Compression(filePath, zipFilePath='./newComp.zip'):
  with zipfile.ZipFile(zipFilePath, 'w', compression=zipfile.ZIP_DEFLATED) as newZipfile:
    newZipfile.write(filePath)

Compression('../img/01.bmp')

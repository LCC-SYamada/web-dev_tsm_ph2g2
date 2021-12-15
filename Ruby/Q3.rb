require 'zlib'

Zlib::GzipWriter.open("01.zip") {|gz|
  data = File.open("../img/01.bmp","rb"){|f| f.read}
  gz.write(data)
  gz.close
}
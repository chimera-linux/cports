pkgname = "fonts-roboto-ttf"
pkgver = "2.138"
pkgrel = 0
pkgdesc = "Roboto family of fonts"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Apache-2.0"
url = "https://github.com/googlefonts/roboto"
source = f"{url}/releases/download/v{pkgver}/roboto-android.zip"
sha256 = "c825453253f590cfe62557733e7173f9a421fff103b00f57d33c4ad28ae53baf"


def install(self):
    self.install_file("*.ttf", "usr/share/fonts/roboto", glob=True)

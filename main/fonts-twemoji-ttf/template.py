pkgname = "fonts-twemoji-ttf"
pkgver = "15.1.0"
pkgrel = 0
pkgdesc = "Twitter Color Emoji SVGinOT Font"
maintainer = "Val Packett <val@packett.cool>"
license = "CC-BY-4.0"
url = "https://github.com/13rac1/twemoji-color-font"
source = f"{url}/releases/download/v{pkgver}/TwitterColorEmoji-SVGinOT-Linux-{pkgver}.tar.gz"
sha256 = "c8a5302ee4e4c2188ce785edd84c50c616a07f6e99fe1b91aecba4e1db341295"


def install(self):
    self.install_file(
        "fontconfig/46-twemoji-color.conf", "usr/share/fontconfig/conf.avail"
    )
    self.install_file(
        "TwitterColorEmoji-SVGinOT.ttf", "usr/share/fonts/twemoji"
    )

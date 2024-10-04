pkgname = "fonts-twemoji-ttf"
pkgver = "15.0.3"
pkgrel = 0
pkgdesc = "Twitter Color Emoji SVGinOT Font"
maintainer = "Val Packett <val@packett.cool>"
license = "CC-BY-4.0"
url = "https://github.com/13rac1/twemoji-color-font"
source = f"{url}/releases/download/v{pkgver}/TwitterColorEmoji-SVGinOT-Linux-{pkgver}.tar.gz"
sha256 = "de6a5cb90dc1684c8f98230eadf58b0385c4f5491f6c082823017d9ca1d3ec7a"


def install(self):
    self.install_file(
        "fontconfig/46-twemoji-color.conf", "usr/share/fontconfig/conf.avail"
    )
    self.install_file(
        "TwitterColorEmoji-SVGinOT.ttf", "usr/share/fonts/twemoji"
    )

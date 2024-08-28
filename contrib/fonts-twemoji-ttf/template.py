pkgname = "fonts-twemoji-ttf"
pkgver = "14.0.2"
pkgrel = 0
pkgdesc = "Twitter Color Emoji SVGinOT Font"
maintainer = "Val Packett <val@packett.cool>"
license = "CC-BY-4.0"
url = "https://github.com/13rac1/twemoji-color-font"
source = f"{url}/releases/download/v{pkgver}/TwitterColorEmoji-SVGinOT-Linux-{pkgver}.tar.gz"
sha256 = "6826e21ea08dc5df26c887ae4e56046987e0f4909df8c02c73de05714a0353c1"


def install(self):
    self.install_file(
        "fontconfig/46-twemoji-color.conf", "usr/share/fontconfig/conf.avail"
    )
    self.install_file(
        "TwitterColorEmoji-SVGinOT.ttf", "usr/share/fonts/twemoji"
    )

pkgname = "fonts-noto-emoji-ttf"
pkgver = "2.048"
pkgrel = 0
pkgdesc = "Google Noto emoji fonts"
license = "OFL-1.1"
url = "https://github.com/googlefonts/noto-emoji"
source = f"{url}/archive/v{pkgver}/font-noto-emoji-{pkgver}.tar.gz"
sha256 = "e6396642172e3d5031bef5f381cc047a007588e73b26209ba1c47b3d1f8faa60"
# No copyright header in license text
options = ["!distlicense"]


def install(self):
    self.install_file(
        "^/66-noto-color-emoji.conf",
        "usr/share/fontconfig/conf.avail",
    )
    self.install_file("fonts/NotoColorEmoji.ttf", "usr/share/fonts/noto")

pkgname = "fonts-noto-emoji-ttf"
pkgver = "2.051"
pkgrel = 0
pkgdesc = "Google Noto emoji fonts"
license = "OFL-1.1"
url = "https://github.com/googlefonts/noto-emoji"
source = f"{url}/archive/v{pkgver}/font-noto-emoji-{pkgver}.tar.gz"
sha256 = "04f3d1e5605edebebac00a7a0becb390a4a3ead015066905b27935b30c18e745"
# No copyright header in license text
options = ["!distlicense"]


def install(self):
    self.install_file(
        "^/66-noto-color-emoji.conf",
        "usr/share/fontconfig/conf.avail",
    )
    self.install_file("fonts/NotoColorEmoji.ttf", "usr/share/fonts/noto")

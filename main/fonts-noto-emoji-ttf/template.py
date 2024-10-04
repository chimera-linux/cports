pkgname = "fonts-noto-emoji-ttf"
pkgver = "2.047"
pkgrel = 0
pkgdesc = "Google Noto emoji fonts"
maintainer = "GeopJr <evan@geopjr.dev>"
license = "OFL-1.1"
url = "https://github.com/googlefonts/noto-emoji"
source = f"{url}/archive/v{pkgver}/font-noto-emoji-{pkgver}.tar.gz"
sha256 = "2cfaf5a427eb26334cdb30d98e4a0c005b660504a339249dc54373e566f09b50"
# No copyright header in license text
options = ["!distlicense"]


def install(self):
    self.install_file(
        self.files_path / "66-noto-color-emoji.conf",
        "usr/share/fontconfig/conf.avail",
    )
    self.install_file("fonts/NotoColorEmoji.ttf", "usr/share/fonts/noto")

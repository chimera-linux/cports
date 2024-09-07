pkgname = "ani-cli"
pkgver = "4.9"
pkgrel = 0
depends = ["aria2", "curl", "fzf", "mpv", "yt-dlp"]
pkgdesc = "CLI to browse and watch anime"
maintainer = "Denis Strizhkin <strdenis02@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/pystardust/ani-cli"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bdd5e3c264ab67760b13d34174ec86c3da3aaaaacda3ba529d8b2648bce2ef08"


def install(self):
    self.install_bin("ani-cli")
    self.install_man("ani-cli.1")

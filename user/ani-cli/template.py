pkgname = "ani-cli"
pkgver = "4.12"
pkgrel = 0
depends = ["aria2", "curl", "fzf", "mpv", "yt-dlp"]
pkgdesc = "CLI to browse and watch anime"
license = "GPL-3.0-or-later"
url = "https://github.com/pystardust/ani-cli"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a247878b8a95d35c5ec6f28abe0594bb3aac29dbd1861531af4a2b909b6b4bed"


def install(self):
    self.install_bin("ani-cli")
    self.install_man("ani-cli.1")

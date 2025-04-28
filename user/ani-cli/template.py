pkgname = "ani-cli"
pkgver = "4.10"
pkgrel = 0
depends = ["aria2", "curl", "fzf", "mpv", "yt-dlp"]
pkgdesc = "CLI to browse and watch anime"
license = "GPL-3.0-or-later"
url = "https://github.com/pystardust/ani-cli"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bf9a61baa70cbbe9028084982b2661c7a0d69823d82534b818abf49e2139d120"


def install(self):
    self.install_bin("ani-cli")
    self.install_man("ani-cli.1")

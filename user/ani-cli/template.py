pkgname = "ani-cli"
pkgver = "4.15"
pkgrel = 0
depends = ["aria2", "botan", "curl", "fzf", "mpv", "yt-dlp"]
pkgdesc = "CLI to browse and watch anime"
license = "GPL-3.0-or-later"
url = "https://github.com/pystardust/ani-cli"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7ede3794978dc2eec87475e0ea96449a604a2589e940c1eab6bfbddb8529f973"


def install(self):
    self.install_bin("ani-cli")
    self.install_man("ani-cli.1")

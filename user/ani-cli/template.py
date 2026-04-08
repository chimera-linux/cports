pkgname = "ani-cli"
pkgver = "4.11"
pkgrel = 0
depends = ["aria2", "curl", "fzf", "mpv", "yt-dlp"]
pkgdesc = "CLI to browse and watch anime"
license = "GPL-3.0-or-later"
url = "https://github.com/pystardust/ani-cli"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "96a0addc9021a029e7b0e421aa60136c004568d23e5e34ca189c395a979f2a29"


def install(self):
    self.install_bin("ani-cli")
    self.install_man("ani-cli.1")

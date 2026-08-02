pkgname = "ani-cli"
pkgver = "5.0"
pkgrel = 0
depends = ["aria2", "botan", "curl", "fzf", "mpv", "yt-dlp"]
pkgdesc = "CLI to browse and watch anime"
license = "GPL-3.0-or-later"
url = "https://github.com/pystardust/ani-cli"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e4703d2f563eee27ea16d92f8e77e3f8a1f07ba8b2433598c3a1ce642841c35c"


def install(self):
    self.install_bin("ani-cli")
    self.install_man("ani-cli.1")

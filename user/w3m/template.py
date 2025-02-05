pkgname = "w3m"
pkgver = "0.5.3_git20230121"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_dir = "."
makedepends = [
    "gc-devel",
    "imlib2-devel",
    "linux-headers",
    "ncurses-devel",
    "openssl3-devel",
]
pkgdesc = "TUI web browser and pager"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/tats/w3m"
source = f"{url}/archive/refs/tags/v{pkgver.replace('_', '+')}.tar.gz"
sha256 = "fdc7d55d3c0104db26aa9759db34f37e5eee03f44c868796e3bbfb8935c96e39"
hardening = ["vis", "!cfi"]


def check(self):
    self.do("sh", "run_tests", wrksrc="tests")


def post_install(self):
    self.install_license("COPYING")

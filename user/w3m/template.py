pkgname = "w3m"
pkgver = "0.5.6"
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
license = "MIT"
url = "https://git.sr.ht/~rkta/w3m"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "8dd652cd3f31817d68c7263c34eeffb50118c80be19e1159bf8cbf763037095e"
hardening = ["vis", "!cfi"]


def check(self):
    self.do("sh", "run", wrksrc="t")


def post_install(self):
    self.install_license("COPYING")

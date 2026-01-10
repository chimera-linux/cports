pkgname = "w3m"
pkgver = "0.5.5"
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
sha256 = "b271c86b13be2207700230cb3f9061271ea37fd1ace199f48b72ea542a529a0f"
hardening = ["vis", "!cfi"]


def check(self):
    self.do("sh", "run", wrksrc="t")


def post_install(self):
    self.install_license("COPYING")

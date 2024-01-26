pkgname = "racket"
pkgver = "8.11.1"
pkgrel = 0
archs = ["aarch64", "x86_64"]
build_wrksrc = "src"
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["automake", "sqlite"]
makedepends = [
    "libffi-devel",
    "lz4-devel",
    "ncurses-devel",
    "zlib-devel",
]
pkgdesc = "Language-oriented programming language"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT OR Apache-2.0"
url = "https://racket-lang.org"
source = f"https://download.racket-lang.org/installers/{pkgver}/racket-{pkgver}-src-builtpkgs.tgz"
sha256 = "47f744eb989e6486c6a6772bc7680a1f07948afdb157ea21b96d1c8b0f7ec447"
# no tests, cross requires external chezscheme
options = ["!check", "!cross"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("racket-devel")
def _devel(self):
    return self.default_devel()

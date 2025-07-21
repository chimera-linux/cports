pkgname = "muon"
pkgver = "0.4.0"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Ddocs=enabled",
    "-Dlibarchive=enabled",
    "-Dlibcurl=enabled",
    "-Dlibpkgconf=enabled",
    "-Dsamurai=disabled",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "python-pyyaml",
    "scdoc",
]
makedepends = [
    "curl-devel",
    "libarchive-devel",
    "pkgconf-devel",
]
depends = ["ninja"]
pkgdesc = "Minimal implementation of meson"
license = "GPL-3.0-only AND Apache-2.0 AND MIT AND Unlicense"
url = "https://muon.build"
source = [
    f"https://git.sr.ht/~lattis/muon/archive/{pkgver}.tar.gz",
    "https://mochiro.moe/wrap/meson-docs-1.5.1-18-g587869c37.tar.gz",
]
source_paths = [".", "subprojects/meson-docs"]
sha256 = [
    "c2ce8302e886b2d3534ec38896a824dc83f43698d085d57bb19a751611d94e86",
    "2a781073f8fdbf0f3c9dcea73cf32a37f12714d6cf0e7054d5dba245c3b564df",
]
# hidden visibility breaks almost all tests
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSES/MIT.txt")

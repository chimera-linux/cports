pkgname = "muon"
pkgver = "0.5.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dmeson-docs=enabled",
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
    "https://github.com/muon-build/meson-docs/archive/1017b3413601044fb41ad04977445e68a80e8181.tar.gz",
]
source_paths = [".", "subprojects/meson-docs"]
sha256 = [
    "565c1b6e1e58f7e90d8813fda0e2102df69fb493ddab4cf6a84ce3647466bee5",
    "ba247999ac7ab9542cb2966a7006b595889ab64f91276f176683ece2a306d97b",
]
# hidden visibility breaks almost all tests
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSES/MIT.txt")

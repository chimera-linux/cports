pkgname = "muon"
pkgver = "0.6.0"
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
    "5300e58c4b4d43e3026856004c79d746075aaa9d9e66d76ba9f32ce249495b81",
    "ba247999ac7ab9542cb2966a7006b595889ab64f91276f176683ece2a306d97b",
]
# hidden visibility breaks almost all tests
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSES/MIT.txt")

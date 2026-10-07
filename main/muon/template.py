pkgname = "muon"
pkgver = "0.7.0"
pkgrel = 0
build_style = "meson"
_docs_commit = "589bc119dfc06bb678fb1688488e508ec51a87b8"
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
    f"https://github.com/muon-build/meson-docs/archive/{_docs_commit}.tar.gz",
]
source_paths = [".", "subprojects/meson-docs"]
sha256 = [
    "e7095741dc11338f5ed8e0aa02e993fc34df4295dad4296127bbb212bcf56e07",
    "55df8d07cb2d430629599ca3913417b91e466dcee9668b139c63d187c9a774f9",
]
# hidden visibility breaks almost all tests
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSES/MIT.txt")

pkgname = "muon"
pkgver = "0.2.0"
pkgrel = 3
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "python-pyyaml",
    "scdoc",
]
makedepends = [
    "libarchive-devel",
    "libcurl-devel",
    "pkgconf-devel",
]
checkdepends = ["git"]
depends = ["ninja"]
pkgdesc = "Minimal implementation of meson"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-only AND Apache-2.0 AND MIT AND Unlicense"
url = "https://muon.build"
source = [
    f"https://git.sr.ht/~lattis/muon/archive/{pkgver}.tar.gz",
    "https://mochiro.moe/wrap/meson-docs-0.64.1-19-g39c6fa4bc.tar.gz",
]
source_paths = [".", "subprojects/meson-docs"]
sha256 = [
    "d73db1be5388821179a25a15ba76fd59a8bf7c8709347a4ec2cb91755203f36c",
    "f6b74283b75085b3e21e851ba4a37934a1793d804d5bacfb3f5e870dd305c85d",
]
# hidden visibility breaks almost all tests
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSES/MIT.txt")

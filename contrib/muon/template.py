pkgname = "muon"
pkgver = "0.2.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "scdoc"]
makedepends = ["libarchive-devel", "libcurl-devel", "pkgconf-devel"]
checkdepends = ["git"]
pkgdesc = "Minimal implementation of meson"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-only AND Apache-2.0 AND MIT AND Unlicense"
url = "https://muon.build"
source = f"https://git.sr.ht/~lattis/muon/archive/{pkgver}.tar.gz"
sha256 = "d73db1be5388821179a25a15ba76fd59a8bf7c8709347a4ec2cb91755203f36c"
# hidden visibility breaks almost all tests
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSES/MIT.txt")

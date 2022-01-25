pkgname = "cracklib"
pkgver = "2.9.7"
pkgrel = 0
build_wrksrc = f"{pkgname}-{pkgver}"
build_style = "gnu_configure"
configure_args = ["--disable-static"]
hostmakedepends = ["pkgconf", "gettext-tiny-devel"]
pkgdesc = "Password checking library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/cracklib/cracklib"
source = [
    f"{url}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz",
    f"{url}/releases/download/v{pkgver}/{pkgname}-words-{pkgver}.gz"
]
sha256 = [
    "8b6fd202f3f1d8fa395d3b7a5d821227cfd8bb4a9a584a7ae30cf62cea6287dd",
    "7f0c45faf84a2494f15d1e2720394aca4a379163a70c4acad948186c0047d389",
]

def post_install(self):
    self.install_file(
        f"../{pkgname}-words-{pkgver}", "usr/share/cracklib",
        name = "cracklib-words"
    )

@subpackage("cracklib-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libcrack")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()

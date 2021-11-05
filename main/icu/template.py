pkgname = "icu"
pkgver = "70.1"
pkgrel = 0
build_wrksrc = "source"
build_style = "gnu_configure"
configure_args = [
    "--with-data-packaging=archive",
    "--enable-static",
]
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
checkdepends = ["python"]
pkgdesc = "Robust and fully-featured Unicode libraries"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ICU"
url = "https://home.unicode.org"
source = f"https://github.com/unicode-org/{pkgname}/releases/download/release-{pkgver.replace('.', '-')}/icu4c-{pkgver.replace('.', '_')}-src.tgz"
sha256 = "8d205428c17bf13bb535300669ed28b338a157b1c01ae66d31d0d3e2d47c3fd5"
tool_flags = {"CFLAGS": ["-fPIC"], "CXXFLAGS": ["-fPIC"]}
# cba for now
options = ["!cross"]

def post_install(self):
    self.install_license(self.builddir / self.wrksrc / "LICENSE")

@subpackage("icu-libs")
def _libs(self):
    return self.default_libs(extra = [
        f"usr/share/icu/{pkgver}/icudt*.dat"
    ])

@subpackage("icu-devel")
def _devel(self):
    return self.default_devel(extra = ["usr/share/icu", "usr/lib/icu"])

pkgname = "kimageannotator"
pkgver = "0.7.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_EXAMPLE=OFF",
    "-DBUILD_SHARED_LIBS=ON",
    "-DBUILD_TESTS=ON",
    "-DBUILD_WITH_QT6=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "gtest-devel",
    "kcolorpicker-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "Tool for annotating images"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://github.com/ksnip/kImageAnnotator"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2335c5be15a5dde34c3333c10a6339da114e2232e4c4642dea1793e491e09677"
# CFI: crashes in tests
hardening = ["vis", "!cfi"]


def check(self):
    from cbuild.util import cmake

    cmake.ctest(
        self,
        f"{self.make_dir}/tests",
        wrapper=["wlheadless-run", "--"],
    )


@subpackage("kimageannotator-devel")
def _(self):
    self.depends += ["kcolorpicker-devel"]
    return self.default_devel()

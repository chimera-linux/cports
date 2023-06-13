pkgname = "qt6-qtwayland"
pkgver = "6.5.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DQT_BUILD_TESTS=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "perl",
    "qt6-qtbase",
    "qt6-qtdeclarative-devel",
]
makedepends = ["qt6-qtbase-devel", "qt6-qtdeclarative-devel"]
checkdepends = ["mesa-dri"]
pkgdesc = "Qt6 Wayland component"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtwayland-everywhere-src-{pkgver}.tar.xz"
sha256 = "ccc57fa277fc5f1c1c2c4733eae80a60996b67a067233c47809e542aa31759a3"
debug_level = 1  # defatten, especially with LTO
# FIXME
hardening = ["!int"]
# TODO
options = ["!cross"]


def do_check(self):
    self.do(
        "ctest",
        "-E",
        "tst_seatv4$",
        wrksrc=self.make_dir,
        env={
            "QT_QPA_PLATFORM": "offscreen",
            "CTEST_OUTPUT_ON_FAILURE": "True",
        },
    )


@subpackage("qt6-qtwayland-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/qt6/libexec",
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )

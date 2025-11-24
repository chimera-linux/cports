pkgname = "qt6-qtimageformats"
pkgver = "6.10.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libtiff-devel",
    "libwebp-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "Qt6 additional image formats component"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtimageformats-everywhere-src-{pkgver}.tar.xz"
sha256 = "498eabdf2381db96f808942b3e3c765f6360fe6c0e9961f0a45ff7a4c68d7a72"
# cross: TODO
options = ["!cross"]


def init_check(self):
    self.make_check_env = {
        "QT_QPA_PLATFORM": "offscreen",
        "QML2_IMPORT_PATH": str(
            self.chroot_cwd / f"{self.make_dir}/lib/qt6/qml"
        ),
    }


@subpackage("qt6-qtimageformats-devel")
def _(self):
    self.depends += [
        self.parent,
        f"qt6-qtbase-devel~{pkgver[:-2]}",
        f"qt6-qtdeclarative-devel~{pkgver[:-2]}",
        f"qt6-qtmultimedia-devel~{pkgver[:-2]}",
    ]
    return self.default_devel()

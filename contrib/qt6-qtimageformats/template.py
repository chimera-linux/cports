pkgname = "qt6-qtimageformats"
pkgver = "6.7.2"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtimageformats-everywhere-src-{pkgver}.tar.xz"
sha256 = "e1a1d8785fae67d16ad0a443b01d5f32663a6b68d275f1806ebab257485ce5d6"
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
def _devel(self):
    self.depends += [
        self.parent,
        f"qt6-qtbase-devel~{pkgver[:-2]}",
        f"qt6-qtdeclarative-devel~{pkgver[:-2]}",
        f"qt6-qtmultimedia-devel~{pkgver[:-2]}",
    ]
    return self.default_devel()

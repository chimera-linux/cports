pkgname = "qt6-qtconnectivity"
pkgver = "6.9.1"
pkgrel = 0
build_style = "cmake"
# cmake import
make_check_args = ["-E", "module_includes"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "bluez-devel",
    "linux-headers",
    "qt6-qtbase-private-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "Qt6 Connectivity component"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtconnectivity-everywhere-src-{pkgver}.tar.xz"
sha256 = "4988e50112104d5ad85e5b3cef66036ca445f18c22cf375d3dac9dcca95e0a17"


def init_check(self):
    self.make_check_env = {
        "QT_QPA_PLATFORM": "offscreen",
        "QML2_IMPORT_PATH": str(
            self.chroot_cwd / f"{self.make_dir}/lib/qt6/qml"
        ),
    }


@subpackage("qt6-qtconnectivity-devel")
def _(self):
    self.depends += [
        f"qt6-qtbase-devel~{pkgver[:-2]}",
        f"qt6-qtdeclarative-devel~{pkgver[:-2]}",
    ]
    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )

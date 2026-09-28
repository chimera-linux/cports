pkgname = "qt6-qtgraphs"
pkgver = "6.11.2"
pkgrel = 0
build_style = "cmake"
# hangs forever
make_check_args = ["-E", "tst_qgqmltest"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qtbase-private-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtquick3d-devel",
]
pkgdesc = "Qt6 Graphs component"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtgraphs-everywhere-src-{pkgver}.tar.xz"
sha256 = "9f2109854afa45dd144116c11461989c411a17065c63da5068441a1200fb8b21"
# FIXME? crashes with eg easyeffects
hardening = ["!int"]


def init_check(self):
    self.make_check_env = {
        "QML2_IMPORT_PATH": str(
            self.chroot_cwd / f"{self.make_dir}/lib/qt6/qml"
        ),
        "QT_QPA_PLATFORM": "offscreen",
    }


def post_install(self):
    self.uninstall("usr/tests")


@subpackage("qt6-qtgraphs-devel")
def _(self):
    self.depends += [
        f"qt6-qtbase-devel~{pkgver[:-2]}",
        f"qt6-qtdeclarative-devel~{pkgver[:-2]}",
        f"qt6-qtquick3d-devel~{pkgver[:-2]}",
    ]
    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )

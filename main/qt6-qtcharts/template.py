pkgname = "qt6-qtcharts"
pkgver = "6.7.3"
pkgrel = 0
build_style = "cmake"
# module_includes: fails to find cmake imports
# qbarseries: hangs and then fails
make_check_args = ["-E", "(module_includes|tst_qbarseries)"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qtbase-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtmultimedia-devel",  # unused but lightly checked anyway
]
pkgdesc = "Qt6 Charts component"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtcharts-everywhere-src-{pkgver}.tar.xz"
sha256 = "07ea63a550e6bcfa4a9c38056f7aa524357305572268fe26f6063d83e4233659"
# cross: TODO
options = ["!cross"]


def init_check(self):
    self.make_check_env = {
        "QML2_IMPORT_PATH": str(
            self.chroot_cwd / f"{self.make_dir}/lib/qt6/qml"
        ),
        "QT_QPA_PLATFORM": "offscreen",
    }


def post_install(self):
    self.uninstall("usr/tests")


@subpackage("qt6-qtcharts-devel")
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

pkgname = "qt6-qtcharts"
pkgver = "6.7.2"
pkgrel = 0
build_style = "cmake"
# module_includes: fails to find cmake imports
# qbarseries: hangs and then fails
make_check_args = ["-E", "(module_includes|tst_qbarseries)"]
make_check_wrapper = ["wlheadless-run", "--"]
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
checkdepends = ["xwayland-run"]
pkgdesc = "Qt6 Charts component"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtcharts-everywhere-src-{pkgver}.tar.xz"
sha256 = "00f6a437458b7f2c4e81d748dbe2a077567a9e6ad8d8e3820b36c39dc5279bda"
# cross: TODO
options = ["!cross"]


def init_check(self):
    self.make_check_env = {
        "QML2_IMPORT_PATH": str(
            self.chroot_cwd / f"{self.make_dir}/lib/qt6/qml"
        ),
    }


def post_install(self):
    self.uninstall("usr/tests")


@subpackage("qt6-qtcharts-devel")
def _devel(self):
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

pkgname = "qt6-qtscxml"
pkgver = "6.9.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DQT_BUILD_TESTS=ON"]
make_check_args = [
    "-E",
    "(module_includes|test_qtscxml_module|tst_scion|tst_qstatemachine)",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "perl",
    "pkgconf",
    "qt6-qtbase",
    "qt6-qtdeclarative-devel",
]
makedepends = [
    "qt6-qtbase-private-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "Qt6 SCXML component"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtscxml-everywhere-src-{pkgver}.tar.xz"
sha256 = "0c33de2023b33a54fa6debd46f422440dca92da532faa7742af051fd88254780"


def init_check(self):
    self.make_check_env = {
        "QML2_IMPORT_PATH": str(
            self.chroot_cwd / f"{self.make_dir}/lib/qt6/qml"
        ),
        "QT_QPA_PLATFORM": "offscreen",
    }


def post_install(self):
    self.uninstall("usr/tests")


@subpackage("qt6-qtscxml-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/qt6/libexec",
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )

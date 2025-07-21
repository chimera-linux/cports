pkgname = "qt6-qtquick3d"
pkgver = "6.9.1"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DQT_FEATURE_system_assimp=ON"]
make_check_args = ["-E", "module_includes"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "assimp-devel",
    "qt6-qtbase-private-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtquicktimeline-devel",
    "qt6-qtshadertools-devel",
]
pkgdesc = "Qt6 Quick 3D component"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtquick3d-everywhere-src-{pkgver}.tar.xz"
sha256 = "f61600da8fbfd51b7d6b5c431cef453d7c24015c374ae25756c0faf0db2c9977"
# cross: TODO
options = ["!cross"]


def init_check(self):
    self.make_check_env = {
        "QT_QPA_PLATFORM": "offscreen",
        "QML2_IMPORT_PATH": str(
            self.chroot_cwd / f"{self.make_dir}/lib/qt6/qml"
        ),
    }


def post_install(self):
    self.uninstall("usr/tests")


@subpackage("qt6-qtquick3d-devel")
def _(self):
    self.depends += [
        f"qt6-qtbase-devel~{pkgver[:-2]}",
        f"qt6-qtdeclarative-devel~{pkgver[:-2]}",
        f"qt6-qtquicktimeline-devel~{pkgver[:-2]}",
    ]
    return self.default_devel(
        extra=[
            "usr/lib/qt6/bin",
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/qt6/plugins/qmltooling/libqmldbg_quick3dprofiler.so",
            "usr/lib/*.prl",
        ]
    )

pkgname = "qt6-qttools"
pkgver = "6.6.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DQT_BUILD_TESTS=OFF",  # downloads gtest
    "-DINSTALL_PUBLICBINDIR=usr/bin",
    "-DLITEHTML_UTF8=ON",
    "-DQT_BUILD_SHARED_LIBS=ON",
    "-DQT_FEATURE_assistant=ON",
    "-DQT_FEATURE_pixeltool=ON",
    "-DQT_FEATURE_distancefieldgenerator=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "perl",
    "qt6-qtbase",
    "clang-tools-extra",
    "qt6-qtdeclarative-devel",
]
makedepends = [
    "qt6-qtbase-devel",
    "qt6-qtdeclarative-devel",
    "llvm-devel",
    "clang-devel",
    "clang-tools-extra",
]
pkgdesc = "Qt6 tools"
maintainer = "q66 <q66@chimera-linux.org>"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qttools-everywhere-src-{pkgver}.tar.xz"
sha256 = "e6d49e9f52111287f77878ecb8b708cce682f10b03ba2476d9247603bc6c4746"
debug_level = 1  # defatten, especially with LTO
# FIXME
hardening = ["!int"]
# TODO
options = ["!check"]

# why?
nopie_files = ["usr/lib/qt6/bin/lupdate", "usr/lib/qt6/bin/qdoc"]


def post_install(self):
    # hardlink
    self.rm(self.destdir / "usr/lib/qt6/bin/qtdiag")
    self.install_link("qtdiag6", "usr/lib/qt6/bin/qtdiag")

    # link publicbindir utils to usr/bin, like qmake6
    # used outside of cmake
    self.install_dir("usr/bin")
    with open(
        self.cwd / self.make_dir / "user_facing_tool_links.txt", "r"
    ) as f:
        for line in f.readlines():
            self.install_link(*line.split())


@subpackage("qt6-qttools-libs")
def _libs(self):
    return self.default_libs()


@subpackage("qt6-qttools-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )

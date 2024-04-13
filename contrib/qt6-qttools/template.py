pkgname = "qt6-qttools"
pkgver = "6.7.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DQT_BUILD_TESTS=OFF",  # downloads gtest
    "-DINSTALL_PUBLICBINDIR=usr/bin",
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
sha256 = "c8da6b239e82fe1e23465cbf0936c0da5a334438d3fb433e19c503cbb1abee7b"
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
    self.install_link("usr/lib/qt6/bin/qtdiag", "qtdiag6")

    # link publicbindir utils to usr/bin, like qmake6
    # used outside of cmake
    self.install_dir("usr/bin")
    with open(
        self.cwd / self.make_dir / "user_facing_tool_links.txt", "r"
    ) as f:
        for line in f.readlines():
            a, b = line.split()
            self.install_link(b, a.replace("/usr/lib", "../lib"))


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

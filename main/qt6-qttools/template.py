pkgname = "qt6-qttools"
pkgver = "6.9.3"
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
    "clang-tools-extra",
    "cmake",
    "ninja",
    "perl",
    "pkgconf",
    "qt6-qtbase",
    "qt6-qtdeclarative-devel",
]
makedepends = [
    "clang-devel",
    "clang-tools-extra",
    "llvm-devel",
    "qt6-qtbase-private-devel",
    "qt6-qtdeclarative-devel",
]
depends = [self.with_pkgver("qt6-qttools-qdbus")]
pkgdesc = "Qt6 tools"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qttools-everywhere-src-{pkgver}.tar.xz"
sha256 = "0cf7ab0e975fc57f5ce1375576a0a76e9ede25e6b01db3cf2339cd4d9750b4e9"
# FIXME
hardening = ["!int"]
# TODO
options = ["!check"]


def post_install(self):
    # hardlink
    self.uninstall("usr/lib/qt6/bin/qtdiag")
    self.install_link("usr/lib/qt6/bin/qtdiag", "qtdiag6")

    # link publicbindir utils to usr/bin, like qmake6
    # used outside of cmake
    self.install_dir("usr/bin")
    with open(
        self.cwd / self.make_dir / "user_facing_tool_links.txt", "r"
    ) as f:
        for line in f.readlines():
            a, b = line.split()
            self.install_link(b, a.replace("../../lib", "../lib"))


@subpackage("qt6-qttools-qdbus")
def _(self):
    self.subdesc = "qdbus"

    return [
        "usr/bin/qdbus*6",
        "usr/lib/qt6/bin/qdbus*",
    ]


@subpackage("qt6-qttools-libs")
def _(self):
    return self.default_libs()


@subpackage("qt6-qttools-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )

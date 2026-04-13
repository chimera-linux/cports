pkgname = "qt6-qttools"
pkgver = "6.10.2"
pkgrel = 1
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
    "perl",
    "pkgconf",
    "qt6-qtbase",
    "qt6-qtdeclarative-devel",
]
makedepends = [
    "clang-devel",
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
sha256 = "1e3d2c07c1fd76d2425c6eaeeaa62ffaff5f79210c4e1a5bc2a6a9db668d5b24"
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

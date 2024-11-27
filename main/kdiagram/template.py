pkgname = "kdiagram"
pkgver = "3.0.1"
pkgrel = 0
build_style = "cmake"
# FIXME: segfault in cxx_atomic_load from ptr assign because ->grid is null
make_check_args = ["-E", "(KGanttView)"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE libraries for creating diagrams"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://invent.kde.org/graphics/kdiagram"
source = f"$(KDE_SITE)/kdiagram/{pkgver}/kdiagram-{pkgver}.tar.xz"
sha256 = "4659b0c2cd9db18143f5abd9c806091c3aab6abc1a956bbf82815ab3d3189c6d"


@subpackage("kdiagram-devel")
def _(self):
    self.depends += [
        "qt6-qtbase-devel",
        "qt6-qtsvg-devel",
    ]
    return self.default_devel()

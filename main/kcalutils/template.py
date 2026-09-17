pkgname = "kcalutils"
pkgver = "26.08.1"
pkgrel = 0
build_style = "cmake"
# doesn't find its own text template plugin
make_check_args = ["-E", "(testdndfactory|testincidenceformatter)"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "grantleetheme-devel",
    "kcalendarcore-devel",
    "kcodecs-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kidentitymanagement-devel",
    "ktexttemplate-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE calendar access library"
license = "LGPL-2.1-or-later"
url = "https://community.kde.org/KDE_PIM"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kcalutils-{pkgver}.tar.xz"
sha256 = "a8db4527bb98e7152ada184a2a998bb88f44f975b8c4bda0907a3ee56c52561c"


@subpackage("kcalutils-devel")
def _(self):
    self.depends += [
        "kcalendarcore-devel",
        "kconfig-devel",
        "kcoreaddons-devel",
    ]
    return self.default_devel()

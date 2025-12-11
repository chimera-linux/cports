pkgname = "kcalutils"
pkgver = "25.12.0"
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
url = "https://api.kde.org/kdepim/kcalutils/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kcalutils-{pkgver}.tar.xz"
sha256 = "43048134e055ffa3e757fde34ebd1bedec8dff6f268e73ec70c8ceffb9433cc0"


@subpackage("kcalutils-devel")
def _(self):
    self.depends += [
        "kcalendarcore-devel",
        "kconfig-devel",
        "kcoreaddons-devel",
    ]
    return self.default_devel()

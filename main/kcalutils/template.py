pkgname = "kcalutils"
pkgver = "26.04.3"
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
sha256 = "a822d1cc8c2b08ae7944c6a574f32f91abe3a1b86adecf70e8bea4b353de88f6"


@subpackage("kcalutils-devel")
def _(self):
    self.depends += [
        "kcalendarcore-devel",
        "kconfig-devel",
        "kcoreaddons-devel",
    ]
    return self.default_devel()

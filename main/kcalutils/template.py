pkgname = "kcalutils"
pkgver = "24.08.3"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/kdepim/kcalutils/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kcalutils-{pkgver}.tar.xz"
sha256 = "7687ce2e3121d1c399ec5d9b3da22c894cd0740cbfce232ce2e2b2d2ce63d820"


@subpackage("kcalutils-devel")
def _(self):
    self.depends += [
        "kcalendarcore-devel",
        "kconfig-devel",
        "kcoreaddons-devel",
    ]
    return self.default_devel()

pkgname = "ksystemlog"
pkgver = "24.08.2"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    # "audit-devel",
    "karchive-devel",
    "kcompletion-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "kitemviews-devel",
    "ktextwidgets-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE system log viewer"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/ksystemlog"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/ksystemlog-{pkgver}.tar.xz"
sha256 = "77b8e629cd9cc09fe583e99bbaffeafeb37d8eda1b2c6cb4082a9427faa6a96e"

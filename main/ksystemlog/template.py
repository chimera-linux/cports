pkgname = "ksystemlog"
pkgver = "25.08.0"
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
    "kcrash-devel",
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
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/ksystemlog"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/ksystemlog-{pkgver}.tar.xz"
sha256 = "3083a32e43c257e4b0d91b2465c0acdf4936d31b5214de1d207b13de063ed869"

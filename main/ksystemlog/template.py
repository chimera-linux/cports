pkgname = "ksystemlog"
pkgver = "25.04.3"
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
sha256 = "cbac290076ee16d35816015a8c99fe297a9093898d0beac29c734bc9e0226afe"

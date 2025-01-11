pkgname = "ksystemlog"
pkgver = "24.12.1"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/ksystemlog"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/ksystemlog-{pkgver}.tar.xz"
sha256 = "fae75112ee5f9231251f7e6a5c77bdf2dda3350d4d8e5e9ca9fa44b7c2d15763"

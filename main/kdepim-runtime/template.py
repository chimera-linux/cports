pkgname = "kdepim-runtime"
pkgver = "25.04.1"
pkgrel = 0
build_style = "cmake"
make_check_args = ["-j1", "-E", "(akonadi-sqlite-.*)"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
    "libxslt-progs",
]
makedepends = [
    "akonadi-calendar-devel",
    "akonadi-contacts-devel",
    "akonadi-devel",
    "akonadi-mime-devel",
    "kcalendarcore-devel",
    "kcalutils-devel",
    "kcmutils-devel",
    "kcodecs-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcontacts-devel",
    "kdav-devel",
    "kidentitymanagement-devel",
    "kimap-devel",
    "kio-devel",
    "kitemmodels-devel",
    "kldap-devel",
    "kmailtransport-devel",
    "kmbox-devel",
    "kmime-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "ktextaddons-devel",
    "ktextwidgets-devel",
    "kwallet-devel",
    "kwindowsystem-devel",
    "libkgapi-devel",
    "libsasl-devel",
    "qca-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtnetworkauth-devel",
    "qt6-qtspeech-devel",
    "qt6-qtwebengine-devel",
    "qtkeychain-devel",
    "pimcommon-devel",
    "shared-mime-info",
]
depends = ["shared-mime-info"]
checkdepends = ["xwayland-run", *depends]
pkgdesc = "KDE PIM Akonadi agents and runtime resources"
license = "LGPL-3.0-only AND GPL-2.0-or-later"
url = "https://invent.kde.org/pim/kdepim-runtime"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kdepim-runtime-{pkgver}.tar.xz"
)
sha256 = "959c5335d00c8eb05b17742da1b7a142b8c6f91884194f3f9bfc09f57f2331ee"

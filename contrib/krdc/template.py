pkgname = "krdc"
pkgver = "24.05.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DQT_MAJOR_VERSION=6"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "freerdp",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qtbase-devel",
    "kconfig-devel",
    "kcmutils-devel",
    "kdnssd-devel",
    "knotifyconfig-devel",
    "knotifications-devel",
    "kbookmarks-devel",
    "kiconthemes-devel",
    "kxmlgui-devel",
    "kcompletion-devel",
    "kwallet-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "ki18n-devel",
    "kio-devel",
    "kstatusnotifieritem-devel",
    "plasma-activities-devel",
    "kdoctools-devel",
    "libvncserver-devel",
    "libssh-devel",
    "freerdp-devel",
]
depends = ["freerdp"]
pkgdesc = "KDE remote desktop client"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/krdc"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/krdc-{pkgver}.tar.xz"
sha256 = "b08c94f736aaa8c0826895ae155230b9a25c5f40306caeada5a4523a889e8977"


@subpackage("krdc-devel")
def _devel(self):
    return self.default_devel()

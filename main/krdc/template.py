pkgname = "krdc"
pkgver = "24.08.2"
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
    "freerdp-devel",
    "kbookmarks-devel",
    "kcmutils-devel",
    "kcompletion-devel",
    "kconfig-devel",
    "kdnssd-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "kstatusnotifieritem-devel",
    "kwallet-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "libssh-devel",
    "libvncserver-devel",
    "plasma-activities-devel",
    "qt6-qtbase-devel",
    "qt6-qtwayland-devel",
]
depends = ["freerdp"]
pkgdesc = "KDE remote desktop client"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/krdc"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/krdc-{pkgver}.tar.xz"
sha256 = "0fbd55a28095d3c84649cfdbe12dd868ddecc23205f698ed03e824585c8bc60b"


@subpackage("krdc-devel")
def _(self):
    return self.default_devel()

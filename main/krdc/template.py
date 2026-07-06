pkgname = "krdc"
pkgver = "26.04.3"
pkgrel = 0
build_style = "cmake"
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
    "kcrash-devel",
    "kdnssd-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "kstatusnotifieritem-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "libssh-devel",
    "libvncserver-devel",
    "plasma-activities-devel",
    "qt6-qtbase-devel",
    "qt6-qtwayland-devel",
    "qtkeychain-devel",
]
depends = ["freerdp"]
pkgdesc = "KDE remote desktop client"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/krdc"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/krdc-{pkgver}.tar.xz"
sha256 = "74cd7e55f2a0a72a8211043122bdaaf1d15fe8393466baa57b593feb3ae1fd04"


@subpackage("krdc-devel")
def _(self):
    return self.default_devel()

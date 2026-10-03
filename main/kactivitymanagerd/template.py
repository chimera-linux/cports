pkgname = "kactivitymanagerd"
pkgver = "6.7.91"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "boost-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kio-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
]
# depends = ["qt6-qtbase-sql"]
pkgdesc = "KDE Manage user's activities and track usage patterns"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://invent.kde.org/plasma/kactivitymanagerd"
source = (
    f"$(KDE_UNSTABLE_SITE)/plasma/{pkgver}/kactivitymanagerd-{pkgver}.tar.xz"
)
sha256 = "91a60306e305c4795a532f5595278e26353149daa86fc7d84068c769de90bd60"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")

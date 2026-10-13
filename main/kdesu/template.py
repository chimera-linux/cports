pkgname = "kdesu"
pkgver = "6.31.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kpty-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Framework for running commands as root"
license = "GPL-2.0-only"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kdesu-{pkgver}.tar.xz"
sha256 = "4e3ed141d538f6d3ee02d5ebad6dd08c260fa38fd0005317d0cd15c23ee7c676"
hardening = ["vis"]


@subpackage("kdesu-devel")
def _(self):
    self.depends += ["kpty-devel"]
    return self.default_devel()

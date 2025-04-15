pkgname = "kdesu"
pkgver = "6.13.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kpty-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Framework for running commands as root"
license = "GPL-2.0-only"
url = "https://api.kde.org/frameworks/kdesu/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kdesu-{pkgver}.tar.xz"
sha256 = "6be91eb21912bb2521f4e4f19267639c3bed33ab5dd09f79f279e2f94c380a62"
hardening = ["vis"]


@subpackage("kdesu-devel")
def _(self):
    self.depends += ["kpty-devel"]
    return self.default_devel()

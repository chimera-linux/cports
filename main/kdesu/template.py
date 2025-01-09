pkgname = "kdesu"
pkgver = "6.9.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only"
url = "https://api.kde.org/frameworks/kdesu/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kdesu-{pkgver}.tar.xz"
sha256 = "1a84a461371ed0984e7ab225c974e80e5f1afb70dfce57582a9b67cdb40ed1ba"
hardening = ["vis"]


@subpackage("kdesu-devel")
def _(self):
    self.depends += ["kpty-devel"]
    return self.default_devel()

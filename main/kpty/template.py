pkgname = "kpty"
pkgver = "6.32.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = ["kcoreaddons-devel", "ki18n-devel", "qt6-qttools-devel"]
pkgdesc = "KDE Interface to pseudo terminal devices"
license = "LGPL-2.1-or-later"
url = "https://community.kde.org/Frameworks"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kpty-{pkgver}.tar.xz"
)
sha256 = "ed8a6feee493a1b98930fb78d40e09a5a7983ec2f29ced0afc83ffbdb54f6152"
hardening = ["vis"]


@subpackage("kpty-devel")
def _(self):
    return self.default_devel()

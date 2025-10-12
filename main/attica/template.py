pkgname = "attica"
pkgver = "6.19.0"
pkgrel = 0
build_style = "cmake"
# requires network access and passes in cbuild chroot
make_check_args = ["-E", "providertest"]
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja", "pkgconf"]
makedepends = ["qt6-qttools-devel"]
pkgdesc = "Freedesktop Open Collaboration Services (OCS) binding for Qt"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/attica/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/attica-{pkgver}.tar.xz"
sha256 = "30813efb577f75b87eec4f02300a906e5f39a8dd2c7e7488958a7ffeaaaee1a8"
hardening = ["vis"]


@subpackage("attica-devel")
def _(self):
    return self.default_devel()

pkgname = "attica"
pkgver = "6.28.0"
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
sha256 = "652e28562ed6798f834843b45f5cd3ea5833f0ee3c2607cfe3d021b57c6e7618"
hardening = ["vis"]


@subpackage("attica-devel")
def _(self):
    return self.default_devel()

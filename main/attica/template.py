pkgname = "attica"
pkgver = "6.18.0"
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
sha256 = "eb2b2be33cc83512c77af2559fcaf7fc58ad191abb82cf40b17b2e9e8400e336"
hardening = ["vis"]


@subpackage("attica-devel")
def _(self):
    return self.default_devel()

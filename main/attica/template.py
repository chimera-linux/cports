pkgname = "attica"
pkgver = "6.31.0"
pkgrel = 0
build_style = "cmake"
# requires network access and passes in cbuild chroot
make_check_args = ["-E", "providertest"]
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja", "pkgconf"]
makedepends = ["qt6-qttools-devel"]
pkgdesc = "Freedesktop Open Collaboration Services (OCS) binding for Qt"
license = "LGPL-2.0-or-later"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/attica-{pkgver}.tar.xz"
sha256 = "5699601e3a957e1eebf8fbe8b1f3d908df3c0a775919bc796b0830b34b59a67d"
hardening = ["vis"]


@subpackage("attica-devel")
def _(self):
    return self.default_devel()

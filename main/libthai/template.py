pkgname = "libthai"
pkgver = "0.1.29"
pkgrel = 0
build_style = "gnu_configure"
# fails to regen
configure_gen = []
make_install_args = ["-j1"]
hostmakedepends = ["pkgconf"]
makedepends = ["libdatrie-devel"]
pkgdesc = "Thai language support routines"
license = "LGPL-2.1-or-later"
url = "https://linux.thai.net/projects/libthai"
source = f"https://linux.thai.net/pub/ThaiLinux/software/libthai/libthai-{pkgver}.tar.xz"
sha256 = "fc80cc7dcb50e11302b417cebd24f2d30a8b987292e77e003267b9100d0f4bcd"

if self.profile().cross:
    hostmakedepends += ["libdatrie"]


@subpackage("libthai-devel")
def _(self):
    return self.default_devel()

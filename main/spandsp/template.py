pkgname = "spandsp"
pkgver = "0.0.6"
pkgrel = 0
build_style = "gnu_configure"
make_install_args = ["-j1"]
hostmakedepends = ["pkgconf"]
makedepends = ["libtiff-devel", "libjpeg-turbo-devel"]
pkgdesc = "Low-level signal processing library for telephony"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later AND GPL-2.0-or-later"
url = "https://www.soft-switch.org"
source = f"$(DEBIAN_SITE)/main/s/{pkgname}/{pkgname}_{pkgver}+dfsg.orig.tar.xz"
sha256 = "3dcdc611b8a119f1f26540d05e6279c4c1e5cd576271f6d45df431359fc190f9"
hardening = ["!cfi"]  # TODO


@subpackage("spandsp-devel")
def _devel(self):
    self.depends += ["libtiff-devel"]

    return self.default_devel()


configure_gen = []

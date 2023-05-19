pkgname = "startup-notification"
pkgver = "0.12"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["lf_cv_sane_realloc=yes", "lf_cv_sane_malloc=yes"]
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel", "libsm-devel", "xcb-util-devel"]
pkgdesc = "Library for tracking application startup"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://www.freedesktop.org/wiki/Software/startup-notification"
source = f"$(FREEDESKTOP_SITE)/{pkgname}/releases/{pkgname}-{pkgver}.tar.gz"
sha256 = "3c391f7e930c583095045cd2d10eb73a64f085c7fde9d260f2652c7cb3cfbe4a"
# the unit test code is broken (passing char * to int args)
options = ["!check"]

@subpackage("startup-notification-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []

pkgname = "libxinerama"
pkgver = "1.1.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxext-devel"]
pkgdesc = "PanoramiX extension library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXinerama-{pkgver}.tar.gz"
sha256 = "2efa855cb42dc620eff3b77700d8655695e09aaa318f791f201fa60afa72b95c"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxinerama-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []

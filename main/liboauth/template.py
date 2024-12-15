pkgname = "liboauth"
pkgver = "1.0.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-nss"]
# bashisms in configure script
configure_env = {"CONFIG_SHELL": "/usr/bin/bash"}
make_dir = "."  # tests broken otherwise
hostmakedepends = ["pkgconf", "bash"]
makedepends = ["curl-devel", "nss-devel"]
pkgdesc = "C implementation of the OAuth protocol"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://sourceforge.net/projects/liboauth"
source = f"$(SOURCEFORGE_SITE)/liboauth/liboauth-{pkgver}.tar.gz"
sha256 = "0df60157b052f0e774ade8a8bac59d6e8d4b464058cc55f9208d72e41156811f"


def post_install(self):
    self.install_license("COPYING.MIT")


@subpackage("liboauth-devel")
def _(self):
    return self.default_devel()


configure_gen = []

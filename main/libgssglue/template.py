pkgname = "libgssglue"
pkgver = "0.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "Mechanism-switch gssapi library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://www.citi.umich.edu/projects/nfsv4/linux"
source = f"{url}/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "3f791a75502ba723e5e85e41e5e0c711bb89e2716b7c0ec6e74bd1df6739043a"


def post_install(self):
    self.install_file(self.files_path / "gssapi_mech.conf", "etc")
    self.install_license("COPYING")


@subpackage("libgssglue-devel")
def _devel(self):
    return self.default_devel()

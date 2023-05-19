pkgname = "attr"
pkgver = "2.5.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    f"--libdir=/usr/lib",
    f"--libexecdir=/usr/lib"
]
make_check_args = ["-j1"] # Tests broken when ran in parallel
hostmakedepends = ["pkgconf"]
checkdepends = ["perl"]
pkgdesc = "Extended attribute support library for ACL support"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://savannah.nongnu.org/projects/attr"
source = f"$(NONGNU_SITE)/attr/attr-{pkgver}.tar.gz"
sha256 = "bae1c6949b258a0d68001367ce0c741cebdacdd3b62965d17e5eb23cd78adaf8"
options = ["bootstrap"]

@subpackage("attr-devel")
def _devel(self):
    return self.default_devel(extra = ["usr/share/doc"])

@subpackage("attr-progs")
def _progs(self):
    return self.default_progs(extra = ["usr/share"])

configure_gen = []

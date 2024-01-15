pkgname = "attr"
pkgver = "2.5.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--libdir=/usr/lib", "--libexecdir=/usr/lib"]
# cycle with automake -> chimerautils
configure_gen = []
make_check_args = ["-j1"]  # Tests broken when ran in parallel
hostmakedepends = ["pkgconf"]
checkdepends = ["perl"]
pkgdesc = "Extended attribute support library for ACL support"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://savannah.nongnu.org/projects/attr"
source = f"$(NONGNU_SITE)/attr/attr-{pkgver}.tar.gz"
sha256 = "39bf67452fa41d0948c2197601053f48b3d78a029389734332a6309a680c6c87"
options = ["bootstrap"]


@subpackage("attr-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/doc"])


@subpackage("attr-progs")
def _progs(self):
    return self.default_progs(extra=["usr/share"])

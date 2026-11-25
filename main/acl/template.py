pkgname = "acl"
pkgver = "2.4.0"
pkgrel = 0
build_style = "gnu_configure"
# cycle chimerautils -> acl -> automake -> chimerautils
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["attr-devel", "linux-headers"]
checkdepends = ["perl"]
pkgdesc = "Access Control List filesystem support"
license = "LGPL-2.1-or-later"
url = "https://savannah.nongnu.org/projects/acl"
source = f"$(NONGNU_SITE)/acl/acl-{pkgver}.tar.gz"
sha256 = "73c853c3d44e1f693e5a96a986f1bd19d3d0dac2c7d453e796177774bc4e5f6a"
# test suite makes assumptions about a GNU environment
options = ["bootstrap", "!check"]


@split("devel")
def _(self):
    self.depends += ["attr-devel"]

    return self.default_devel(man="5")


@split("progs")
def _(self):
    return self.default_progs(extra=["usr/share"])

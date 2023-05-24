pkgname = "sysfsutils"
pkgver = "2.1.0"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["pkgconf", "gmake"]
pkgdesc = "Utilities to deal with sysfs"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND LGPL-2.1-or-later"
url = "http://linux-diag.sourceforge.net/Sysfsutils.html"
source = f"$(SOURCEFORGE_SITE)/linux-diag/{pkgname}-{pkgver}.tar.gz"
sha256 = "e865de2c1f559fff0d3fc936e660c0efaf7afe662064f2fb97ccad1ec28d208a"


@subpackage("libsysfs")
def _libmagic(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()


@subpackage("sysfsutils-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []

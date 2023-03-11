pkgname = "libiscsi"
pkgver = "1.19.0"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["automake", "libtool", "gmake", "pkgconf"]
makedepends = ["linux-headers", "libgcrypt-devel"]
pkgdesc = "ISCSI client library and utilities"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later AND GPL-2.0-or-later"
url = "https://foo.software"
source = f"https://github.com/sahlberg/libiscsi/archive/{pkgver}.tar.gz"
sha256 = "c7848ac722c8361d5064654bc6e926c2be61ef11dd3875020a63931836d806df"
tool_flags = {'CFLAGS': ['-Wno-strict-prototypes']}

def pre_configure(self):
    self.do("./autogen.sh")

@subpackage("libiscsi-devel")
def _devel(self):
    return self.default_devel()

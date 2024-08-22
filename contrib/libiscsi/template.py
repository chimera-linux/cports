pkgname = "libiscsi"
pkgver = "1.20.0"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
make_dir = "."
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["linux-headers", "libgcrypt-devel"]
pkgdesc = "ISCSI client library and utilities"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later AND GPL-2.0-or-later"
url = "https://foo.software"
source = f"https://github.com/sahlberg/libiscsi/archive/{pkgver}.tar.gz"
sha256 = "6321d802103f2a363d3afd9a5ae772de0b4052c84fe6a301ecb576b34e853caa"
tool_flags = {"CFLAGS": ["-Wno-strict-prototypes"]}


@subpackage("libiscsi-devel")
def _(self):
    return self.default_devel()

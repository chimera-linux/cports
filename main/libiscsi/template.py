pkgname = "libiscsi"
pkgver = "1.20.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-werror"]
configure_gen = ["./autogen.sh"]
make_dir = "."
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["linux-headers", "libgcrypt-devel"]
pkgdesc = "ISCSI client library and utilities"
license = "LGPL-2.1-or-later AND GPL-2.0-or-later"
url = "https://github.com/sahlberg/libiscsi"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "2b2a773ea0d3a708c1cafe61bbee780325fb1aafec6477f17d3f403e8732c9bf"
tool_flags = {"CFLAGS": ["-Wno-strict-prototypes"]}


@subpackage("libiscsi-devel")
def _(self):
    return self.default_devel()

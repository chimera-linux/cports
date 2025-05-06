pkgname = "libiscsi"
pkgver = "1.20.1"
pkgrel = 1
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
sha256 = "6bd6feef2904de1bb1869cec935b58995bc1311cad57184a2221e09ed6137eec"
tool_flags = {"CFLAGS": ["-Wno-strict-prototypes"]}


@subpackage("libiscsi-devel")
def _(self):
    return self.default_devel()

pkgname = "neon"
pkgver = "0.32.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-expat",
    "--with-ssl",
    "--with-ca-bundle=/etc/ssl/certs/ca-certificates.crt",
    "--without-gssapi",
    "--enable-shared",
    "--enable-threadsafe-ssl=posix",
    "--disable-static",
    "--disable-nls",
]
configure_gen = []
make_cmd = "gmake"
make_dir = "."
make_check_args = ["-j1"]
hostmakedepends = ["pkgconf", "gmake", "xmlto", "perl"]
makedepends = [
    "openssl-devel",
    "libproxy-devel",
    "libexpat-devel",
    "zlib-devel",
]
depends = ["ca-certificates"]
pkgdesc = "HTTP and WebDAV client library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://notroj.github.io/neon"
source = f"{url}/{pkgname}-{pkgver}.tar.gz"
sha256 = "4872e12f802572dedd4b02f870065814b2d5141f7dbdaf708eedab826b51a58a"


@subpackage("neon-devel")
def _dev(self):
    return self.default_devel()

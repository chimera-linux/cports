pkgname = "neon"
pkgver = "0.33.0"
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
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
make_dir = "."
make_check_args = ["-j1"]
hostmakedepends = ["automake", "pkgconf", "libtool", "gmake", "xmlto", "perl"]
makedepends = [
    "openssl-devel",
    "libproxy-devel",
    "libexpat-devel",
    "zlib-ng-compat-devel",
]
depends = ["ca-certificates"]
pkgdesc = "HTTP and WebDAV client library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://notroj.github.io/neon"
source = f"{url}/{pkgname}-{pkgver}.tar.gz"
sha256 = "659a5cc9cea05e6e7864094f1e13a77abbbdbab452f04d751a8c16a9447cf4b8"


@subpackage("neon-devel")
def _devel(self):
    return self.default_devel()

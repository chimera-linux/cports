pkgname = "curl"
pkgver = "7.79.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-threaded-resolver",
    "--enable-ipv6",
    "--with-libssh2",
    "--with-ssl",
    "--with-zstd",
    "--with-ca-bundle=/etc/ssl/certs/ca-certificates.crt",
    "ac_cv_path_NROFF=/usr/bin/mandoc",
    "ac_cv_sizeof_off_t=8",
]
make_check_env = {"USER": "nobody"}
hostmakedepends = ["pkgconf", "perl", "mandoc"]
makedepends = [
    "nghttp2-devel", "zlib-devel", "libzstd-devel",
    "openssl-devel", "libssh2-devel"
]
checkdepends = ["python", "nghttp2"]
depends = ["ca-certificates"]
pkgdesc = "Command line tool for transferring data with URL syntax"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://curl.haxx.se"
source = f"{url}/download/{pkgname}-{pkgver}.tar.bz2"
sha256 = "de62c4ab9a9316393962e8b94777a570bb9f71feb580fb4475e412f2f9387851"
# missing some checkdepends
options = ["!check", "!cross"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libcurl")
def _libcurl(self):
    self.pkgdesc = "Multiprotocol file transfer library"

    return self.default_libs()

@subpackage("libcurl-devel")
def _devel(self):
    self.depends += makedepends
    self.pkgdesc = "Multiprotocol file transfer library (development files)"

    return self.default_devel(man = True)

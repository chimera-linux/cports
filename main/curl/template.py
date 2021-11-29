pkgname = "curl"
pkgver = "7.80.0"
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
sha256 = "dd0d150e49cd950aff35e16b628edf04927f0289df42883750cf952bb858189c"
# missing some checkdepends
options = ["!check", "!cross"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libcurl")
def _libcurl(self):
    self.pkgdesc = "Multiprotocol file transfer library"

    return self.default_libs()

@subpackage("libcurl-static")
def _static(self):
    self.pkgdesc = "Multiprotocol file transfer library (static)"
    return self.default_static()

@subpackage("libcurl-devel")
def _devel(self):
    self.depends += makedepends
    self.pkgdesc = "Multiprotocol file transfer library (development files)"

    return self.default_devel(man = True)

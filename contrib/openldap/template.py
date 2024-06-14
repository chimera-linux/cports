pkgname = "openldap"
pkgver = "2.6.8"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-debug",
    "--disable-slapd",
    "--disable-sql",
    "--disable-static",
    "--disable-versioning",
    "--disable-wt",
    "--enable-backends=mod",
    "--enable-crypt",
    "--enable-dynamic",
    "--enable-modules",
    "--enable-overlays=mod",
    "--enable-rlookups",
    "--enable-spasswd",
    "--enable-syslog",
    "--with-cyrus-sasl",
    "--with-tls=openssl",
]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gmake",
    "libtool",
    "mandoc",
    "pkgconf",
]
makedepends = [
    "libevent-devel",
    "libltdl-devel",
    "libsasl-devel",
    "libsodium-devel",
    "openssl-devel",
]
pkgdesc = "FOSS implementation of the Lightweight Directory Access Protocol"
maintainer = "Renato Botelho do Couto <renato@netgate.com>"
license = "OLDAP-2.8"
url = "https://www.openldap.org"
source = (
    f"{url}/software/download/OpenLDAP/openldap-release/{pkgname}-{pkgver}.tgz"
)
sha256 = "48969323e94e3be3b03c6a132942dcba7ef8d545f2ad35401709019f696c3c4e"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("openldap-libs")
def _lib(self):
    return self.default_libs()


@subpackage("openldap-devel")
def _devel(self):
    return self.default_devel()

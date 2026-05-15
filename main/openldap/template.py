pkgname = "openldap"
pkgver = "2.6.13"
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
hostmakedepends = [
    "automake",
    "libtool",
    "mandoc",
    "pkgconf",
]
makedepends = [
    "libevent-devel",
    "libsasl-devel",
    "libsodium-devel",
    "libtool-devel",
    "openssl3-devel",
]
pkgdesc = "FOSS implementation of the Lightweight Directory Access Protocol"
license = "OLDAP-2.8"
url = "https://www.openldap.org"
source = (
    f"{url}/software/download/OpenLDAP/openldap-release/openldap-{pkgver}.tgz"
)
sha256 = "d693b49517a42efb85a1a364a310aed16a53d428d1b46c0d31ef3fba78fcb656"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("openldap-libs")
def _(self):
    return self.default_libs()


@subpackage("openldap-devel")
def _(self):
    self.depends += ["libsasl-devel"]
    return self.default_devel()

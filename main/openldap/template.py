# TODO: slapd service
pkgname = "openldap"
pkgver = "2.6.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-slapd", "--enable-syslog", "--enable-crypt",
    "--enable-dynamic", "--enable-spasswd", "--enable-rlookups",
    "--enable-modules", "--enable-backends=mod", "--enable-overlays=mod",
    "--disable-sql", "--disable-wt", "--disable-static", "--disable-debug",
    "--disable-versioning", "--with-tls=openssl", "--with-cyrus-sasl",
]
make_cmd = "gmake"
hostmakedepends = [
    "gmake", "pkgconf", "automake", "libtool", "groff",
]
makedepends = [
    "openssl-devel", "libsasl-devel", "libltdl-devel", "libevent-devel",
    "libsodium-devel",
]
depends = [f"openldap-progs={pkgver}-r{pkgrel}"]
pkgdesc = "FOSS implementation of the Lightweight Directory Access Protocol"
maintainer = "q66 <q66@chimera-linux.org>"
license = "OLDAP-2.0"
url = "https://www.openldap.org"
source = f"{url}/software/download/OpenLDAP/openldap-release/{pkgname}-{pkgver}.tgz"
sha256 = "d2a2a1d71df3d77396b1c16ad7502e674df446e06072b0e5a4e941c3d06c0d46"
file_modes = {
    "etc/openldap/slapd.conf": ("root", "ldap", 0o640),
    "etc/openldap/slapd.ldif": ("root", "ldap", 0o640),
    "etc/openldap/slapd.d": ("ldap", "ldap", 0o700),
    "var/lib/openldap": ("ldap", "ldap", 0o700),
}
# test suite takes ages
options = ["!cross", "!check"]

system_users = [
    {
        "name": "ldap",
        "id": 83,
        "home": "/var/lib/openldap",
    }
]

def pre_configure(self):
    self.do("autoreconf", "-if")

def post_install(self):
    self.install_dir("etc/openldap/slapd.d", mode = 0o700, empty = True)
    self.install_dir("var/lib/openldap", mode = 0o700, empty = True)
    self.install_license("LICENSE")

@subpackage("openldap-libs")
def _lib(self):
    return self.default_libs()

@subpackage("openldap-devel")
def _devel(self):
    return self.default_devel()

@subpackage("openldap-progs")
def _progs(self):
    return [
        "usr/bin/ldap*",
        "usr/share/man/man1/ldap*.1",
    ]

# FIXME visibility
hardening = ["!vis"]

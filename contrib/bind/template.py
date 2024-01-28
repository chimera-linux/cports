pkgname = "bind"
pkgver = "9.18.21"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "doxygen",
    "gmake",
    "libtool",
    "pkgconf",
    "python-sphinx",
    "xsltproc",
]
makedepends = [
    "cmocka-devel",
    "heimdal-devel",
    "libcap-devel",
    "libuv-devel",
    "libxml2-devel",
    "json-c-devel",
    "nghttp2-devel",
    "openssl-devel",
]
checkdepends = ["python-pytest", "python-dnspython"]
depends = ["bind-progs"]
pkgdesc = "ISC DNS server"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MPL-2.0"
url = "https://www.isc.org/bind"
source = f"https://downloads.isc.org/isc/bind9/{pkgver}/bind-{pkgver}.tar.xz"
sha256 = "a556be22505d9ea4f9c6717aee9c549739c68498aff3ca69035787ecc648fec5"


def post_install(self):
    self.install_service(self.files_path / "named")
    # get rid of hard links
    self.rm(self.destdir / "usr/bin/named-compilezone")
    self.rm(self.destdir / "usr/bin/ddns-confgen")
    self.install_link("named-checkzone", "usr/bin/named-compilezone")
    self.install_link("tsig-keygen", "usr/bin/ddns-confgen")


@subpackage("bind-devel")
def _devel(self):
    return self.default_devel()


@subpackage("bind-progs")
def _progs(self):
    def func():
        for prog in [
            "arpaname",
            "delv",
            "dig",
            "dnssec-cds",
            "dnssec-dsfromkey",
            "dnssec-importkey",
            "dnssec-keyfromlabel",
            "dnssec-keygen",
            "dnssec-revoke",
            "dnssec-settime",
            "dnssec-signzone",
            "dnssec-verify",
            "host",
            "mdig",
            "named-checkconf",
            "named-checkzone",
            "named-compilezone",
            "named-journalprint",
            "named-rrchecker",
            "nsec3hash",
            "nslookup",
            "nsupdate",
        ]:
            self.take(f"usr/bin/{prog}")
            self.take(f"usr/share/man/man1/{prog}.1")

    return func

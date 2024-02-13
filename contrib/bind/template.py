pkgname = "bind"
pkgver = "9.18.24"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
# FIXME: in tests/isc netmgr_test can fail in either tls_noresponse or one other
# CI=1 skips 'long' tests
make_check_env = {"CI": "1"}
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
depends = [f"bind-progs={pkgver}-r{pkgrel}"]
pkgdesc = "ISC DNS server"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MPL-2.0"
url = "https://www.isc.org/bind"
source = f"https://downloads.isc.org/isc/bind9/{pkgver}/bind-{pkgver}.tar.xz"
sha256 = "709d73023c9115ddad3bab65b6c8c79a590196d0d114f5d0ca2533dbd52ddf66"


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
    # "cli" utilities that can be used standalone,
    # the rest of the progs are for running bind itself
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

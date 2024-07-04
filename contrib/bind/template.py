pkgname = "bind"
pkgver = "9.18.27"
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
sha256 = "ea3f3d8cfa2f6ae78c8722751d008f54bc17a3aed2be3f7399eb7bf5f4cda8f1"


def post_install(self):
    self.install_service(self.files_path / "named")
    # get rid of hard links
    self.uninstall("usr/bin/named-compilezone")
    self.uninstall("usr/bin/ddns-confgen")
    self.install_link("usr/bin/named-compilezone", "named-checkzone")
    self.install_link("usr/bin/ddns-confgen", "tsig-keygen")


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

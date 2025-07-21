pkgname = "bind"
pkgver = "9.20.11"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-libidn2"]
make_dir = "."
# FIXME: in tests/isc netmgr_test can fail in either tls_noresponse or one other
# CI=1 skips 'long' tests
make_check_env = {"CI": "1"}
hostmakedepends = [
    "automake",
    "doxygen",
    "libtool",
    "libxslt-progs",
    "pkgconf",
    "python-sphinx",
]
makedepends = [
    "cmocka-devel",
    "heimdal-devel",
    "jemalloc-devel",
    "json-c-devel",
    "libcap-devel",
    "libidn2-devel",
    "libuv-devel",
    "libxml2-devel",
    "lmdb-devel",
    "nghttp2-devel",
    "openssl3-devel",
    "userspace-rcu-devel",
]
checkdepends = ["python-pytest", "python-dnspython"]
depends = [self.with_pkgver("bind-progs")]
pkgdesc = "ISC DNS server"
license = "MPL-2.0"
url = "https://www.isc.org/bind"
source = f"https://downloads.isc.org/isc/bind9/{pkgver}/bind-{pkgver}.tar.xz"
sha256 = "4da2d532e668bc21e883f6e6d9d3d81794d9ec60b181530385649a56f46ee17a"
# lto: some udp tests fail otherwise
options = ["!lto"]

if self.profile().arch in ["loongarch64"]:
    # rwlock test timeout, otherwise good
    options += ["!check"]


def post_install(self):
    self.install_service(self.files_path / "named")
    # get rid of hard links
    self.uninstall("usr/bin/named-compilezone")
    self.uninstall("usr/bin/ddns-confgen")
    self.install_link("usr/bin/named-compilezone", "named-checkzone")
    self.install_link("usr/bin/ddns-confgen", "tsig-keygen")


@subpackage("bind-devel")
def _(self):
    return self.default_devel()


@subpackage("bind-libs")
def _(self):
    # bind has libfoo.so as the symlink,
    # and libfoo-version.so as the main lib
    return ["usr/lib/lib*-*.so"]


@subpackage("bind-progs")
def _(self):
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
            "dnssec-ksr",
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
            "named-nzd2nzf",
            "named-rrchecker",
            "nsec3hash",
            "nslookup",
            "nsupdate",
        ]:
            self.take(f"cmd:{prog}")

    return func

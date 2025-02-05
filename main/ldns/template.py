pkgname = "ldns"
pkgver = "1.8.4"
pkgrel = 3
build_style = "gnu_configure"
configure_args = [
    "--with-drill",
    "--with-examples",
    "--disable-dane-ta-usage",
    "--with-trust-anchor=/usr/share/dns/root.key",
]
hostmakedepends = [
    "automake",
    "dns-root-data",
    "perl",
    "pkgconf",
    "slibtool",
]
makedepends = ["libpcap-devel", "openssl3-devel", "dns-root-data"]
pkgdesc = "Modern DNS/DNSSEC library"
subdesc = "utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://www.nlnetlabs.nl/projects/ldns"
source = f"http://www.nlnetlabs.nl/downloads/ldns/ldns-{pkgver}.tar.gz"
sha256 = "838b907594baaff1cd767e95466a7745998ae64bc74be038dccc62e2de2e4247"
# no check target
options = ["!check"]


def init_configure(self):
    self.configure_args += [f"--with-ssl={self.profile().sysroot / 'usr'}"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("ldns-libs")
def _(self):
    self.depends = ["dns-root-data"]
    # transitional
    self.provides = [self.with_pkgver("libldns")]

    return self.default_libs()


@subpackage("ldns-devel")
def _(self):
    self.depends += ["openssl3-devel"]
    # transitional
    self.provides = [self.with_pkgver("libldns-devel")]

    return self.default_devel()

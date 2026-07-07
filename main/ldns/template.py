pkgname = "ldns"
pkgver = "1.9.2"
pkgrel = 0
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
license = "BSD-3-Clause"
url = "http://www.nlnetlabs.nl/projects/ldns"
source = f"http://www.nlnetlabs.nl/downloads/ldns/ldns-{pkgver}.tar.gz"
sha256 = "b524fa21994b6e834200ceb8c27f1b84bda5982fe35706f058196c079db94d5d"
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

pkgname = "ldns"
pkgver = "1.7.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-drill", "--with-examples", "--disable-dane-ta-usage",
    "--with-trust-anchor=/etc/dns/root.key"
]
# custom rules don't like out-of-tree build
make_dir = "."
hostmakedepends = ["pkgconf", "perl", "dnssec-anchors"]
makedepends = ["libpcap-devel", "openssl-devel", "dnssec-anchors"]
pkgdesc = "Modern DNS/DNSSEC library - utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://www.nlnetlabs.nl/projects/ldns"
source = f"http://www.nlnetlabs.nl/downloads/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "8ac84c16bdca60e710eea75782356f3ac3b55680d40e1530d7cea474ac208229"
# no check target
options = ["!check"]

def init_configure(self):
    self.configure_args += [
        "--with-ssl=" + str(self.profile().sysroot / "usr")
    ]

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libldns")
def _lib(self):
    self.depends = ["dnssec-anchors"]
    self.pkgdesc = "Modern DNS/DNSSEC library"

    return self.default_libs()

@subpackage("libldns-devel")
def _devel(self):
    self.depends += ["openssl-devel"]
    self.pkgdesc = "Modern DNS/DNSSEC library (development files)"

    return self.default_devel()

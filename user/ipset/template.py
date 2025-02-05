pkgname = "ipset"
pkgver = "7.23"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-kmod=no"]
make_dir = "."
make_check_target = "tests"
hostmakedepends = [
    "automake",
    "libtool-devel",
    "libtool",
    "pkgconf",
]
makedepends = [
    "libmnl-devel",
    "linux-headers",
]
checkdepends = ["bash", "iptables"]
pkgdesc = "Manage Linux IP sets"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://ipset.netfilter.org"
source = f"{url}/ipset-{pkgver}.tar.bz2"
sha256 = "db3a51a9ebf27c7cbd0a1482c46c5e0ed630c28c796f73287c4b339dd46086e5"
# requires modifying actual ipsets for tests
options = ["linkundefver", "!check"]


@subpackage("ipset-devel")
def _(self):
    return self.default_devel()

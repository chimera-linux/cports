pkgname = "ipset"
pkgver = "7.24"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-kmod=no"]
make_dir = "."
make_check_target = "tests"
hostmakedepends = [
    "automake",
    "libtool",
    "libtool-devel",
    "pkgconf",
]
makedepends = [
    "libmnl-devel",
    "linux-headers",
]
checkdepends = ["bash", "iptables"]
pkgdesc = "Manage Linux IP sets"
license = "GPL-2.0-only"
url = "https://ipset.netfilter.org"
source = f"{url}/ipset-{pkgver}.tar.bz2"
sha256 = "fbe3424dff222c1cb5e5c34d38b64524b2217ce80226c14fdcbb13b29ea36112"
# requires modifying actual ipsets for tests
options = ["linkundefver", "!check"]


@subpackage("ipset-devel")
def _(self):
    return self.default_devel()

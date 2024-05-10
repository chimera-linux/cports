pkgname = "ipset"
pkgver = "7.21"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-kmod=no"]
make_cmd = "gmake"
make_dir = "."
make_check_target = "tests"
hostmakedepends = [
    "automake",
    "gmake",
    "libltdl-devel",
    "libtool",
    "pkgconf",
]
makedepends = [
    "libmnl-devel",
    "linux-headers",
]
checkdepends = ["bash", "iptables"]
pkgdesc = "Manage Linux IP sets"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-only"
url = "https://ipset.netfilter.org"
source = f"{url}/ipset-{pkgver}.tar.bz2"
sha256 = "e2c6ce4fcf3acb3893ca5d35c86935f80ad76fc5ccae601185842df760e0bc69"
# requires modifying actual ipsets for tests
options = ["linkundefver", "!check"]


@subpackage("ipset-devel")
def _devel(self):
    return self.default_devel()

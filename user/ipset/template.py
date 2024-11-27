pkgname = "ipset"
pkgver = "7.22"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-kmod=no"]
make_dir = "."
make_check_target = "tests"
hostmakedepends = [
    "automake",
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://ipset.netfilter.org"
source = f"{url}/ipset-{pkgver}.tar.bz2"
sha256 = "f6ac5a47c3ef9f4c67fcbdf55e791cbfe38eb0a4aa1baacd12646a140abacdd9"
# requires modifying actual ipsets for tests
options = ["linkundefver", "!check"]


@subpackage("ipset-devel")
def _(self):
    return self.default_devel()

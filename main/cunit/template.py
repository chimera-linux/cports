pkgname = "cunit"
pkgver = "2.1.3"
pkgrel = 0
_pkgver = f"{pkgver[: pkgver.rfind('.')]}-{pkgver[-1]}"
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "bash",
    "libtool",
    "pkgconf",
]
pkgdesc = "Automated C testing framework"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://cunit.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/cunit/CUnit/{_pkgver}/CUnit-{_pkgver}.tar.bz2"
sha256 = "f5b29137f845bb08b77ec60584fdb728b4e58f1023e6f249a464efa49a40f214"


def post_extract(self):
    # the configure fails since this is there already
    (self.cwd / "config.status").unlink()


@subpackage("cunit-devel")
def _(self):
    return self.default_devel()

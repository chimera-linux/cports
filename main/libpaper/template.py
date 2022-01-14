pkgname = "libpaper"
pkgver = "1.1.28"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool", "gettext-tiny"]
pkgdesc = "Library for handling paper characteristics"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://packages.debian.org/unstable/source/libpaper"
source = f"$(DEBIAN_SITE)/main/libp/{pkgname}/{pkgname}_{pkgver}.tar.gz"
sha256 = "c8bb946ec93d3c2c72bbb1d7257e90172a22a44a07a07fb6b802a5bb2c95fddc"

def pre_configure(self):
    self.do("autoreconf", "-if")

def post_install(self):
    self.install_dir("etc/libpaper.d", empty = True)
    # systemwide default papersize
    with (self.destdir / "etc/papersize").open("w") as ps:
        ps.write("# Write the paper size here, see papersize(5)")
    # localization
    for f in (self.cwd / "debian/po").glob("*.po"):
        loc = f"usr/share/locale/{f.stem}/LC_MESSAGES"
        self.install_dir(loc)
        self.do(
            "msgfmt", "-o", self.chroot_destdir / loc / "libpaper.mo",
            self.chroot_cwd / "debian/po" / f.name
        )

@subpackage("libpaper-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libpaper-progs")
def _progs(self):
    return self.default_progs()

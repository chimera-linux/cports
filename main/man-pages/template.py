pkgname = "man-pages"
pkgver = "5.13"
pkgrel = 0
make_cmd = "gmake"
hostmakedepends = ["gmake"]
pkgdesc = "Linux Documentation Project manual pages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://man7.org/linux/man-pages/index.html"
source = f"$(KERNEL_SITE)/docs/man-pages/{pkgname}-{pkgver}.tar.xz"
sha256 = "614dae3efe7dfd480986763a2a2a8179215032a5a4526c0be5e899a25f096b8b"

def do_install(self):
    from cbuild.util import make

    make.Make(self).invoke("all", [
        "VERBOSE=1", f"prefix={self.chroot_destdir}/usr"
    ])

    # remove duplicate manpages
    with self.pushd(self.destdir / "usr/share/man"):
        self.rm("man1/iconv.1")
        self.rm("man1/getent.1")
        self.rm("man1/ldd.1")
        self.rm("man3/err.3")
        self.rm("man3/getspnam.3")
        self.rm("man3/rand.3")
        self.rm("man5/passwd.5")
        self.rm("man5/tzfile.5")
        self.rm("man7/man.7")
        self.rm("man7/symlink.7")
        self.rm("man8/tzselect.8")
        self.rm("man8/zdump.8")
        self.rm("man8/zic.8")

@subpackage("man-pages-devel")
def _devel(self):
    self.pkgdesc = f"{pkgdesc} (development pages)"
    return ["usr/share/man/man[23]"]

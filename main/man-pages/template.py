pkgname = "man-pages"
pkgver = "6.04"
pkgrel = 0
make_cmd = "gmake"
hostmakedepends = ["gmake", "bash"]
pkgdesc = "Linux Documentation Project manual pages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://man7.org/linux/man-pages/index.html"
source = f"$(KERNEL_SITE)/docs/man-pages/{pkgname}-{pkgver}.tar.xz"
sha256 = "c2c0b9329955df81af45ee80ebc84c47291f95df5157db1fab988199f9371af1"
options = ["!autosplit"]


def do_install(self):
    from cbuild.util import make

    make.Make(self).invoke(
        "install", ["VERBOSE=1", f"prefix={self.chroot_destdir}/usr"]
    )

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
    self.options = ["!autosplit"]

    return ["usr/share/man/man[23]"]

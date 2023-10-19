pkgname = "man-pages"
pkgver = "6.05.01"
pkgrel = 2
hostmakedepends = ["gmake", "bash"]
pkgdesc = "Linux Documentation Project manual pages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://man7.org/linux/man-pages/index.html"
source = f"$(KERNEL_SITE)/docs/man-pages/{pkgname}-{pkgver}.tar.xz"
sha256 = "b96ab6b44a688c91d1b572e52fece519e1cfd2bb4c33fe7014fc3fd1ef3f9cae"
options = ["!autosplit"]


def do_install(self):
    self.do(
        "gmake",
        "install",
        "VERBOSE=1",
        f"prefix={self.chroot_destdir}/usr",
    )

    # remove duplicate manpages
    with self.pushd(self.destdir / "usr/share/man"):
        self.rm("man1/time.1")
        self.rm("man1/getent.1")
        self.rm("man3/getspnam.3")
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

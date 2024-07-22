pkgname = "man-pages"
pkgver = "6.9.1"
pkgrel = 1
hostmakedepends = ["gmake", "gsed", "bash"]
pkgdesc = "Linux Documentation Project manual pages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://man7.org/linux/man-pages/index.html"
source = f"$(KERNEL_SITE)/docs/man-pages/man-pages-{pkgver}.tar.xz"
sha256 = "e23cbac29f110ba571f0da8523e79d373691466ed7f2a31301721817d34530bd"
options = ["!autosplit"]


def do_install(self):
    self.do(
        "gmake",
        "install",
        "SED=gsed",
        "VERBOSE=1",
        "LINK_PAGES=symlink",
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

    # dead links due to getspnam.3 (provided by shadow)
    with self.pushd(self.destdir / "usr/share/man/man3"):
        self.rm("endspent.3")
        self.rm("fgetspent.3")
        self.rm("fgetspent_r.3")
        self.rm("getspent.3")
        self.rm("getspent_r.3")
        self.rm("getspnam_r.3")
        self.rm("lckpwdf.3")
        self.rm("putspent.3")
        self.rm("setspent.3")
        self.rm("sgetspent.3")
        self.rm("sgetspent_r.3")
        self.rm("ulckpwdf.3")


@subpackage("man-pages-devel")
def _devel(self):
    self.subdesc = "development pages"
    self.options = ["!autosplit"]

    return [
        "usr/share/man/man[23]*",
        "usr/share/man/man4/*ioctl*",
        "usr/share/man/man7/sigevent.7",
    ]

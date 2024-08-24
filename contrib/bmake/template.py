pkgname = "bmake"
pkgver = "20240808"
pkgrel = 1
pkgdesc = "Portable version of NetBSD make"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.crufty.net/help/sjg/bmake.html"
source = f"https://www.crufty.net/ftp/pub/sjg/bmake-{pkgver}.tar.gz"
sha256 = "b59189251b483decd4492f1f74387b2a584c03d5aa4637cd48b38ec62b9c0848"
hardening = ["vis", "cfi"]


if self.profile().cross:
    hostmakedepends = ["bmake"]


def do_build(self):
    self.mkdir("build", parents=True)
    eargs = []
    if self.profile().cross:
        eargs = ["--host=" + self.profile().triplet]
    self.do(
        self.chroot_cwd / "boot-strap",
        *eargs,
        "--prefix=/usr",
        "op=build",
        wrksrc="build",
    )


def do_install(self):
    eargs = []
    if self.profile().cross:
        eargs = ["BMAKE=bmake"]
    self.do(
        self.chroot_cwd / "boot-strap",
        "--prefix=/usr",
        "--install-destdir=" + str(self.chroot_destdir),
        "op=install",
        *eargs,
        wrksrc="build",
    )
    self.uninstall("usr/share/man")
    self.install_man("bmake.1")
    self.install_license("LICENSE")


def do_check(self):
    self.do(
        self.chroot_cwd / "boot-strap",
        "--prefix=/usr",
        "op=test",
        wrksrc="build",
    )

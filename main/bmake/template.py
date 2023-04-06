pkgname = "bmake"
pkgver = "20230321"
pkgrel = 0
pkgdesc = "Portable version of NetBSD make"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://www.crufty.net/help/sjg/bmake.html"
source = f"http://www.crufty.net/ftp/pub/sjg/bmake-{pkgver}.tar.gz"
sha256 = "ed7d568c08748a2221e19ddc1aebed97dd430ab0c6942304698b1c2363fa8256"
# FIXME failed test
hardening = ["vis", "cfi", "!int"]
options = ["bootstrap"]

def do_build(self):
    self.mkdir("build", parents = True)
    eargs = []
    if self.profile().cross:
        eargs = ["--host=" + self.profile().triplet]
    self.do(
        self.chroot_cwd / "boot-strap", *eargs, "--prefix=/usr", "op=build",
        wrksrc = "build"
    )

def do_install(self):
    eargs = []
    if self.profile().cross:
        eargs = ["BMAKE=make"]
    self.do(
        self.chroot_cwd / "boot-strap", "--prefix=/usr",
        "--install-destdir=" + str(self.chroot_destdir), "op=install", *eargs,
        wrksrc = "build"
    )
    self.rm(self.destdir / "usr/share/man", recursive = True)
    self.install_man("bmake.1")
    self.install_man("make.1")
    self.install_license("LICENSE")
    self.install_link("bmake", "usr/bin/make")

def do_check(self):
    self.do(
        self.chroot_cwd / "boot-strap", "--prefix=/usr", "op=test",
        wrksrc = "build"
    )

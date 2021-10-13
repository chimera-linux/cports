pkgname = "bmake"
pkgver = "20211001"
pkgrel = 0
pkgdesc = "Portable version of NetBSD make"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://www.crufty.net/help/sjg/bmake.html"
source = f"http://www.crufty.net/ftp/pub/sjg/bmake-{pkgver}.tar.gz"
sha256 = "cad7ef0fb41138050f8932af3a7ade16f7265b3f37ff6356703e0b1ad6542739"
options = ["bootstrap"]

def do_build(self):
    self.mkdir("build", parents = True)
    eargs = []
    if self.cross_build:
        eargs = ["--host=" + self.build_profile.short_triplet]
    self.do(
        self.chroot_cwd / "boot-strap",
        eargs + ["--prefix=/usr", "op=build"],
        wrksrc = "build"
    )

def do_install(self):
    eargs = []
    if self.cross_build:
        eargs = ["BMAKE=make"]
    self.do(
        self.chroot_cwd / "boot-strap", [
            "--prefix=/usr", "--install-destdir=" + str(self.chroot_destdir),
            "op=install"
        ] + eargs,
        wrksrc = "build"
    )
    self.rm(self.destdir / "usr/share/man", recursive = True)
    self.install_man("bmake.1")
    self.install_man("make.1")
    self.install_license("LICENSE")
    self.install_link("bmake", "usr/bin/make")

def do_check(self):
    self.do(
        self.chroot_cwd / "boot-strap",
        ["--prefix=/usr", "op=test"],
        wrksrc = "build"
    )

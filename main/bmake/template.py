pkgname = "bmake"
pkgver = "20240212"
pkgrel = 0
pkgdesc = "Portable version of NetBSD make"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.crufty.net/help/sjg/bmake.html"
source = f"https://www.crufty.net/ftp/pub/sjg/bmake-{pkgver}.tar.gz"
sha256 = "971d5a364035349e984d82c2a48d546a0c73e52f3b8f2aa29a3be3d2408ffaa8"
hardening = ["vis", "cfi"]
options = ["bootstrap"]


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
        eargs = ["BMAKE=make"]
    self.do(
        self.chroot_cwd / "boot-strap",
        "--prefix=/usr",
        "--install-destdir=" + str(self.chroot_destdir),
        "op=install",
        *eargs,
        wrksrc="build",
    )
    self.rm(self.destdir / "usr/share/man", recursive=True)
    self.install_man("bmake.1")
    self.install_man("make.1")
    self.install_license("LICENSE")
    self.install_link("bmake", "usr/bin/make")


def do_check(self):
    self.do(
        self.chroot_cwd / "boot-strap",
        "--prefix=/usr",
        "op=test",
        wrksrc="build",
    )

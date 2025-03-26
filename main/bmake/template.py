pkgname = "bmake"
pkgver = "20250308"
pkgrel = 0
pkgdesc = "Portable version of NetBSD make"
license = "BSD-3-Clause"
url = "https://www.crufty.net/help/sjg/bmake.html"
source = f"https://www.crufty.net/ftp/pub/sjg/bmake-{pkgver}.tar.gz"
sha256 = "2388d9fb186576633aa725ff163552a5dba7a6a375a8cb9a9014ab57ee7d99a2"
hardening = ["vis", "cfi"]


if self.profile().cross:
    hostmakedepends = ["bmake"]


def build(self):
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


def install(self):
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


def check(self):
    self.do(
        self.chroot_cwd / "boot-strap",
        "--prefix=/usr",
        "op=test",
        wrksrc="build",
    )

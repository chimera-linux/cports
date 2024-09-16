pkgname = "bmake"
pkgver = "20240909"
pkgrel = 0
pkgdesc = "Portable version of NetBSD make"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.crufty.net/help/sjg/bmake.html"
source = f"https://www.crufty.net/ftp/pub/sjg/bmake-{pkgver}.tar.gz"
sha256 = "d4e019e26c64cc8ffcf1cae9bb04fbb13da8fa6f41fb30fd26e221f655d4e84d"
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

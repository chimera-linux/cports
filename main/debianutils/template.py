pkgname = "debianutils"
pkgver = "5.22"
pkgrel = 0
pkgdesc = "Miscellaneous utilities from Debian"
license = "GPL-2.0-or-later"
url = "https://tracker.debian.org/pkg/debianutils"
source = f"$(DEBIAN_SITE)/main/d/debianutils/debianutils_{pkgver}.tar.xz"
sha256 = "043569241cdd893cc45e00f917c94c123d0c24143895d91c4d08c6c567e35155"
compression = "deflate"
hardening = ["vis", "cfi"]
options = ["bootstrap"]


def build(self):
    from cbuild.util import compiler

    cfl = [
        "-DHAVE_GETOPT_H",
        f'-DPACKAGE_VERSION="{pkgver}"',
        "-Wall",
        "-Wextra",
    ]

    cc = compiler.C(self)
    cc.invoke(["ischroot.c"], "ischroot", flags=cfl)
    cc.invoke(["run-parts.c"], "run-parts", flags=cfl)


def install(self):
    self.install_bin("ischroot")
    self.install_man("ischroot.1")
    self.install_bin("run-parts")
    self.install_man("run-parts.8")
    self.install_bin("savelog")
    self.install_man("savelog.8")

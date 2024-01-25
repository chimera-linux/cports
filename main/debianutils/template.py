pkgname = "debianutils"
pkgver = "5.16"
pkgrel = 0
pkgdesc = "Miscellaneous utilities from Debian"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://tracker.debian.org/pkg/debianutils"
source = f"$(DEBIAN_SITE)/main/d/debianutils/debianutils_{pkgver}.tar.xz"
sha256 = "eeb069c2639906f4181214dd1c4e448bc825229b0250ebf66f69c7344e8aa1e0"
hardening = ["vis", "cfi"]


def do_build(self):
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


def do_install(self):
    self.install_bin("ischroot")
    self.install_man("ischroot.1")
    self.install_bin("run-parts")
    self.install_man("run-parts.8")
    self.install_bin("savelog")
    self.install_man("savelog.8")

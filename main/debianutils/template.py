pkgname = "debianutils"
pkgver = "5.7"
pkgrel = 0
build_style = "gnu_configure"
pkgdesc = "Miscellaneous utilities from Debian"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://tracker.debian.org/pkg/debianutils"
source = f"$(DEBIAN_SITE)/main/d/debianutils/debianutils_{pkgver}.orig.tar.gz"
sha256 = "27ec9e0e7e44dc8ab611aa576330471bacb07e4491ffecf0d3aa6909c92f9022"
hardening = ["vis", "cfi"]


def post_install(self):
    # (add|remove)-shell conflicts with our system
    # installkernel is not something we want either
    # which is provided by chimerautils
    self.rm(self.destdir / "usr/bin/add-shell")
    self.rm(self.destdir / "usr/bin/remove-shell")
    self.rm(self.destdir / "usr/bin/update-shells")
    self.rm(self.destdir / "usr/bin/installkernel")
    self.rm(self.destdir / "usr/bin/which")
    self.rm(self.destdir / "usr/bin/tempfile")
    for f in (self.destdir / "usr/share/man").rglob("*.[18]"):
        match f.name:
            case "add-shell.8" | "remove-shell.8" | "update-shells.8" | "installkernel.8" | "which.1" | "tempfile.1":
                f.unlink()


configure_gen = []

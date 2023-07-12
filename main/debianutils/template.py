pkgname = "debianutils"
pkgver = "5.8"
pkgrel = 0
build_style = "gnu_configure"
pkgdesc = "Miscellaneous utilities from Debian"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://tracker.debian.org/pkg/debianutils"
source = f"$(DEBIAN_SITE)/main/d/debianutils/debianutils_{pkgver}.orig.tar.gz"
sha256 = "5b086d27eb9063de4d746760d0faeb40d9464fb855fc8a8e7fb93b03efcec622"
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

pkgname = "debianutils"
pkgver = "4.11.2"
pkgrel = 0
build_style = "gnu_configure"
pkgdesc = "Miscellaneous utilities from Debian"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://tracker.debian.org/pkg/debianutils"
source = f"$(DEBIAN_SITE)/main/d/debianutils/debianutils_{pkgver}.tar.xz"
sha256 = "3b680e81709b740387335fac8f8806d71611dcf60874e1a792e862e48a1650de"

def post_install(self):
    # (add|remove)-shell conflicts with our system
    # installkernel is not something we want either
    # which is provided by bsdutils
    self.rm(self.destdir / "usr/bin/add-shell")
    self.rm(self.destdir / "usr/bin/remove-shell")
    self.rm(self.destdir / "usr/bin/installkernel")
    self.rm(self.destdir / "usr/bin/which")
    for f in (self.destdir / "usr/share/man").rglob("*.[18]"):
        match f.name:
            case "add-shell.8" | "remove-shell.8" | "installkernel.8" | \
                 "which.1":
                f.unlink()

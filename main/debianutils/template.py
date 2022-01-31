pkgname = "debianutils"
pkgver = "5.5"
pkgrel = 0
build_style = "gnu_configure"
pkgdesc = "Miscellaneous utilities from Debian"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://tracker.debian.org/pkg/debianutils"
source = f"$(DEBIAN_SITE)/main/d/debianutils/debianutils_{pkgver}.orig.tar.xz"
sha256 = "2b0fad5c00eb2b8461523b2950e6f06e6ddbb0ac3384c5a3377867d51098d102"

def post_install(self):
    # (add|remove)-shell conflicts with our system
    # installkernel is not something we want either
    # which is provided by bsdutils
    self.rm(self.destdir / "usr/bin/add-shell")
    self.rm(self.destdir / "usr/bin/remove-shell")
    self.rm(self.destdir / "usr/bin/update-shells")
    self.rm(self.destdir / "usr/bin/installkernel")
    self.rm(self.destdir / "usr/bin/which")
    for f in (self.destdir / "usr/share/man").rglob("*.[18]"):
        match f.name:
            case "add-shell.8" | "remove-shell.8" | "update-shells.8" | \
                 "installkernel.8" | "which.1":
                f.unlink()

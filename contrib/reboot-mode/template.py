pkgname = "reboot-mode"
pkgver = "1.0.0"
pkgrel = 0
build_style = "makefile"
make_build_target = pkgname
makedepends = ["linux-headers"]
pkgdesc = "Reboot a mobile device to a specific mode"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://gitlab.com/postmarketOS/reboot-mode"
source = f"{url}/-/archive/{pkgver}.tar.gz"
sha256 = "ed9f13dffe745a109970c12f48a7be3e1c1f7bdee35a0d242264df11f6a17a62"

def do_install(self):
    self.install_bin(pkgname)

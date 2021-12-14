pkgname = "xinit"
pkgver = "1.4.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-xinitdir=/etc/X11/xinit"]
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel"]
pkgdesc = "X init program"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "de9b8f617b68a70f6caf87da01fcf0ebd2b75690cdcba9c921d0ef54fa54abb9"

def post_install(self):
    self.install_license("COPYING")

    self.install_file(
        self.files_path / "xinitrc", "etc/skel", name = ".xinitrc"
    )
    self.install_file(
        self.files_path / "xsession", "etc/skel", name = ".xsession"
    )
    self.install_file(self.files_path / "xserverrc", "etc/X11/xinit")

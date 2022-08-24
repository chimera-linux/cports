pkgname = "xinit"
pkgver = "1.4.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-xinitdir=/etc/X11/xinit"]
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel"]
depends = ["cmd:mcookie!util-linux"]
pkgdesc = "X init program"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "de9b8f617b68a70f6caf87da01fcf0ebd2b75690cdcba9c921d0ef54fa54abb9"

def post_install(self):
    self.install_license("COPYING")

    # remove all the broken upstream junk
    # also TODO: write a manpage for new startx
    self.rm(self.destdir / "usr/bin/startx")
    self.rm(self.destdir / "usr/share/man/man1/startx.1")
    self.rm(self.destdir / "etc/X11/xinit", recursive = True)

    self.install_file(self.files_path / "startx", "usr/bin", mode = 0o755)
    self.install_file(self.files_path / "Xsession", "etc/X11", mode = 0o755)

    # default xsession scripts
    self.install_dir("etc/X11/Xsession.d")
    self.install_file(
        self.files_path / "00default", "etc/X11/Xsession.d", mode = 0o755
    )

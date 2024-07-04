pkgname = "xinit"
pkgver = "1.4.2"
pkgrel = 2
build_style = "gnu_configure"
configure_args = ["--with-xinitdir=/etc/X11/xinit"]
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel"]
depends = ["cmd:mcookie!chimerautils"]
pkgdesc = "X init program"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.gz"
sha256 = "9121c9162f6dedab1229a8c4ed4021c4d605699cb0da580ac2ee1b0c96b3f60e"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")

    # remove all the broken upstream junk
    # also TODO: write a manpage for new startx
    self.uninstall("usr/bin/startx")
    self.uninstall("usr/share/man/man1/startx.1")
    self.uninstall("etc/X11/xinit", recursive=True)

    self.install_file(self.files_path / "startx", "usr/bin", mode=0o755)
    self.install_file(self.files_path / "Xsession", "etc/X11", mode=0o755)

    # default xsession scripts
    self.install_dir("etc/X11/Xsession.d")
    self.install_file(
        self.files_path / "00default", "etc/X11/Xsession.d", mode=0o755
    )


configure_gen = []

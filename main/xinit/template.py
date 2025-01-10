pkgname = "xinit"
pkgver = "1.4.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-xinitdir=/etc/X11/xinit"]
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = ["libx11-devel"]
depends = ["cmd:mcookie!chimerautils"]
pkgdesc = "X init program"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xinit-{pkgver}.tar.gz"
sha256 = "9d876569b84ff384fa4c3e4354b1e1830f0517d504b7674b05ec9958a84b77f8"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")

    # remove all the broken upstream junk
    # also TODO: write a manpage for new startx
    self.uninstall("usr/bin/startx")
    self.uninstall("usr/share/man/man1/startx.1")
    self.uninstall("etc/X11/xinit")

    self.install_file(self.files_path / "startx", "usr/bin", mode=0o755)
    self.install_file(self.files_path / "Xsession", "etc/X11", mode=0o755)

    # default xsession scripts
    self.install_dir("etc/X11/Xsession.d")
    self.install_file(
        self.files_path / "00default", "etc/X11/Xsession.d", mode=0o755
    )

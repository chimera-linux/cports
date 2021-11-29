pkgname = "xkeyboard-config"
pkgver = "2.34"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-xkb-rules-symlink=xfree86,xorg", "--enable-compat-rules"
]
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf", "xsltproc", "python", "perl"]
makedepends = ["libx11-devel", "xkbcomp"]
depends = ["xkbcomp"]
pkgdesc = "X Keyboard Configuration Database"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/XKeyboardConfig"
source = f"$(XORG_SITE)/data/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "b321d27686ee7e6610ffe7b56e28d5bbf60625a1f595124cd320c0caa717b8ce"
options = ["lto"]

def post_install(self):
    self.install_license("COPYING")

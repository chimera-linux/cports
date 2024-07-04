pkgname = "xorgproto"
pkgver = "2024.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-legacy"]
hostmakedepends = ["pkgconf", "xorg-util-macros", "automake", "libtool"]
pkgdesc = "Combined X.Org X11 protocol headers"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/proto/{pkgname}-{pkgver}.tar.gz"
sha256 = "4f6b9b4faf91e5df8265b71843a91fc73dc895be6210c84117a996545df296ce"
# we don't want dependencies on all the pkg-config stuff
options = ["!scanrundeps"]


def post_install(self):
    for f in self.cwd.glob("COPYING-*"):
        self.install_license(f)

    for f in (self.destdir / "usr/include/X11/extensions").glob("apple*"):
        f.unlink()
    for f in (self.destdir / "usr/include/X11/extensions").glob("windows*"):
        f.unlink()

    self.uninstall(f"usr/share/licenses/{pkgname}/COPYING-applewmproto")
    self.uninstall(f"usr/share/licenses/{pkgname}/COPYING-windowswmproto")

    self.uninstall("usr/share/pkgconfig/applewmproto.pc")
    self.uninstall("usr/share/pkgconfig/windowswmproto.pc")

    # provided by libx11-devel
    self.uninstall("usr/include/X11/extensions/XKBgeom.h")

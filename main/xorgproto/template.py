pkgname = "xorgproto"
pkgver = "2021.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-legacy"]
hostmakedepends = ["pkgconf", "xorg-util-macros"]
pkgdesc = "Combined X.Org X11 protocol headers"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/proto/{pkgname}-{pkgver}.tar.gz"
sha256 = "be6ddd6590881452fdfa170c1c9ff87209a98d36155332cbf2ccbc431add86ff"
# we don't want dependencies on all the pkg-config stuff
options = ["!scanrundeps"]

def post_install(self):
    for f in self.cwd.glob("COPYING-*"):
        self.install_license(f)

    for f in (self.destdir / "usr/include/X11/extensions").glob("apple*"):
        f.unlink()
    for f in (self.destdir / "usr/include/X11/extensions").glob("windows*"):
        f.unlink()

    self.rm(
        self.destdir / f"usr/share/licenses/{pkgname}/COPYING-applewmproto"
    )
    self.rm(
        self.destdir / f"usr/share/licenses/{pkgname}/COPYING-windowswmproto"
    )

    self.rm(self.destdir / "usr/share/pkgconfig/applewmproto.pc")
    self.rm(self.destdir / "usr/share/pkgconfig/windowswmproto.pc")

    # provided by libx11-devel
    self.rm(self.destdir / "usr/include/X11/extensions/XKBgeom.h")

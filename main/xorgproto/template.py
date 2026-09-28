pkgname = "xorgproto"
pkgver = "2024.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-legacy"]
hostmakedepends = ["automake", "libtool", "pkgconf", "xorg-util-macros"]
pkgdesc = "Combined X.Org X11 protocol headers"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/proto/xorgproto-{pkgver}.tar.gz"
sha256 = "4f6b9b4faf91e5df8265b71843a91fc73dc895be6210c84117a996545df296ce"
# we don't want dependencies on all the pkg-config stuff
options = ["!scanrundeps"]


def post_install(self):
    for f in self.cwd.glob("COPYING-*"):
        self.install_license(f)

    for os in ["apple", "windows"]:
        self.uninstall(f"usr/include/X11/extensions/{os}*", glob=True)
        self.uninstall(f"usr/share/licenses/{pkgname}/COPYING-{os}wmproto")
        self.uninstall(f"usr/share/pkgconfig/{os}wmproto.pc")

    # provided by libx11-devel
    self.uninstall("usr/include/X11/extensions/XKBgeom.h")

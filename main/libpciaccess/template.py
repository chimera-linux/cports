pkgname = "libpciaccess"
pkgver = "0.19"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dinstall-scanpci=false"]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "X11 PCI access library"
license = "MIT"
url = "http://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libpciaccess-{pkgver}.tar.xz"
sha256 = "3c55aa86c82e54a4e3109786f0463530d53b36b6d1cfd14616454f985dd2aa43"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libpciaccess-devel")
def _(self):
    return self.default_devel()

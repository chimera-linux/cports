pkgname = "umockdev"
pkgver = "0.18.3"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gobject-introspection",
    "meson",
    "pkgconf",
    "python",
    "vala",
]
makedepends = ["glib-devel", "libpcap-devel", "linux-headers", "udev-devel"]
pkgdesc = "Mock hardware devices"
maintainer = "triallax <triallax@tutanota.com>"
license = "LGPL-2.1-or-later"
url = "https://github.com/martinpitt/umockdev"
source = f"https://github.com/martinpitt/umockdev/releases/download/{pkgver}/umockdev-{pkgver}.tar.xz"
sha256 = "aba95c323037c842f1617931260231b8557d119aa2891cbca8b811fcc559294a"
# TODO
options = ["!check", "!cross"]


@subpackage("umockdev-devel")
def _(self):
    return self.default_devel()

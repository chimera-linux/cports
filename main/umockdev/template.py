pkgname = "umockdev"
pkgver = "0.18.4"
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
checkdepends = ["libgudev-devel", "udev"]
pkgdesc = "Mock hardware devices"
maintainer = "triallax <triallax@tutanota.com>"
license = "LGPL-2.1-or-later"
url = "https://github.com/martinpitt/umockdev"
source = f"https://github.com/martinpitt/umockdev/releases/download/{pkgver}/umockdev-{pkgver}.tar.xz"
sha256 = "115306f17be78f8c99e20652e2deccdd48df38736bf00eb4f43fefc3809a319c"
patch_style = "patch"
# see below
options = ["!cross"]

if self.profile().arch in ["ppc64", "ppc64le"]:
    # FIXME: ERROR:../tests/test-ioctl-tree.c:99:t_type_get_by: assertion failed
    # (ioctl_type_get_by_name("USBDEVFS_CONNECTINFO", &id)->id == USBDEVFS_CONNECTINFO):
    # (-2146937583 == 2148029713)
    options += ["!check"]


@subpackage("umockdev-devel")
def _(self):
    return self.default_devel()

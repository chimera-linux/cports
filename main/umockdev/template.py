pkgname = "umockdev"
pkgver = "0.19.3"
pkgrel = 0
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
license = "LGPL-2.1-or-later"
url = "https://github.com/martinpitt/umockdev"
source = f"{url}/releases/download/{pkgver}/umockdev-{pkgver}.tar.xz"
sha256 = "46e45eab6f656bfc092438d7e0e5df4c5f51d18e3a83360c2be680b207a1a0b7"
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

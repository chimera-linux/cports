pkgname = "sshfs"
pkgver = "3.7.6"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "ninja",
    "pkgconf",
    "python-docutils",
    "scdoc",
]
makedepends = [
    "fuse-devel",
    "glib-devel",
    "linux-headers",
]
pkgdesc = "FUSE client for SSH"
license = "GPL-2.0-or-later"
url = "https://github.com/libfuse/sshfs"
source = f"{url}/releases/download/sshfs-{pkgver}/sshfs-{pkgver}.tar.xz"
sha256 = "6a1bcb31450a077e9cb1b7ff158c71de34db697c3c0da6cb362502131e495893"
# CFI: shitty struct buffer -> struct readdir_handle cast
hardening = ["vis", "!cfi"]
# requires fuse kernel module
options = ["!check"]

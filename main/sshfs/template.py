pkgname = "sshfs"
pkgver = "3.7.5"
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
sha256 = "0e45db63c2d00919db3174134fa234c6e0682d6fe573c46312d1d53d1d61a8bb"
# CFI: shitty struct buffer -> struct readdir_handle cast
hardening = ["vis", "!cfi"]
# requires fuse kernel module
options = ["!check"]

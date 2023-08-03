pkgname = "sshfs"
pkgver = "3.7.3"
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
]
pkgdesc = "FUSE client for SSH"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://github.com/libfuse/sshfs"
source = f"{url}/releases/download/sshfs-{pkgver}/sshfs-{pkgver}.tar.xz"
sha256 = "5218ce7bdd2ce0a34137a0d7798e0f6d09f0e6d21b1e98ee730a18b0699c2e99"
# FIXME: cfi shitty struct buffer -> struct readdir_handle cast
hardening = ["vis"]
# requires fuse kernel module
options = ["!check"]

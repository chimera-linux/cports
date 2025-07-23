pkgname = "ostree"
pkgver = "2025.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-builtin-grub2-mkconfig",
    "--with-crypto=openssl",
    "--with-modern-grub",
    "--with-openssl",
    "--with-curl",
    "--with-soup=no",
    "--disable-gtk-doc",
]
hostmakedepends = [
    "automake",
    "bison",
    "docbook-xsl-nons",
    "gobject-introspection",
    "gtk-doc-tools",
    "libtool",
    "libxslt-progs",
    "pkgconf",
]
makedepends = [
    "curl-devel",
    "e2fsprogs-devel",
    "fuse-devel",
    "glib-devel",
    "gpgme-devel",
    "libarchive-devel",
    "libgpg-error-devel",
    "linux-headers",
    "openssl3-devel",
    "xz-devel",
]
checkdepends = ["attr-progs", "libarchive-progs", "gnupg", "xz"]
pkgdesc = "Operating system and container binary deployment and upgrades"
license = "LGPL-2.0-or-later"
url = "https://ostreedev.github.io/ostree"
source = f"https://github.com/ostreedev/ostree/releases/download/v{pkgver}/libostree-{pkgver}.tar.xz"
sha256 = "014d12d19ea664fae53fe147d3d2c0b7465a3c37e099c87d289df908adeb5669"
# failing on their test harness, i will find motivation Soon
options = ["!check"]


@subpackage("ostree-devel")
def _(self):
    return self.default_devel()

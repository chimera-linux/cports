pkgname = "ostree"
pkgver = "2026.6"
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
sha256 = "164b8226aea6a0e6601036de02a5e3b62307bae25890ed557fb4e19020bd5974"
# failing on their test harness, i will find motivation Soon
options = ["!check"]


@subpackage("ostree-devel")
def _(self):
    return self.default_devel()

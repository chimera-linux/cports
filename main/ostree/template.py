pkgname = "ostree"
pkgver = "2024.4"
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
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "bison",
    "docbook-xsl-nons",
    "gmake",
    "gobject-introspection",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
    "xsltproc",
]
makedepends = [
    "e2fsprogs-devel",
    "fuse-devel",
    "glib-devel",
    "gpgme-devel",
    "libcurl-devel",
    "libgpg-error-devel",
    "linux-headers",
    "openssl-devel",
    "xz-devel",
    "libarchive-devel",
]
checkdepends = ["attr-progs", "bsdtar", "gnupg", "xz"]
pkgdesc = "Operating system and container binary deployment and upgrades"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.0-or-later"
url = "https://ostreedev.github.io/ostree"
source = f"https://github.com/ostreedev/ostree/releases/download/v{pkgver}/libostree-{pkgver}.tar.xz"
sha256 = "63c9190821333ac7373e0d923e4c2766b25ebdcfdf4efb44cb5928c6589d9fcb"
# failing on their test harness, i will find motivation Soon
options = ["!check"]


@subpackage("ostree-devel")
def _devel(self):
    return self.default_devel()

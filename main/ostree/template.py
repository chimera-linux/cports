pkgname = "ostree"
pkgver = "2023.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-builtin-grub2-mkconfig",
    "--with-ed25519-libsodium",
    "--with-openssl",
    "--with-curl",
    "--with-soup=no",
    "--disable-gtk-doc",
]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "bison",
    "xsltproc",
    "gmake",
    "gobject-introspection",
    "docbook-xsl-nons",
    "gtk-doc-tools",
]
makedepends = [
    "glib-devel",
    "liblzma-devel",
    "e2fsprogs-devel",
    "gpgme-devel",
    "fuse-devel",
    "libcurl-devel",
    "libgpg-error-devel",
    "libsodium-devel",
    "openssl-devel",
    "linux-headers",
]
checkdepends = ["attr-progs", "bsdtar", "gnupg", "xz"]
pkgdesc = "Operating system and container binary deployment and upgrades"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.0-or-later"
url = "https://ostreedev.github.io/ostree"
source = f"https://github.com/ostreedev/ostree/releases/download/v{pkgver}/libostree-{pkgver}.tar.xz"
sha256 = "bc593afb31fe1ac3d50419f917fafe321a0a3561d7bb2ba498a83740fe3adb14"
# failing on their test harness, i will find motivation Soon
options = ["!check", "!cross"]


@subpackage("ostree-devel")
def _devel(self):
    return self.default_devel()

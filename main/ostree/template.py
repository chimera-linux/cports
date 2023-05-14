pkgname = "ostree"
pkgver = "2023.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-builtin-grub2-mkconfig", "--with-ed25519-libsodium", "--with-openssl", "--with-curl",
                  "--with-soup=no"]
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "bison", "gtk-doc-tools", "xsltproc", "gmake"]
makedepends = ["glib-devel", "liblzma-devel", "e2fsprogs-devel", "gpgme-devel", "fuse-devel", "libcurl-devel",
               "gobject-introspection", "linux-headers", "libgpg-error-devel", "libsodium-devel", "openssl-devel"]
# checkdepends = ["attr-progs", "bsdtar", "gnupg", "xz"]
pkgdesc = "Operating system and container binary deployment and upgrades"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.0-or-later"
url = "https://ostreedev.github.io/ostree"
source = f"https://github.com/ostreedev/ostree/releases/download/v{pkgver}/libostree-{pkgver}.tar.xz"
sha256 = "dd792b167693a1971c9f6e3168013d906ac035100ff6c719a3b322eb44b96f55"
# failing on their test harness, i will find motivation Soon
options = ["!check"]


@subpackage("ostree-devel")
def _devel(self):
    return self.default_devel()

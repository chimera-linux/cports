pkgname = "libgcrypt"
pkgver = "1.11.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-static",
    "--without-capabilities",
    "ac_cv_sys_symbol_underscore=no",
]
hostmakedepends = [
    "automake",
    "libgpg-error-devel",  # for gpg-error.m4
    "libtool",
    "pkgconf",
]
makedepends = ["libgpg-error-devel"]
pkgdesc = "GNU cryptographic library"
license = "LGPL-2.1-or-later"
url = "https://www.gnupg.org"
source = f"{url}/ftp/gcrypt/libgcrypt/libgcrypt-{pkgver}.tar.bz2"
sha256 = "6ba59dd192270e8c1d22ddb41a07d95dcdbc1f0fb02d03c4b54b235814330aac"
options = ["linkundefver"]


def post_extract(self):
    # ancient dogshit
    self.rm("m4/gpg-error.m4")


@subpackage("libgcrypt-devel")
def _(self):
    return self.default_devel(extra=["usr/share/info"])


@subpackage("libgcrypt-progs")
def _(self):
    return self.default_progs()

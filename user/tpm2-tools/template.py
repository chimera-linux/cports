pkgname = "tpm2-tools"
pkgver = "5.7"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "autoconf",
    "automake",
    "gmake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "libcurl-devel",
    "openssl-devel",
    "tpm2-tss-devel",
]
pkgdesc = "Trusted Platform Module (TPM2.0) tools"
maintainer = "natthias <natthias@proton.me>"
license = "BSD-3-Clause"
url = "https://github.com/tpm2-software/tpm2-tools"
source = f"{url}/releases/download/{pkgver}/tpm2-tools-{pkgver}.tar.gz"
sha256 = "3810d36b5079256f4f2f7ce552e22213d43b1031c131538df8a2dbc3c570983a"
# symlinks tpm2 to tpm2_completion.bash
options = ["!lto", "!lintcomp"]


def post_install(self):
    self.install_license("docs/LICENSE")

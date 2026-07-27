pkgname = "tpm2-tools"
pkgver = "5.8"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "curl-devel",
    "openssl3-devel",
    "tpm2-tss-devel",
]
pkgdesc = "Trusted Platform Module (TPM2.0) tools"
license = "BSD-3-Clause"
url = "https://github.com/tpm2-software/tpm2-tools"
source = f"{url}/releases/download/{pkgver}/tpm2-tools-{pkgver}.tar.gz"
sha256 = "1cb73185cae814b4e15c7c2d0b22642d640faf48775f4156a1fd92edf84bef73"
# symlinks tpm2 to tpm2_completion.bash
options = ["!lto", "!lintcomp"]


def post_install(self):
    self.install_license("docs/LICENSE")

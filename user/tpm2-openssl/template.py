pkgname = "tpm2-openssl"
pkgver = "1.3.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "openssl3-devel",
    "tpm2-tss-devel",
]
pkgdesc = "OpenSSL provider for TPM2 integration"
license = "BSD-3-Clause"
url = "https://github.com/tpm2-software/tpm2-openssl"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "df14f849b0151a0550faf156c1c8e6d8465f089914881adae608de7c143301bd"
# requires a TPM2 device (not in the sandbox) or simulator (not packaged)
options = ["!check"]


def post_prepare(self):
    with open(self.cwd / "VERSION", "w") as f:
        f.write(pkgver)


def post_install(self):
    self.install_license("LICENSE")

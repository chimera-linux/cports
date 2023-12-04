pkgname = "tpm2-tss"
pkgver = "4.0.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-unit",
    "--runstatedir=/run",
    "--with-crypto=ossl",
    "--with-tctidefaultmodule=device",
    "--with-tctidefaultconfig=/dev/tpmrm0",
]
configure_gen = []
make_cmd = "gmake"
make_check_args = ["-j1"]
hostmakedepends = ["cmocka", "gmake", "perl", "pkgconf"]
makedepends = [
    "cmocka-devel",
    "json-c-devel",
    "libcurl-devel",
    "libuuid-devel",
    "linux-headers",
    "openssl-devel",
]
pkgdesc = "Implementation of TCG TPM2"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/tpm2-software/tpm2-tss"
source = f"{url}/releases/download/{pkgver}/tpm2-tss-{pkgver}.tar.gz"
sha256 = "532a70133910b6bd842289915b3f9423c0205c0ea009d65294ca18a74087c950"
# a few fail seemingly due to namespaces
options = ["!check"]
system_users = [
    {
        "name": "_tss",
        "id": None,
        "home": "/var/lib/tpm2-tss",
    }
]


def post_install(self):
    self.install_license("LICENSE")
    self.mv(self.destdir / "etc/tmpfiles.d", self.destdir / "usr/lib")
    self.rm(self.destdir / "etc/sysusers.d", recursive=True)


@subpackage("tpm2-tss-devel")
def _dev(self):
    return self.default_devel()

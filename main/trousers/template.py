pkgname = "trousers"
pkgver = "0.3.15"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["openssl-devel", "linux-headers"]
pkgdesc = "Trusted Computing Software Stack for the TPM"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://trousers.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "1e5be93e518372acf1d92d2f567d01a46fdb0b730487e544e6fb896c59cac77f"
file_modes = {
    "etc/tcsd.conf": ("tss", "tss", 0o600),
    "var/lib/tpm": ("tss", "tss", 0o700),
}
system_users = [
    {
        "name": "tss",
        "id": None,
        "home": "/var/lib/tpm",
    }
]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "tcsd")
    self.install_dir("var/lib/tpm", mode=0o700, empty=True)


@subpackage("libtspi")
def _tspi(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()


@subpackage("trousers-devel")
def _devel(self):
    return self.default_devel()

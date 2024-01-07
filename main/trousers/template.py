pkgname = "trousers"
pkgver = "0.3.15"
pkgrel = 2
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["openssl-devel", "linux-headers"]
pkgdesc = "Trusted Computing Software Stack for the TPM"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://trousers.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "1e5be93e518372acf1d92d2f567d01a46fdb0b730487e544e6fb896c59cac77f"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "tcsd")
    self.install_dir("usr/share/trousers")
    # tmpfiles will copy from it
    self.mv(self.destdir / "etc/tcsd.conf", self.destdir / "usr/share/trousers")
    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="tss.conf",
    )
    self.install_file(
        self.files_path / "tmpfiles.conf",
        "usr/lib/tmpfiles.d",
        name="tss.conf",
    )


@subpackage("libtspi")
def _tspi(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()


@subpackage("trousers-devel")
def _devel(self):
    return self.default_devel()

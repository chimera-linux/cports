pkgname = "trousers"
pkgver = "0.3.15"
pkgrel = 4
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["openssl3-devel", "linux-headers"]
pkgdesc = "Trusted Computing Software Stack for the TPM"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://trousers.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/trousers/trousers-{pkgver}.tar.gz"
sha256 = "1e5be93e518372acf1d92d2f567d01a46fdb0b730487e544e6fb896c59cac77f"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "tcsd")
    # tmpfiles will copy from it
    self.rename("etc/tcsd.conf", "usr/share/trousers/tcsd.conf", relative=False)
    self.install_sysusers(self.files_path / "sysusers.conf", name="tss")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf", name="tss")


@subpackage("trousers-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libtspi")]

    return self.default_libs()


@subpackage("trousers-devel")
def _(self):
    return self.default_devel()

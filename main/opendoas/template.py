pkgname = "opendoas"
pkgver = "6.8.1"
pkgrel = 0
build_style = "configure"
configure_args = ["--with-pam", "--with-timestamp", "--prefix=/usr"]
make_cmd = "gmake"
hostmakedepends = ["byacc", "gmake"]
makedepends = ["linux-pam-devel"]
pkgdesc = "Portable OpenBSD doas to execute commands as another user"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC AND BSD-3-Clause"
url = "https://github.com/Duncaen/OpenDoas"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "c9070ae745d0f1bbe68ef0783a3958cd011b409959f65fd100e6b42b8ad6b162"
suid_files = ["usr/bin/doas"]
# no test suite
options = ["!check"]

def pre_configure(self):
    self.cp(self.files_path / "doas.pam", "pam.d__doas__linux")

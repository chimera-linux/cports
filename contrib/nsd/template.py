pkgname = "nsd"
pkgver = "4.9.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-user=_nsd"]
make_check_target = "test"
hostmakedepends = ["automake", "bison", "flex"]
makedepends = [
    "libevent-devel",
    "openssl-devel",
]
pkgdesc = "Authoritative DNS name server"
maintainer = "yanchan09 <yan@omg.lol>"
license = "BSD-3-Clause"
url = "https://nlnetlabs.nl/projects/nsd/about"
source = f"https://nlnetlabs.nl/downloads/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "a6c23a53ee8111fa71e77b7565d1b8f486ea695770816585fbddf14e4367e6df"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")

    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "nsd")

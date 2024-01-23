pkgname = "nsd"
pkgver = "4.8.0"
pkgrel = 1
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
sha256 = "820da4e384721915f4bcaf7f2bed98519da563c6e4c130c742c724760ec02a0a"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")

    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="nsd.conf",
    )
    self.install_service(self.files_path / "nsd")

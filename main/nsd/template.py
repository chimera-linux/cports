pkgname = "nsd"
pkgver = "4.11.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-user=_nsd"]
# simdzone fails to load its own includes if we don't do this
make_dir = "."
make_check_target = "test"
hostmakedepends = ["automake", "bison", "flex"]
makedepends = [
    "libevent-devel",
    "openssl3-devel",
]
pkgdesc = "Authoritative DNS name server"
maintainer = "yanchan09 <yan@omg.lol>"
license = "BSD-3-Clause"
url = "https://nlnetlabs.nl/projects/nsd/about"
source = f"https://nlnetlabs.nl/downloads/nsd/nsd-{pkgver}.tar.gz"
sha256 = "696e50052008de4fa7ab1d818d5b77eb63247eea2f0575114c9592ff9188a614"
hardening = ["cfi", "vis"]


def post_install(self):
    self.install_license("LICENSE")

    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "nsd")

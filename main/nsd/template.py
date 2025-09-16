pkgname = "nsd"
pkgver = "4.12.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-user=_nsd"]
# simdzone fails to load its own includes if we don't do this
make_dir = "."
make_check_target = "test"
hostmakedepends = ["automake", "bison", "flex", "pkgconf"]
makedepends = [
    "dinit-chimera",
    "libevent-devel",
    "openssl3-devel",
]
pkgdesc = "Authoritative DNS name server"
license = "BSD-3-Clause"
url = "https://nlnetlabs.nl/projects/nsd/about"
source = f"https://nlnetlabs.nl/downloads/nsd/nsd-{pkgver}.tar.gz"
sha256 = "f9ecc2cf79ba50580f2df62918efc440084c5bf11057db44c19aa9643cd4b5e8"
hardening = ["cfi", "vis"]


def post_install(self):
    self.install_license("LICENSE")

    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "nsd")

pkgname = "unbound"
pkgver = "1.18.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-dnscrypt",
    "--enable-event-api",
    "--with-username=_unbound",
    "--with-rootkey-file=/etc/dns/root.key",
    "--with-conf-file=/etc/unbound/unbound.conf",
    "--with-pidfile=/run/unbound.pid",
    f"--with-ssl={self.profile().sysroot / 'usr'}",
    f"--with-libevent={self.profile().sysroot / 'usr'}",
    f"--with-libexpat={self.profile().sysroot / 'usr'}",
]
make_dir = "."  # fails to build otherwise
hostmakedepends = ["pkgconf"]
makedepends = [
    "libexpat-devel",
    "libevent-devel",
    "libsodium-devel",
    "openssl-devel",
]
depends = ["dnssec-anchors"]
pkgdesc = "Validating, recursive, and caching DNS resolver"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://nlnetlabs.nl/projects/unbound/about"
source = f"https://nlnetlabs.nl/downloads/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "3da95490a85cff6420f26fae0b84a49f5112df1bf1b7fc34f8724f02082cb712"
system_users = ["_unbound"]


def post_install(self):
    self.install_license("LICENSE")

    self.install_file("doc/example.conf", "usr/share/examples/unbound")
    (self.destdir / "etc/unbound/unbound.conf").unlink()
    self.install_file(self.files_path / "unbound.conf", "etc/unbound")

    self.install_service(self.files_path / "unbound")


@subpackage("libunbound")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()


@subpackage("unbound-devel")
def _devel(self):
    self.depends += ["openssl-devel", "libsodium-devel"]

    return self.default_devel()


configure_gen = []

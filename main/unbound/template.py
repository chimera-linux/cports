pkgname = "unbound"
pkgver = "1.19.2"
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
configure_gen = []
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
sha256 = "cc560d345734226c1b39e71a769797e7fdde2265cbb77ebce542704bba489e55"


def post_install(self):
    self.install_license("LICENSE")

    self.install_file("doc/example.conf", "usr/share/examples/unbound")
    (self.destdir / "etc/unbound/unbound.conf").unlink()
    self.install_file(self.files_path / "unbound.conf", "etc/unbound")

    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="unbound.conf",
    )
    self.install_service(self.files_path / "unbound")


@subpackage("libunbound")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()


@subpackage("unbound-devel")
def _devel(self):
    self.depends += ["openssl-devel", "libsodium-devel"]

    return self.default_devel()

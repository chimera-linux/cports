pkgname = "unbound"
pkgver = "1.20.0"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--enable-cachedb",
    "--enable-dnscrypt",
    "--enable-dnstap",
    "--enable-event-api",
    "--enable-subnet",
    "--enable-tfo-client",
    "--enable-tfo-server",
    "--with-username=_unbound",
    "--with-rootkey-file=/etc/dns/root.key",
    "--with-conf-file=/etc/unbound/unbound.conf",
    "--with-pidfile=/run/unbound.pid",
    f"--with-libevent={self.profile().sysroot / 'usr'}",
    f"--with-libexpat={self.profile().sysroot / 'usr'}",
    f"--with-libhiredis={self.profile().sysroot / 'usr'}",
    f"--with-libnghttp2={self.profile().sysroot / 'usr'}",
    f"--with-protobuf-c={self.profile().sysroot / 'usr'}",
    f"--with-ssl={self.profile().sysroot / 'usr'}",
]
configure_gen = []
make_dir = "."  # fails to build otherwise
hostmakedepends = [
    "pkgconf",
    "protobuf-c-devel",
]
makedepends = [
    "hiredis-devel",
    "libexpat-devel",
    "libevent-devel",
    "libsodium-devel",
    "nghttp2-devel",
    "openssl-devel",
    "protobuf-c-devel",
]
depends = ["dnssec-anchors"]
pkgdesc = "Validating, recursive, and caching DNS resolver"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://nlnetlabs.nl/projects/unbound/about"
source = f"https://nlnetlabs.nl/downloads/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "56b4ceed33639522000fd96775576ddf8782bb3617610715d7f1e777c5ec1dbf"


def post_install(self):
    self.install_license("LICENSE")

    self.install_file("doc/example.conf", "usr/share/examples/unbound")
    (self.destdir / "etc/unbound/unbound.conf").unlink()
    self.install_file(self.files_path / "unbound.conf", "etc/unbound")

    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "unbound")


@subpackage("libunbound")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()


@subpackage("unbound-devel")
def _devel(self):
    self.depends += ["openssl-devel", "libsodium-devel"]

    return self.default_devel()

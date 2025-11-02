pkgname = "unbound"
pkgver = "1.24.1"
pkgrel = 0
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
    "--with-rootkey-file=/usr/share/dns/root.key",
    "--with-conf-file=/etc/unbound/unbound.conf",
    "--with-pidfile=/run/unbound.pid",
    f"--with-libevent={self.profile().sysroot / 'usr'}",
    f"--with-libexpat={self.profile().sysroot / 'usr'}",
    f"--with-libhiredis={self.profile().sysroot / 'usr'}",
    f"--with-libnghttp2={self.profile().sysroot / 'usr'}",
    f"--with-protobuf-c={self.profile().sysroot / 'usr'}",
    f"--with-ssl={self.profile().sysroot / 'usr'}",
]
make_dir = "."  # fails to build otherwise
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "protobuf-c-devel",
]
makedepends = [
    "hiredis-devel",
    "libevent-devel",
    "libexpat-devel",
    "libsodium-devel",
    "nghttp2-devel",
    "openssl3-devel",
    "protobuf-c-devel",
]
depends = ["dns-root-data"]
pkgdesc = "Validating, recursive, and caching DNS resolver"
license = "BSD-3-Clause"
url = "https://nlnetlabs.nl/projects/unbound/about"
source = f"https://nlnetlabs.nl/downloads/unbound/unbound-{pkgver}.tar.gz"
sha256 = "7f2b1633e239409619ae0527f67878b0f33ae0ec0ee5a3a51c042c359ba1eeab"
skip_dependencies = ["usr/lib/dinit.d/*"]


def post_install(self):
    self.install_license("LICENSE")

    self.install_file("doc/example.conf", "usr/share/examples/unbound")
    (self.destdir / "etc/unbound/unbound.conf").unlink()
    self.install_file(self.files_path / "unbound.conf", "etc/unbound")

    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "unbound")


@subpackage("unbound-libs")
def _(self):
    self.renames = ["libunbound"]

    return self.default_libs()


@subpackage("unbound-devel")
def _(self):
    self.depends += ["openssl3-devel", "libsodium-devel"]

    return self.default_devel()

pkgname = "unbound"
pkgver = "1.22.0"
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
    "pkgconf",
    "protobuf-c-devel",
    "slibtool",
]
makedepends = [
    "hiredis-devel",
    "libexpat-devel",
    "libevent-devel",
    "libsodium-devel",
    "nghttp2-devel",
    "openssl3-devel",
    "protobuf-c-devel",
]
depends = ["dns-root-data"]
pkgdesc = "Validating, recursive, and caching DNS resolver"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://nlnetlabs.nl/projects/unbound/about"
source = f"https://nlnetlabs.nl/downloads/unbound/unbound-{pkgver}.tar.gz"
sha256 = "c5dd1bdef5d5685b2cedb749158dd152c52d44f65529a34ac15cd88d4b1b3d43"


def post_install(self):
    self.install_license("LICENSE")

    self.install_file("doc/example.conf", "usr/share/examples/unbound")
    (self.destdir / "etc/unbound/unbound.conf").unlink()
    self.install_file(self.files_path / "unbound.conf", "etc/unbound")

    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "unbound")


@subpackage("unbound-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libunbound")]

    return self.default_libs()


@subpackage("unbound-devel")
def _(self):
    self.depends += ["openssl3-devel", "libsodium-devel"]

    return self.default_devel()

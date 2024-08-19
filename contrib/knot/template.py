pkgname = "knot"
pkgver = "3.3.8"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-dnstap",
    "--enable-fastparser",
    "--enable-quic",
    "--with-rundir=/run/knot",
]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gmake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "fstrm-devel",
    "gnutls-devel",
    "libedit-devel",
    "linux-headers",
    "lmdb-devel",
    "nghttp2-devel",
    "ngtcp2-devel",
    "protobuf-c-devel",
    "userspace-rcu-devel",
]
pkgdesc = "Authoritative-only DNS server"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "GPL-3.0-or-later"
url = "https://www.knot-dns.cz"
source = f"https://secure.nic.cz/files/knot-dns/knot-{pkgver}.tar.xz"
sha256 = "498de8338489a625673797f7ecc921fa4490c826afbfa42fa66922b525089e6a"


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "knotd")


@subpackage("knot-devel")
def _devel(self):
    return self.default_devel()


@subpackage("knot-libs")
def _libs(self):
    return self.default_libs()


@subpackage("knot-progs")
def _progs(self):
    def func():
        for prog in ["kdig", "khost", "knsupdate"]:
            self.take(f"usr/bin/{prog}")
            self.take(f"usr/share/man/man1/{prog}.1")

    return func

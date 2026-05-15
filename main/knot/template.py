pkgname = "knot"
pkgver = "3.5.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-dnstap",
    "--enable-fastparser",
    "--enable-quic",
    "--with-rundir=/run/knot",
]
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "dinit-chimera",
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
license = "GPL-3.0-or-later"
url = "https://www.knot-dns.cz"
source = f"https://secure.nic.cz/files/knot-dns/knot-{pkgver}.tar.xz"
sha256 = "4a0bc892dfaa5a150ff2855f0a88f2267124bc271818eae9a2b1f6da487c34e4"


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "knotd")


@subpackage("knot-devel")
def _(self):
    return self.default_devel()


@subpackage("knot-libs")
def _(self):
    return self.default_libs()


@subpackage("knot-progs")
def _(self):
    def func():
        for prog in ["kdig", "khost", "knsupdate"]:
            self.take(f"cmd:{prog}")

    return func

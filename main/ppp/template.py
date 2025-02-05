# fix up networkmanager when updating this (versioned .so paths)
pkgname = "ppp"
pkgver = "2.5.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--prefix=/usr",
    "--enable-multilink",
    "--with-logfile-dir=/var/log/ppp",
    "--with-runtime-dir=/run/pppd",
]
make_build_args = ["CBCP=y"]
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["libpcap-devel", "openssl3-devel", "linux-headers"]
pkgdesc = "PPP (Point-to-Point Protocol) daemon"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause AND LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://ppp.samba.org"
source = f"https://ftp.samba.org/pub/ppp/ppp-{pkgver}.tar.gz"
sha256 = "47da358de54a10cb10bf6ff2cf9b1c03c0d3555518f6182e8f701b8e55733cb2"
# no check target
# no file for bsd
options = ["!check", "!distlicense"]


def post_install(self):
    self.install_file("include/linux/ppp_defs.h", "usr/include/net")

    # eliminate suid bits
    for f in (self.destdir / f"usr/lib/pppd/{pkgver}").glob("*.so"):
        f.chmod(0o755)

    # just says "lock"
    self.uninstall("etc/ppp/options.example")
    self.install_file(self.files_path / "options", "etc/ppp", mode=0o644)
    self.install_file(self.files_path / "ip-up", "etc/ppp", mode=0o755)
    self.install_file(self.files_path / "ip-down", "etc/ppp", mode=0o755)
    self.install_file(self.files_path / "ipv6-up", "etc/ppp", mode=0o755)
    self.install_file(self.files_path / "ipv6-down", "etc/ppp", mode=0o755)

    self.install_file(
        self.files_path / "ip-up.d.dns.sh",
        "etc/ppp/ip-up.d",
        name="00-dns.sh",
        mode=0o755,
    )
    self.install_file(
        self.files_path / "ip-down.d.dns.sh",
        "etc/ppp/ip-down.d",
        name="00-dns.sh",
        mode=0o755,
    )
    self.install_file(
        self.files_path / "ipv6-up.d.iface-config.sh",
        "etc/ppp/ipv6-up.d",
        name="00-iface-config.sh",
        mode=0o755,
    )
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")

    self.install_bin("scripts/pon")
    self.install_man("scripts/pon.1")
    self.install_bin("scripts/poff")
    self.install_bin("scripts/plog")


@subpackage("ppp-devel")
def _(self):
    self.depends += [self.parent, "libpcap-devel"]

    return self.default_devel()

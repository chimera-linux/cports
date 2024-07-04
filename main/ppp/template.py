# fix up networkmanager when updating this (versioned .so paths)
pkgname = "ppp"
pkgver = "2.5.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--prefix=/usr",
    "--with-logfile-dir=/var/log/ppp",
    "--with-runtime-dir=/run/pppd",
]
make_cmd = "gmake"
make_build_args = ["CBCP=y"]
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["libpcap-devel", "openssl-devel", "linux-headers"]
pkgdesc = "PPP (Point-to-Point Protocol) daemon"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause AND LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://ppp.samba.org"
source = f"https://ftp.samba.org/pub/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "5cae0e8075f8a1755f16ca290eb44e6b3545d3f292af4da65ecffe897de636ff"
# no check target
options = ["!check"]


def post_install(self):
    self.install_file("include/net/ppp_defs.h", "usr/include/net")

    # eliminate suid bits
    for f in (self.destdir / f"usr/lib/pppd/{pkgver}").glob("*.so"):
        f.chmod(0o755)

    self.uninstall("etc/ppp/options")
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
    self.install_dir("etc/ppp/ipv6-down.d", empty=True)
    self.install_dir("etc/ppp/peers", empty=True)

    self.install_bin("scripts/pon")
    self.install_man("scripts/pon.1")
    self.install_bin("scripts/poff")
    self.install_bin("scripts/plog")


@subpackage("ppp-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}", "libpcap-devel"]

    return self.default_devel()


configure_gen = []

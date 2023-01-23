# fix up networkmanager when updating this (versioned .so paths)
pkgname = "ppp"
pkgver = "2.4.9"
pkgrel = 0
build_style = "configure"
configure_args = ["--prefix=/usr"]
make_cmd = "gmake"
make_build_args = ["CBCP=y"]
hostmakedepends = ["gmake"]
makedepends = ["libpcap-devel", "openssl-devel", "linux-headers"]
pkgdesc = "PPP (Point-to-Point Protocol) daemon"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause AND LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://ppp.samba.org"
source = f"https://ftp.samba.org/pub/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "f938b35eccde533ea800b15a7445b2f1137da7f88e32a16898d02dee8adc058d"
# unmarked api
hardening = ["!vis"]
# no check target
options = ["!check"]

def init_configure(self):
    cfl = self.get_cflags(shell = True)
    ldfl = self.get_ldflags(shell = True)

    self.configure_args += [
        "--cc=" + self.get_tool("CC"),
        "--cflags=" + cfl
    ]
    self.make_build_args += [
        "LDFLAGS=" + cfl + " " + ldfl,
        "CBUILD_SYSROOT=" + str(self.profile().sysroot)
    ]
    self.make_install_args += [
        "INSTROOT=" + str(self.chroot_destdir),
        "DESTDIR=" + str(self.chroot_destdir / "usr"),
        "BINDIR=" + str(self.chroot_destdir / "usr/bin"),
        "CBUILD_SYSROOT=" + str(self.profile().sysroot)
    ]

def post_install(self):
    self.install_file("include/net/ppp_defs.h", "usr/include/net")

    # eliminate suid bits
    for f in (self.destdir / f"usr/lib/pppd/{pkgver}").glob("*.so"):
        f.chmod(0o755)

    self.install_file(self.files_path / "options", "etc/ppp", mode = 0o644)
    self.install_file(self.files_path / "ip-up", "etc/ppp", mode = 0o755)
    self.install_file(self.files_path / "ip-down", "etc/ppp", mode = 0o755)
    self.install_file(self.files_path / "ipv6-up", "etc/ppp", mode = 0o755)
    self.install_file(self.files_path / "ipv6-down", "etc/ppp", mode = 0o755)

    self.install_file(
        self.files_path / "ip-up.d.dns.sh", "etc/ppp/ip-up.d",
        name = "00-dns.sh", mode = 0o755
    )
    self.install_file(
        self.files_path / "ip-down.d.dns.sh", "etc/ppp/ip-down.d",
        name = "00-dns.sh", mode = 0o755
    )
    self.install_file(
        self.files_path / "ipv6-up.d.iface-config.sh", "etc/ppp/ipv6-up.d",
        name = "00-iface-config.sh", mode = 0o755
    )
    self.install_dir("etc/ppp/ipv6-down.d", empty = True)
    self.install_dir("etc/ppp/peers", empty = True)

    self.install_bin("scripts/pon")
    self.install_man("scripts/pon.1")
    self.install_bin("scripts/poff")
    self.install_bin("scripts/plog")

    self.install_file("etc.ppp/pap-secrets", "etc/ppp", mode = 0o600)
    self.install_file("etc.ppp/chap-secrets", "etc/ppp", mode = 0o600)

@subpackage("ppp-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}", "libpcap-devel"]

    return self.default_devel()

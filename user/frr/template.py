pkgname = "frr"
pkgver = "10.4.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--enable-configfile-mask=0640",
    "--enable-group=_frr",
    "--enable-logfile-mask=0640",
    "--enable-rpki",
    "--enable-user=_frr",
    "--enable-vty-group=_frrvty",
    "--sbindir=/usr/lib/frr",
]
configure_gen = ["./bootstrap.sh"]
make_dir = "."
hostmakedepends = [
    "automake",
    "bison",
    "flex",
    "libtool",
    "musl-bsd-headers",
    "pkgconf",
]
makedepends = [
    "c-ares-devel",
    "elfutils-devel",
    "json-c-devel",
    "libcap-devel",
    "libyang-devel",
    "libzmq-devel",
    "linux-headers",
    "pcre2-devel",
    "protobuf-c-devel",
    "python-devel",
    "readline-devel",
    "rtrlib-devel",
]
checkdepends = ["python-pytest"]
pkgdesc = "IP routing protocol suite"
license = "GPL-2.0-or-later"
url = "https://frrouting.org"
source = (
    f"https://github.com/FRRouting/frr/archive/refs/tags/frr-{pkgver}.tar.gz"
)
sha256 = "8e4003eaba168626c5ea7a6735f2c85c87b04214e6f8c8f2715b21f8ae40970b"


def post_install(self):
    for f in [
        "daemons",
        "frr.conf",
        "vtysh.conf",
        "support_bundle_commands.conf",
    ]:
        self.install_file(f"tools/etc/frr/{f}", "usr/share/etc/frr")
    self.install_file(
        "tools/etc/iproute2/rt_protos.d/frr.conf",
        "usr/share/iproute2/rt_protos.d",
    )
    self.install_license("COPYING")
    self.install_sysusers("^/sysusers.conf")
    self.install_tmpfiles("^/tmpfiles.conf")
    self.install_service("^/frr")
    self.install_service("^/frr-daemon")
    self.install_service("^/frr-zebra")
    # devel files are only for build usage and should not be part of pkg
    self.uninstall("usr/include")
    self.uninstall("usr/lib/*.so", glob=True)
    # FRR provides multiple startup scripts, lets keep only frrinit.sh
    self.uninstall("usr/lib/frr/frr")
    self.uninstall("usr/lib/frr/frr-reload")

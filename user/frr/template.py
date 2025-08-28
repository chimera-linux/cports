pkgname = "frr"
pkgver = "10.7.1"
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
    "pkgconf",
]
makedepends = [
    "c-ares-devel",
    "dinit-chimera",
    "elfutils-devel",
    "json-c-devel",
    "libcap-devel",
    "libyang-devel",
    "libzmq-devel",
    "linux-headers",
    "musl-bsd-headers",
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
sha256 = "6aaf9d89deb94eeda6acceaa6fe48d8cd365d0908231e58f628538ff49696fc4"
options = ["etcfiles"]


def post_install(self):
    for f in [
        "daemons",
        "frr.conf",
        "vtysh.conf",
        "support_bundle_commands.conf",
    ]:
        self.install_file(f"tools/etc/frr/{f}", "etc/frr")
    self.install_file(
        "tools/etc/iproute2/rt_protos.d/frr.conf",
        "usr/share/iproute2/rt_protos.d",
    )
    self.install_license("COPYING")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "frr")
    self.install_service(self.files_path / "frr-daemon")
    self.install_service(self.files_path / "frr-rundir")
    self.install_service(self.files_path / "frr-zebra")
    # build only
    self.uninstall("usr/include")
    self.uninstall("usr/lib/*.so", glob=True)
    # FRR provides multiple startup scripts, lets keep only frrinit.sh
    self.uninstall("usr/lib/frr/frr")
    self.uninstall("usr/lib/frr/frr-reload")

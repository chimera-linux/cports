pkgname = "frr"
pkgver = "10.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--enable-configfile-mask=0640",
    "--enable-logfile-mask=0640",
    "--enable-rpki",
    "--enable-vty-group=frrvty",
    "--sbindir=/usr/lib/frr",
]
# configure_env = {"LIBTOOLFLAGS": "-rpath /usr/lib/frr"}
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
sha256 = "0f10aca9074c773c12be8a07382c7560d625d4a2c842d82261d18bb8f4b26f6c"


def post_install(self):
    for f in [
        "daemons",
        "frr.conf",
        "vtysh.conf",
        "support_bundle_commands.conf",
    ]:
        self.install_file(f"tools/etc/frr/{f}", "usr/share/frr/conf")
    self.install_file(
        "tools/etc/iproute2/rt_protos.d/frr.conf",
        "usr/share/iproute2/rt_protos.d",
    )
    self.install_license("COPYING")
    self.install_sysusers("^/sysusers.conf")
    self.install_tmpfiles("^/tmpfiles.conf")
    self.install_service("^/frr")
    # devel files are only for build usage and should not be part of pkg
    self.uninstall("usr/include")
    self.uninstall("usr/lib/*.so", glob=True)
    # FRR provides multiple startup scripts, lets keep only frrinit.sh
    self.uninstall("usr/lib/frr/frr")
    self.uninstall("usr/lib/frr/frr-reload")


@subpackage("frr-pythontools")
def _(self):
    self.subdesc = "python tools"
    self.depends = [self.parent]
    return ["usr/lib/frr/*.py"]


@subpackage("frr-rpki")
def _(self):
    self.subdesc = "BGP RPKI support"
    self.depends = [self.parent]
    return [
        "usr/lib/frr/modules/bgpd_rpki.so",
        "usr/share/yang/frr-bgp-rpki.yang",
    ]

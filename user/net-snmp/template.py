pkgname = "net-snmp"
pkgver = "5.9.5.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-embedded-perl",
    "--disable-static",
    "--enable-blumenthal-aes",
    "--enable-ipv6",
    "--enable-ucd-snmp-compatibility",
    "--with-defaults",
    "--with-logfile=/var/log/net-snmpd.log",
    "--with-openssl",
    "--with-persistent-directory=/usr/lib/net-snmp",
]
make_check_target = "test"
hostmakedepends = [
    "automake",
    "file",
    "linux-headers",
    "pkgconf",
    "slibtool",
]
makedepends = ["dinit-chimera", "openssl3-devel"]
checkdepends = ["iproute2"]
pkgdesc = "Simple Network Management Protocol"
license = "BSD-3-Clause"
url = "http://www.net-snmp.org"
source = f"https://sourceforge.net/projects/{pkgname}/files/{pkgname}/{pkgver}/net-snmp-{pkgver}.tar.gz"
sha256 = "16707719f833184a4b72835dac359ae188123b06b5e42817c00790d7dc1384bf"
# tests take an eternity
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
    self.uninstall("usr/lib/libsnmp*", glob=True)
    self.install_file(
        "build/EXAMPLE.conf", "usr/share/examples/net-snmp", name="snmpd.conf"
    )
    self.install_file(self.files_path / "snmptrapd.conf", "etc/snmp")
    self.install_service(self.files_path / "snmpd")
    self.install_service(self.files_path / "snmptrapd")


@subpackage("net-snmp-snmpd")
def _(self):
    self.pkgdesc = "Simple Network Management Protocol daemon"
    self.depends = [self.parent]

    return [
        "usr/bin/net-snmp-create-v3-user",
        "usr/bin/snmpd",
        "usr/lib/dinit.d/snmpd",
        "usr/share/examples/net-snmp/snmpd.conf",
    ]


@subpackage("net-snmp-snmptrapd")
def _(self):
    self.pkgdesc = "Simple Network Management Protocol notification receiver"
    self.depends = [self.parent]
    self.options = ["etcfiles"]

    return [
        "etc/snmp/snmptrapd.conf",
        "usr/bin/snmptrapd",
        "usr/lib/dinit.d/snmptrapd",
    ]


@subpackage("net-snmp-devel")
def _(self):
    return self.default_devel()

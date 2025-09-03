pkgname = "net-snmp"
pkgver = "5.9.4"
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
configure_gen = []
make_check_target = "test"
hostmakedepends = [
    "file",
    "linux-headers",
    "pkgconf",
]
makedepends = ["dinit-chimera", "openssl3-devel"]
checkdepends = ["iproute2"]
pkgdesc = "Simple Network Management Protocol"
license = "BSD-3-Clause"
url = "http://www.net-snmp.org"
source = f"https://sourceforge.net/projects/{pkgname}/files/{pkgname}/{pkgver}/net-snmp-{pkgver}.tar.gz"
sha256 = "8b4de01391e74e3c7014beb43961a2d6d6fa03acc34280b9585f4930745b0544"
options = ["!parallel"]


def post_install(self):
    self.install_license("COPYING")
    self.uninstall("usr/lib/libsnmp*", glob=True)
    self.install_file(
        "build/EXAMPLE.conf", "usr/lib/net-snmp", name="snmpd.conf"
    )
    self.install_file(self.files_path / "snmptrapd.conf", "usr/lib/net-snmp")
    self.install_service(self.files_path / "snmpd")
    self.install_service(self.files_path / "snmptrapd")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")


@subpackage("net-snmp-snmpd")
def _(self):
    self.pkgdesc = "Simple Network Management Protocol daemon"
    self.depends = [f"net-snmp~{pkgver}"]

    return [
        "usr/bin/net-snmp-create-v3-user",
        "usr/bin/snmpd",
        "usr/lib/dinit.d/snmpd",
        "usr/lib/net-snmp/snmpd.conf",
    ]


@subpackage("net-snmp-snmptrapd")
def _(self):
    self.pkgdesc = "Simple Network Management Protocol notification receiver"
    self.depends = [f"net-snmp~{pkgver}"]

    return [
        "usr/bin/snmptrapd",
        "usr/lib/dinit.d/snmptrapd",
        "usr/lib/net-snmp/snmptrapd.conf",
    ]


@subpackage("net-snmp-devel")
def _(self):
    return self.default_devel()

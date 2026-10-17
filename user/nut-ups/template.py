pkgname = "nut-ups"
pkgver = "2.8.5"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--with-confdir=/etc/ups",
    "--with-doc=man",
    "--disable-static",
    "--datadir=/usr/share/ups",
    "--with-user=_nut",
    "--with-group=_nut",
    "--with-ssl",
    "--with-usb",
    "--with-dev",
    "--with-serial",
    "--with-avahi",
    "--with-udev-dir=/usr/lib/udev",
    "--prefix=/usr",
    "--exec-prefix=/usr",
    "--sbindir=/usr/bin",
    "--libexecdir=/usr/lib",
    "--mandir=/usr/share/man",
    "--with-confdir-examples=/usr/share/examples/ups",
    "--with-libltdl",
    "--without-ipmi",
    "--without-freeipmi",
    "--without-systemdsystemunitdir",
    "--without-snmp",
    "--with-drvpath=/usr/lib/nut",
    "--without-cgi",
    "--enable-docs-changelog=no",
    "--with-statepath=/run/ups",
    "--with-altpidpath=/run/ups",
    "--with-pidpath=/run/ups",
    "--with-powerdownflag=/run/ups/killpower",
    "--with-pynut=no",
]
hostmakedepends = ["asciidoc", "pkgconf"]
makedepends = [
    "avahi-devel",
    "dinit-chimera",
    "libtool-devel",
    "libusb-devel",
    "neon-devel",
    "openssl3-devel",
]
pkgdesc = "Tools for working with power supplies"
license = "GPL-2.0-or-later AND GPL-3.0-or-later"
url = "https://www.networkupstools.org"
source = f"https://github.com/networkupstools/nut/releases/download/v{pkgver}/nut-{pkgver}.tar.gz"
sha256 = "18bf32e59eb764b13da3c4fa70384926d7fa584cb31d2fe7f137a570633eeec1"
# check fails on man page sanity check
options = ["!check"]


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    # service files
    self.install_service(self.files_path / "upsd")
    self.install_service(self.files_path / "upsmon")
    self.install_service(self.files_path / "ups-dev")
    self.install_service(self.files_path / "ups-rundir")


@subpackage("nut-ups-devel")
def _(self):
    return self.default_devel()


@subpackage("nut-ups-libs")
def _(self):
    return self.default_libs()

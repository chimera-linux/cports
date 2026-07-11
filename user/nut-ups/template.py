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
    "--with-powerdownflag=/run/ups",
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
options = ["etcfiles", "!check"]


def post_install(self):
    self.install_license("LICENSE-GPL2")
    self.install_license("LICENSE-GPL3")
    self.install_sysusers("^/sysusers.conf")
    self.install_tmpfiles("^/tmpfiles.conf")
    # service files
    self.install_service("^/upsd")
    self.install_service("^/upsmon")
    self.install_service("^/ups-dev")
    self.install_service("^/ups-rundir")
    # rename config files
    self.rename("etc/ups/nut.conf.sample", "nut.conf")
    self.rename("etc/ups/ups.conf.sample", "ups.conf")
    self.rename("etc/ups/upsd.conf.sample", "upsd.conf")
    self.rename("etc/ups/upsd.users.sample", "upsd.users")
    self.rename("etc/ups/upsmon.conf.sample", "upsmon.conf")
    self.rename("etc/ups/upssched.conf.sample", "upssched.conf")


@subpackage("nut-devel")
def _(self):
    return self.default_devel()

pkgname = "hplip"
pkgver = "3.23.12"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--disable-doc-build",
    "--disable-fax-build",
    "--disable-gui-build",
    "--disable-imageProcessor-build",
    # net-snmp
    "--disable-network-build",
    "--enable-cups-drv-install",
    "--enable-cups-ppd-install",
]
make_dir = "."
# libtool relink is racy..
make_install_args = ["-j1"]
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "python-devel",
]
makedepends = [
    "cups-devel",
    "dbus-devel",
    "libjpeg-turbo-devel",
    "libusb-devel",
    "python-devel",
    "sane-backends-devel",
]
depends = ["python"]
pkgdesc = "Drivers for HP printers"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-only AND BSD-3-Clause AND MIT"
url = "https://developers.hp.com/hp-linux-imaging-and-printing"
source = f"https://downloads.sourceforge.net/hplip/hplip-{pkgver}.tar.gz"
sha256 = "a76c2ac8deb31ddb5f0da31398d25ac57440928a0692dcb060a48daa718e69ed"
# nuh uh
hardening = ["!vis"]
# TODO: probably ignores CC
options = ["!cross"]

tool_flags = {"CFLAGS": ["-D_GNU_SOURCE"]}


def post_extract(self):
    # the reconf fails because these files are "required"; just quickly make them all
    for f in ["NEWS", "README", "AUTHORS", "ChangeLog", "INSTALL"]:
        (self.cwd / f).touch()


def post_install(self):
    from cbuild.util import python

    python.precompile(self, "usr/share/hplip")

    dd = self.destdir
    self.install_license("COPYING")
    self.rm(dd / "usr/lib/systemd", recursive=True)
    # rename default dll.conf that conflicts with sane-backends to own name,
    # loads hpaio
    self.install_dir("etc/sane.d/dll.d")
    self.mv(dd / "etc/sane.d/dll.conf", dd / "etc/sane.d/dll.d/hpaio")
    self.mv(dd / "etc/udev", dd / "usr/lib")

    # move elfs to libexec
    self.install_dir("usr/libexec/hplip")
    for f in ["locatedriver", "dat2drv"]:
        self.mv(dd / "usr/share/hplip" / f, dd / "usr/libexec/hplip")
        self.install_link(f"../../libexec/hplip/{f}", f"usr/share/hplip/{f}")

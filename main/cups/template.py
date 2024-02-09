pkgname = "cups"
pkgver = "2.4.7"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--enable-relro",
    "--enable-acl",
    "--enable-dbus",
    "--enable-libpaper",
    "--enable-pam",
    "--enable-raw-printing",
    "--disable-gssapi",
    "--without-rcdir",
    "--without-systemd",
    "--with-tls=openssl",
    "--with-dnssd=avahi",
    "--with-rundir=/run/cups",
    "--with-logdir=/var/log/cups",
    "--with-docdir=/usr/share/cups/doc",
    "--with-menudir=/usr/share/applications",
    "--with-xinetd=/etc/xinetd.d",
    "--with-cups-user=_cups",
    "--with-cups-group=lp",
    "--with-system-groups=_lpadmin sys root",
]
configure_gen = []
# build system is bad
make_dir = "."
make_check_args = ["-j1"]
hostmakedepends = [
    "avahi-devel",
    "openssl-devel",
    "pkgconf",
    "xdg-utils",
]
makedepends = [
    "acl-devel",
    "avahi-devel",
    "libpaper-devel",
    "libpng-devel",
    "libtiff-devel",
    "libusb-devel",
    "linux-headers",
    "linux-pam-devel",
    "openssl-devel",
]
depends = ["xdg-utils"]
pkgdesc = "Common Unix Printing System"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/OpenPrinting/cups"
source = f"{url}/releases/download/v{pkgver}/{pkgname}-{pkgver}-source.tar.gz"
sha256 = "dd54228dd903526428ce7e37961afaed230ad310788141da75cebaa08362cf6c"
# build system is bad
tool_flags = {
    "CFLAGS": ["-Wno-unused-command-line-argument"],
    "CXXFLAGS": ["-Wno-unused-command-line-argument"],
}
file_modes = {
    "etc/cups/classes.conf": ("root", "lp", 0o644),
    "etc/cups/printers.conf": ("root", "lp", 0o644),
    "etc/cups/subscriptions.conf": ("root", "lp", 0o644),
    "etc/cups/cups-files.conf": ("root", "lp", 0o640),
    "etc/cups/cups-files.conf.default": ("root", "lp", 0o640),
    "etc/cups/cupsd.conf": ("root", "lp", 0o640),
    "etc/cups/cupsd.conf.default": ("root", "lp", 0o640),
    "etc/cups/snmp.conf": ("root", "lp", 0o640),
    "etc/cups/snmp.conf.default": ("root", "lp", 0o640),
}
# FIXME int
hardening = ["!int"]
# undefined references everywhere
options = ["!lto"]


def init_configure(self):
    # build system is bad
    self.configure_args += [
        "--with-optim="
        + self.get_cflags(shell=True)
        + " "
        + self.get_ldflags(shell=True)
    ]


def post_install(self):
    self.install_file(self.files_path / "client.conf", "etc/cups")

    self.install_service(self.files_path / "cupsd")

    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="cups.conf",
    )
    self.install_file(
        self.files_path / "tmpfiles.conf",
        "usr/lib/tmpfiles.d",
        name="cups.conf",
    )

    # install some more configuration files that will get filled by cupsd
    for f in ["printers", "classes", "subscriptions"]:
        (self.destdir / f"etc/cups/{f}.conf").touch(mode=0o644)


@subpackage("cups-libs")
def _libs(self):
    self.file_modes = {"etc/cups/client.conf": ("root", "lp", 0o644)}

    return self.default_libs(
        extra=[
            "etc/cups/client.conf",
            "usr/share/man/man5/client.conf.5",
        ]
    )


@subpackage("cups-devel")
def _devel(self):
    self.depends += ["zlib-devel"]

    return self.default_devel()

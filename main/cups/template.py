pkgname = "cups"
pkgver = "2.4.12"
pkgrel = 0
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
    "--with-dbusdir=/usr/share/dbus-1",
    "--with-rundir=/run/cups",
    "--with-logdir=/var/log/cups",
    "--with-docdir=/usr/share/cups/doc",
    "--with-menudir=/usr/share/applications",
    "--with-xinetd=/etc/xinetd.d",
    "--with-cups-user=_cups",
    "--with-cups-group=lp",
    "--with-system-groups=_lpadmin root",
]
configure_gen = []
# build system is bad
make_dir = "."
make_check_args = ["-j1"]
hostmakedepends = [
    "avahi-bootstrap",
    "openssl3-devel",
    "pkgconf",
    "xdg-utils",
]
makedepends = [
    "acl-devel",
    "avahi-bootstrap",
    "dbus-devel",
    "dinit-chimera",
    "libpaper-devel",
    "libpng-devel",
    "libtiff-devel",
    "libusb-devel",
    "linux-headers",
    "linux-pam-devel",
    "openssl3-devel",
]
depends = ["xdg-utils"]
pkgdesc = "Common Unix Printing System"
license = "Apache-2.0"
url = "https://github.com/OpenPrinting/cups"
source = f"{url}/releases/download/v{pkgver}/cups-{pkgver}-source.tar.gz"
sha256 = "b1dde191a4ae2760c47220c82ca6155a28c382701e6c1a0159d1054990231d59"
# build system is bad
tool_flags = {
    "CFLAGS": ["-Wno-unused-command-line-argument"],
    "CXXFLAGS": ["-Wno-unused-command-line-argument"],
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
    self.install_file(self.files_path / "client.conf.default", "usr/share/cups")

    self.install_service(self.files_path / "cupsd")

    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_tmpfiles(
        self.files_path / "tmpfiles-client.conf", name="cups-client"
    )

    # move the default configs
    for f in (self.destdir / "etc/cups").rglob("*.default"):
        self.install_file(f, "usr/share/cups", mode=0o644)

    # and nuke the /etc stuff
    self.uninstall("etc/cups")

    # we don't have xinetd
    self.uninstall("etc/xinetd.d")


@subpackage("cups-libs")
def _(self):
    return self.default_libs(
        extra=[
            "usr/lib/tmpfiles.d/cups-client.conf",
            "usr/share/cups/client.conf.default",
            "usr/share/man/man5/client.conf.5",
        ]
    )


@subpackage("cups-devel")
def _(self):
    self.depends += ["zlib-ng-compat-devel"]

    return self.default_devel()

pkgname = "nyagetty"
pkgver = "2.38.99"
pkgrel = 1
build_style = "meson"
hostmakedepends = ["meson"]
makedepends = ["linux-headers"]
depends = ["virtual:cmd:login!shadow"]
pkgdesc = "Standalone util-linux agetty"
maintainer = "q66 <q66@chimera-linux.org>"
license = "0BSD"
url = "https://github.com/chimera-linux/nyagetty"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7033d6840f839a6ad6d788d92f45efd0bb10c835c0560dba5d15ad8a6b9dff90"
hardening = ["vis", "cfi"]

# sync securetty in base-files with this when updating
_ttys = [
    # /dev/console
    ("console", None),
    # graphical terminals
    ("tty1", None),
    ("tty2", None),
    ("tty3", None),
    ("tty4", None),
    ("tty5", None),
    ("tty6", None),
    ("tty7", None),
    ("tty8", None),
    # generic serial
    ("ttyS0", True),
    ("ttyS1", True),
    ("ttyS2", True),
    ("ttyS3", True),
    # usb serial
    ("ttyUSB0", True),
    ("ttyUSB1", True),
    # various serial
    ("ttyAMA0", True),
    ("ttyAMA1", True),
    ("ttySIF0", True),
    ("ttySIF1", True),
    ("ttymxc0", True),
    ("ttymxc1", True),
    ("ttymxc2", True),
    ("ttymxc3", True),
    # ibm/xen terminals
    ("hvc0", 38400),
    ("hvc1", 38400),
    ("hvsi0", 19200),
    ("hvsi1", 19200),
]


def post_install(self):
    # agetty dinit helper
    self.install_file(
        self.files_path / "dinit-agetty", "usr/libexec", mode=0o755
    )
    # agetty conf wrapper
    self.install_file(
        self.files_path / "agetty-default", "usr/libexec", mode=0o755
    )
    self.install_file(
        self.files_path / "agetty-serial", "usr/libexec", mode=0o755
    )
    # core service
    self.install_service(self.files_path / "agetty", enable=True)
    # generate services for individual gettys
    for name, baud in _ttys:
        svpath = self.destdir / f"etc/dinit.d/agetty-{name}"
        with open(svpath, "w") as sv:
            if baud is None:
                cmd = f"agetty-default {name}"
            elif baud is True:
                cmd = f"agetty-serial {name}"
            else:
                cmd = f"agetty-serial {name} {baud}"
            sv.write(
                f"""# agetty service for {name}
type            = process
command         = /usr/libexec/{cmd}
restart         = true
depends-on      = login.target
termsignal      = HUP
restart         = true
smooth-recovery = true
inittab-id      = {name.removeprefix('tty')}
inittab-line    = {name}
"""
            )
        svpath.chmod(0o644)


@subpackage("nyagetty-dinit")
def _dinit(self):
    self.pkgdesc = f"{pkgdesc} (service files)"

    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}", "dinit-chimera"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "dinit-chimera"]

    return ["etc/dinit.d/agetty*", "usr/libexec/dinit-agetty"]

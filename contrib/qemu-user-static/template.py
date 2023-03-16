import os

pkgname = "qemu-user-static"
pkgver = "7.2.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-linux-user",
    "--disable-system",
    "--static"
]
make_cmd = "gmake"
hostmakedepends = ["python", "ninja", "pkgconf", "bzip2", "gmake", "bash", "perl", "ugetopt"]
makedepends = [
    "glib-devel", "libbz2-devel", "linux-headers", "nss-devel", "libaio-devel",
    "gnutls-devel", "dtc-devel", "libunwind-devel-static"
]
pkgdesc = "Generic and open source machine emulator (statically built user mode)"
maintainer = "eater <=@eater.me>"
license = "GPL-2.0 AND (BSD-3-Clause OR MIT)"
url = "https://qemu.org"
source = f"https://download.qemu.org/qemu-{pkgver}.tar.xz"
sha256 = "5b49ce2687744dad494ae90a898c52204a3406e84d072482a1e1be854eeb2157"
exec_wrappers = [("/usr/bin/ugetopt", "getopt")]


def post_install(self):
    # usr/share has some stuff we don't want
    self.rm(self.destdir / "usr/share", recursive=True)
    # script expects folder to be there
    self.mkdir(self.destdir / "usr/share/binfmts", parents=True)
    self.do(self.chroot_cwd / "scripts/qemu-binfmt-conf.sh",
            "--debian",
            "--qemu-suffix", "-static",
            "--qemu-path", "/usr/bin",
            "--exportdir", self.chroot_destdir / "usr/share/binfmts",
            # preserve
            "--preserve-argv0", "yes",
            # fix_binary
            "--persistent", "yes",
            # credentials
            "--credential", "yes")

    # suffix all qemu binaries with -static
    for item in os.listdir(self.destdir / "usr/bin"):
        if item.startswith("qemu-"):
            self.mv(self.destdir / "usr/bin" / item, self.destdir / "usr/bin" / f"{item}-static")


@subpackage("qemu-user-static-binfmt")
def _binfmt(self):
    self.install_if = [f"qemu-user-static={pkgver}-r{pkgrel}", "binfmt-support"]
    self.depends += [f"qemu-user-static={pkgver}-r{pkgrel}", "binfmt-support", "!qemu-binfmt"]
    self.pkgdesc += " (binfmt support)"
    return ["usr/share/binfmts"]

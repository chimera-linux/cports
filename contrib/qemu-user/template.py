pkgname = "qemu-user"
pkgver = "8.0.0"
pkgrel = 0
build_style = "gnu_configure"
# TODO vde liburing libssh capstone
configure_args = [
    "--enable-linux-user",
    "--disable-bsd-user",
    "--disable-kvm",
    "--disable-png",
    "--disable-fdt",
    "--disable-virtfs",
    "--disable-seccomp",
    "--disable-system",
    "--static",
]
make_cmd = "gmake"
hostmakedepends = [
    "meson", "ninja", "pkgconf", "gmake", "bash", "perl", "flex", "bison",
    "bzip2", "ugetopt",
]
makedepends = [
    "glib-devel-static", "zlib-devel-static", "libcxx-devel-static",
    "pcre2-devel-static", "libunwind-devel-static", "musl-devel-static",
    "libatomic-chimera-devel-static", "linux-headers",
]
pkgdesc = "QEMU user mode emulators"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND LGPL-2.1-only"
url = "https://qemu.org"
source = f"https://download.qemu.org/qemu-{pkgver}.tar.xz"
sha256 = "bb60f0341531181d6cc3969dd19a013d0427a87f918193970d9adb91131e56d0"
# maybe someday
options = ["!cross", "!check"]
exec_wrappers = [("/usr/bin/ugetopt", "getopt")]

def post_install(self):
    self.rm(self.destdir / "usr/share", recursive = True)
    self.install_dir("usr/lib/binfmt.d")

    self.do(
        "scripts/qemu-binfmt-conf.sh", "--systemd", "ALL",
        "--exportdir", self.chroot_destdir / "usr/lib/binfmt.d",
        "--qemu-path", "/usr/bin",
        "--preserve-argv0", "yes",
        "--persistent", "yes",
        "--credential", "yes",
    )

def _upkg(uname):
    @subpackage(f"qemu-user-{uname}")
    def _u(self):
        self.pkgdesc = f"{pkgdesc} ({uname})"
        self.install_if = [f"qemu-user={pkgver}-r{pkgrel}"]

        return [f"usr/bin/qemu-{uname}"]

    match uname:
        case "cris" | "nios2":
            # no binfmt support
            return

    do_pkg = True
    curarch = self.profile().arch
    if uname == curarch:
        do_pkg = False
    elif curarch == "x86_64" and uname == "i386":
        do_pkg = False

    # binfmt package is not generated for current arch
    @subpackage(f"qemu-user-{uname}-binfmt", do_pkg)
    def _binfmt(self):
        self.pkgdesc = f"{pkgdesc} ({uname} binfmt)"
        self.install_if = [f"qemu-user-{uname}={pkgver}-r{pkgrel}"]

        extra = []

        match uname:
            case "i386":
                extra = [
                    f"usr/lib/binfmt.d/qemu-i486.conf"
                ]

        return [f"usr/lib/binfmt.d/qemu-{uname}.conf"] + extra

for _u in [
    "aarch64", "aarch64_be", "alpha", "arm", "armeb", "cris", "hexagon",
    "hppa", "i386", "loongarch64", "m68k", "microblaze", "microblazeel",
    "mips", "mips64", "mips64el", "mipsel", "mipsn32", "mipsn32el", "nios2",
    "or1k", "ppc", "ppc64", "ppc64le", "riscv32", "riscv64", "s390x", "sh4",
    "sh4eb", "sparc", "sparc32plus", "sparc64", "x86_64", "xtensa", "xtensaeb",
]:
    _upkg(_u)

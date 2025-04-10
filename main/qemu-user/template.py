pkgname = "qemu-user"
pkgver = "9.2.3"
pkgrel = 0
build_style = "gnu_configure"
# TODO vde libssh capstone
configure_args = [
    "--enable-linux-io-uring",
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
# actually meson
configure_gen = []
hostmakedepends = [
    "bash",
    "bison",
    "bzip2",
    "flex",
    "meson",
    "ninja",
    "perl",
    "pkgconf",
    "ugetopt",
]
makedepends = [
    "glib-devel",
    "glib-devel-static",
    "libatomic-chimera-devel-static",
    "libcxx-devel-static",
    "libdrm-devel",
    "libunwind-devel-static",
    "liburing-devel-static",
    "linux-headers",
    "musl-devel-static",
    "pcre2-devel",
    "pcre2-devel-static",
    "zlib-ng-compat-devel",
    "zlib-ng-compat-devel-static",
]
pkgdesc = "QEMU user mode emulators"
license = "GPL-2.0-only AND LGPL-2.1-only"
url = "https://qemu.org"
source = f"https://download.qemu.org/qemu-{pkgver}.tar.xz"
sha256 = "baed494270c361bf69816acc84512e3efed71c7a23f76691642b80bc3de7693e"
# maybe someday
options = ["!cross", "!check", "empty"]
exec_wrappers = [("/usr/bin/ugetopt", "getopt")]


def init_configure(self):
    ljobs = 4 if self.make_jobs >= 4 else self.make_jobs
    # qemu links a lot of big exes at once so ensure there is not more than four
    self.configure_args += [f"-Dbackend_max_links={ljobs}"]


def post_install(self):
    self.uninstall("usr/share")
    self.install_dir("usr/lib/binfmt.d")

    self.do(
        "scripts/qemu-binfmt-conf.sh",
        "--systemd",
        "ALL",
        "--exportdir",
        self.chroot_destdir / "usr/lib/binfmt.d",
        "--qemu-path",
        "/usr/bin",
        "--preserve-argv0",
        "yes",
        "--persistent",
        "yes",
        "--credential",
        "yes",
    )


_skip_32bit = {
    "i386": "x86_64",
    "aarch64": "arm",
    "arm": "aarch64",
    "ppc": "ppc64",
    "ppc64": "ppc",
    "ppcle": "ppc64le",
    "riscv32": "riscv64",
}


def _upkg(uname):
    @subpackage(f"qemu-user-{uname}")
    def _(self):
        self.subdesc = uname
        self.install_if = [self.parent]

        return [f"usr/bin/qemu-{uname}"]

    do_pkg = True

    match self.profile().arch:
        case "armv7":
            curarch = "arm"
        case arch:
            curarch = arch

    if uname == curarch:
        do_pkg = False
    elif uname in _skip_32bit and _skip_32bit[uname] == curarch:
        do_pkg = False

    # binfmt package is not generated for current arch
    @subpackage(f"qemu-user-{uname}-binfmt", do_pkg)
    def _(self):
        self.subdesc = f"{uname} binfmt"
        self.install_if = [self.with_pkgver(f"qemu-user-{uname}")]
        self.depends = [self.with_pkgver(f"qemu-user-{uname}")]

        extra = []

        match uname:
            case "i386":
                extra = ["usr/lib/binfmt.d/qemu-i486.conf"]

        return [f"usr/lib/binfmt.d/qemu-{uname}.conf", *extra]


for _u in [
    "aarch64",
    "aarch64_be",
    "alpha",
    "arm",
    "armeb",
    "hexagon",
    "hppa",
    "i386",
    "loongarch64",
    "m68k",
    "microblaze",
    "microblazeel",
    "mips",
    "mips64",
    "mips64el",
    "mipsel",
    "mipsn32",
    "mipsn32el",
    "or1k",
    "ppc",
    "ppc64",
    "ppc64le",
    "riscv32",
    "riscv64",
    "s390x",
    "sh4",
    "sh4eb",
    "sparc",
    "sparc32plus",
    "sparc64",
    "x86_64",
    "xtensa",
    "xtensaeb",
]:
    _upkg(_u)

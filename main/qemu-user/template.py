pkgname = "qemu-user"
pkgver = "10.1.2"
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
sha256 = "9d75f331c1a5cb9b6eb8fd9f64f563ec2eab346c822cb97f8b35cd82d3f11479"
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

    # drop binfmts with no corresponding emulator
    for x in (self.destdir / "usr/lib/binfmt.d").iterdir():
        name = x.name.removesuffix(".conf")
        # we need to match this
        if name == "qemu-i486":
            name = "qemu-i386"
        if not (self.destdir / "usr/bin" / name).is_file():
            x.unlink()


_skip_32bit = {
    "i386": "x86_64",
    "arm": "aarch64",
    "ppc": "ppc64",
    "ppcle": "ppc64le",
    "riscv32": "riscv64",
}


def _upkg(uname, wordsize):
    do_epkg = True

    if self.profile().wordsize == 32 and wordsize == 64:
        do_epkg = False

    @subpackage(f"qemu-user-{uname}", do_epkg)
    def _(self):
        self.subdesc = uname
        self.install_if = [self.parent]

        return [f"usr/bin/qemu-{uname}"]

    do_bpkg = do_epkg

    match self.profile().arch:
        case "armv7":
            curarch = "arm"
        case arch:
            curarch = arch

    if uname == curarch:
        do_bpkg = False
    elif uname in _skip_32bit and _skip_32bit[uname] == curarch:
        do_bpkg = False

    # binfmt package is not generated for current arch
    @subpackage(f"qemu-user-{uname}-binfmt", do_bpkg)
    def _(self):
        self.subdesc = f"{uname} binfmt"
        self.install_if = [self.with_pkgver(f"qemu-user-{uname}")]
        self.depends = [self.with_pkgver(f"qemu-user-{uname}")]

        extra = []

        match uname:
            case "i386":
                extra = ["usr/lib/binfmt.d/qemu-i486.conf"]

        return [f"usr/lib/binfmt.d/qemu-{uname}.conf", *extra]


for _u, _w in [
    ("aarch64", 64),
    ("aarch64_be", 64),
    ("alpha", 64),
    ("arm", 32),
    ("armeb", 32),
    ("hexagon", 32),
    ("hppa", 64),
    ("i386", 32),
    ("loongarch64", 64),
    ("m68k", 32),
    ("microblaze", 32),
    ("microblazeel", 32),
    ("mips", 32),
    ("mips64", 64),
    ("mips64el", 64),
    ("mipsel", 32),
    ("mipsn32", 64),
    ("mipsn32el", 64),
    ("or1k", 32),
    ("ppc", 32),
    ("ppc64", 64),
    ("ppc64le", 64),
    ("riscv32", 32),
    ("riscv64", 64),
    ("s390x", 64),
    ("sh4", 32),
    ("sh4eb", 32),
    ("sparc", 32),
    ("sparc32plus", 64),
    ("sparc64", 64),
    ("x86_64", 64),
    ("xtensa", 32),
    ("xtensaeb", 32),
]:
    _upkg(_u, _w)

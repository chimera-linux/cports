pkgname = "grub"
pkgver = "2.12"
pkgrel = 2
configure_args = [
    "--sysconfdir=/etc",
    "--prefix=/usr",
    "--libdir=/usr/lib",
    "--sbindir=/usr/bin",
    "--disable-werror",
    "--enable-device-mapper",
    "--enable-cache-stats",
    "--enable-nls",
    "--enable-grub-mkfont",
    "--enable-grub-mount",
    "AWK=gawk",
]
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "binutils",
    "bison",
    "flex",
    "font-unifont-bdf",
    "gawk",
    "gettext",
    "help2man",
    "libtool",
    "pkgconf",
    "python",
]
makedepends = [
    "freetype-devel",
    "fuse-devel",
    "gettext-devel",
    "lvm2-devel",
    "ncurses-devel",
    "xz-devel",
]
depends = ["os-prober", "cmd:findmnt!util-linux-mount"]
pkgdesc = "GRand Unified Bootloader version 2"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/grub"
source = f"$(GNU_SITE)/grub/grub-{pkgver}.tar.xz"
sha256 = "f3c97391f7c4eaa677a78e090c7e97e6dc47b16f655f04683ebd37bef7fe0faa"
# our strip wrapper prevents correct kernel.img generation
env = {"CBUILD_BYPASS_STRIP_WRAPPER": "1"}
# the freestanding bits
nopie_files = ["usr/lib/grub/*"]
# single completion file for multiple commands
options = ["!lintcomp"]

if self.profile().arch == "loongarch64":
    broken = "causes a machine exception at runtime"

_tpl = self.profile().triplet
exec_wrappers = [
    (f"/usr/bin/{_tpl}-ld.bfd", f"{_tpl}-ld"),
    ("/usr/bin/ld.bfd", "ld"),
]
tools = {"LD": f"{_tpl}-ld.bfd"}
# fool the build system into using binutils for these tools
for _tool in ["objcopy", "strip", "ar", "ranlib", "nm"]:
    exec_wrappers += [
        (f"/usr/bin/{_tpl}-g{_tool}", f"{_tpl}-{_tool}"),
    ]
    tools[_tool.upper()] = f"{_tpl}-g{_tool}"

# this should be a list of tuples:
# (arch, platform, cflags, ldflags, platform_name)
_platforms = [
    # the default build is BIOS, we also want EFI
    # (32 and 64 bit) as well as coreboot and Xen
    ("i386", "pc", "", "", "x86 PC/BIOS"),
    ("i386", "efi", "", "", "x86 EFI"),
    ("i386", "coreboot", "", "", "x86 coreboot"),
    ("x86_64", "efi", "", "", "x86_64 EFI"),
    ("x86_64", "xen", "", "", "x86_64 Xen"),
    ("powerpc", "ieee1275", "-mno-altivec", "", "PowerPC OpenFirmware"),
    ("arm64", "efi", "", "", "Aarch64 EFI"),
    ("loongarch64", "efi", "", "", "LoongArch64 EFI"),
    # relaxation causes R_RISCV_ALIGN
    ("riscv64", "efi", "-mno-relax", "-mno-relax", "64-bit RISC-V EFI"),
]

match self.profile().arch:
    case "x86_64":
        _archs = ["i386", "x86_64"]
    case "ppc64le" | "ppc64" | "ppc":
        _archs = ["powerpc"]
    case "aarch64":
        _archs = ["arm64"]
    case "riscv64":
        _archs = ["riscv64"]
        # otherwise crashes llvm backend (unsupported code model for lowering)
        configure_args += ["grub_cv_cc_mcmodel=no"]
    case "loongarch64":
        _archs = ["loongarch64"]
    case _:
        _archs = []
        broken = f"Unsupported platform ({self.profile().arch})"


def init_configure(self):
    # configure tests, sigh
    self.tools[
        "CC"
    ] += " --start-no-unused-arguments -fuse-ld=bfd --end-no-unused-arguments"
    self.env["TARGET_CC"] = self.tools["CC"]


def configure(self):
    # reconfigure the autotools
    self.do("autoreconf", "-if")
    # configure tools build
    self.mkdir("build")
    self.do(
        self.chroot_cwd / "configure",
        f"--host={self.profile().triplet}",
        "--with-platform=none",
        *configure_args,
        wrksrc="build",
    )
    # platforms build
    for arch, platform, ecfl, ldfl, desc in _platforms:
        if arch not in _archs:
            continue
        ldfl += " -fuse-ld=bfd"
        bdir = f"build_{arch}_{platform}"
        self.mkdir(bdir)
        cfl = "-fno-stack-protector " + ecfl
        # configure freestanding; rename arm64 as a special case
        if arch == "arm64":
            arch = "aarch64"
        self.do(
            self.chroot_cwd / "configure",
            f"--host={self.profile().triplet}",
            f"--target={arch}",
            f"--with-platform={platform}",
            "--disable-efiemu",
            *configure_args,
            wrksrc=bdir,
            env={
                "BUILD_CFLAGS": cfl,
                "BUILD_LDFLAGS": ldfl,
                "CFLAGS": cfl,
                "LDFLAGS": ldfl,
                "TARGET_OBJCOPY": "llvm-objcopy",
                "TARGET_RANLIB": "llvm-ranlib",
                "TARGET_STRIP": "llvm-strip",
                "TARGET_NM": "llvm-nm",
                "MAKE": "make",
            },
        )


def build(self):
    # primary build
    self.do("make", "-C", "build", f"-j{self.make_jobs}")
    # extra targets
    for arch, platform, cfl, ldfl, desc in _platforms:
        if arch not in _archs:
            continue
        self.do("make", "-C", f"build_{arch}_{platform}", f"-j{self.make_jobs}")


def install(self):
    ddir = self.chroot_destdir
    # populate extra targets first
    for arch, platform, cfl, ldfl, desc in _platforms:
        if arch not in _archs:
            continue
        bdir = f"build_{arch}_{platform}"
        # full install
        self.do("make", "-C", bdir, "install", f"DESTDIR={ddir}")
        # remove stuff that is not platform specific
        for d in ["etc", "usr/share", "usr/bin"]:
            self.uninstall(d)
    # install tools last
    self.do("make", "-C", "build", "install", f"DESTDIR={ddir}")


def post_install(self):
    # kernel hook
    self.install_file(
        self.files_path / "99-grub.sh", "usr/lib/kernel.d", mode=0o755
    )
    # conf file
    self.install_file(
        self.files_path / "grub.default", "etc/default", name="grub"
    )
    # update-grub
    self.install_bin(self.files_path / "update-grub")
    # move completions
    self.rename(
        "etc/bash_completion.d",
        "usr/share/bash-completion/completions",
        relative=False,
    )
    # unused tools
    self.uninstall("usr/bin/grub-ofpathname")
    self.uninstall("usr/bin/grub-sparc64-setup")


@subpackage("grub-utils")
def _(self):
    self.subdesc = "additional utilities"
    self.depends = [self.parent]

    return [
        "usr/bin/grub-menulst2cfg",
        "usr/bin/grub-fstest",
        "usr/bin/grub-mkfont",
    ]


def _genplatform(arch, platform, desc):
    @subpackage(f"grub-{arch}-{platform}-dbg", arch in _archs)
    def _(self):
        self.subdesc = f"{desc} debug files"
        self.depends = [self.with_pkgver(f"grub-{arch}-{platform}")]
        self.options = ["!strip", "foreignelf", "execstack"]

        def _install():
            self.take(f"usr/lib/grub/{arch}-{platform}/*.module")
            self.take(
                f"usr/lib/grub/{arch}-{platform}/*.image", missing_ok=True
            )
            self.take(f"usr/lib/grub/{arch}-{platform}/*.exec", missing_ok=True)

        return _install

    @subpackage(f"grub-{arch}-{platform}", arch in _archs)
    def _(self):
        self.subdesc = f"{desc} support"
        self.depends = [self.parent]
        self.options = ["!strip", "foreignelf", "execstack"]

        if platform == "efi":
            self.depends += ["efibootmgr", "dosfstools"]
        elif platform == "ieee1275":
            self.depends += ["powerpc-utils"]

        return [f"usr/lib/grub/{arch}-{platform}"]


# generate platform subpackages
for _arch, _platform, _cfl, _ldfl, _desc in _platforms:
    _genplatform(_arch, _platform, _desc)

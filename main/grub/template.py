pkgname = "grub"
pkgver = "2.06"
pkgrel = 0
configure_args = [
    "--sysconfdir=/etc", "--prefix=/usr", "--libdir=/usr/lib",
    "--sbindir=/usr/bin", "--disable-werror", "--enable-device-mapper",
    "--enable-cache-stats", "--enable-nls", "--enable-grub-mkfont",
    "--enable-grub-mount",
]
make_cmd = "gmake"
# our strip wrapper prevents correct kernel.img generation
make_install_env = {"CBUILD_BYPASS_STRIP_WRAPPER": "1"}
hostmakedepends = [
    "gmake", "pkgconf", "flex", "bison", "help2man", "python",
    "gettext-tiny", "font-unifont-bdf", f"binutils-{self.profile().arch}",
]
makedepends = [
    "gettext-tiny-devel", "freetype-devel", "ncurses-devel", "liblzma-devel",
    "device-mapper-devel", "fuse-devel",
]
depends = ["os-prober"]
pkgdesc = "GRand Unified Bootloader version 2"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/grub"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "b79ea44af91b93d17cd3fe80bdae6ed43770678a9a5ae192ccea803ebb657ee1"
# the freestanding bits
nopie_files = ["usr/lib/grub/*"]

exec_wrappers = []
# fool the build system into using binutils for these tools
for tool in ["objcopy", "strip", "ar", "ranlib", "nm"]:
    tpl = self.profile().triplet
    exec_wrappers += [
        (f"/usr/bin/{tpl}-g{tool}", f"{tpl}-{tool}"),
    ]

# this should be a list of tuples:
# (arch, platform, cflags, ldflags, platform_name)
_platforms = []

match self.profile().arch:
    case "x86_64":
        # the default build is BIOS, we also want EFI
        # (32 and 64 bit) as well as coreboot and Xen
        _platforms = [
            # need bfd linker for x86/BIOS to get 512 byte first-stage images
            ("i386", "pc", "-fuse-ld=bfd", "-fuse-ld=bfd", "x86 PC/BIOS"),
            ("i386", "efi", "", "", "x86 EFI"),
            ("i386", "coreboot", "", "", "x86 coreboot"),
            ("x86_64", "efi", "", "", "x86_64 EFI"),
            ("x86_64", "xen", "", "", "x86_64 Xen"),
        ]
    case "ppc64le" | "ppc64":
        _platforms = [
            ("powerpc", "ieee1275", "-mno-altivec", "", "PowerPC OpenFirmware"),
        ]
    case "aarch64":
        _platforms = [
            ("arm64", "efi", "", "", "Aarch64 EFI"),
        ]
    case "rsicv64":
        _platforms = [
            ("riscv64", "efi", "", "", "64-bit RISC-V EFI"),
        ]
    case _:
        broken = f"Unsupported platform ({self.profile().arch})"

def init_configure(self):
    from cbuild.util import make
    self.make = make.Make(self)

def do_configure(self):
    # configure tools build
    self.mkdir("build")
    self.do(
        self.chroot_cwd / "configure", f"--host={self.profile().triplet}",
        f"--with-platform=none", *configure_args,
        wrksrc = "build"
    )
    # platforms build
    for arch, platform, ecfl, ldfl, desc in _platforms:
        bdir = f"build_{arch}_{platform}"
        self.mkdir(bdir)
        cfl = "-fno-stack-protector -no-integrated-as " + ecfl
        # configure freestanding
        self.do(
            self.chroot_cwd / "configure", f"--host={self.profile().triplet}",
            f"--target={arch}", f"--with-platform={platform}",
            "--disable-efiemu", *configure_args,
            wrksrc = bdir, env = {
                "BUILD_CFLAGS": cfl,
                "BUILD_LDFLAGS": ldfl,
                "CFLAGS": cfl,
                "LDFLAGS": ldfl
            }
        )

def do_build(self):
    # primary build
    self.make.build(wrksrc = "build")
    # extra targets
    for arch, platform, cfl, ldfl, desc in _platforms:
        self.make.build(wrksrc = f"build_{arch}_{platform}")

def do_install(self):
    # populate extra targets first
    for arch, platform, cfl, ldfl, desc in _platforms:
        bdir = f"build_{arch}_{platform}"
        # full install
        self.make.install(wrksrc = bdir)
        # remove stuff that is not platform specific
        for d in ["etc", "usr/share", "usr/bin"]:
            self.rm(self.destdir / d, recursive = True, force = True)
    # install tools last
    self.make.install(wrksrc = "build")

def post_install(self):
    # kernel hook
    self.install_file(
        self.files_path / "99-grub.sh", "etc/kernel.d", mode = 0o755
    )
    # conf file
    self.install_file(
        self.files_path / "grub.default", "etc/default", name = "grub"
    )
    # update-grub
    self.install_bin(self.files_path / "update-grub")
    # move completions
    self.install_dir("usr/share/bash-completion/completions")
    self.mv(
        self.destdir / "etc/bash_completion.d/grub",
        self.destdir / "usr/share/bash-completion/completions"
    )
    # unused tools
    self.rm(self.destdir / "usr/bin/grub-ofpathname")
    self.rm(self.destdir / "usr/bin/grub-sparc64-setup")

@subpackage("grub-utils")
def _utils(self):
    self.pkgdesc = f"{pkgdesc} (additional utilities)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "usr/bin/grub-menulst2cfg",
        "usr/bin/grub-fstest",
        "usr/bin/grub-mkfont",
    ]

def _genplatform(arch, platform, desc):
    @subpackage(f"grub-{arch}-{platform}-dbg")
    def _platdbg(self):
        self.pkgdesc = f"{pkgdesc} ({desc} debug files)"
        self.depends = [f"grub-{arch}-{platform}={pkgver}-r{pkgrel}"]
        self.options = ["!strip", "foreignelf"]

        def _install():
            self.take(f"usr/lib/grub/{arch}-{platform}/*.module")
            self.take(
                f"usr/lib/grub/{arch}-{platform}/*.image", missing_ok = True
            )
            self.take(
                f"usr/lib/grub/{arch}-{platform}/*.exec", missing_ok = True
            )

        return _install

    @subpackage(f"grub-{arch}-{platform}")
    def _plat(self):
        self.pkgdesc = f"{pkgdesc} ({desc} support)"
        self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
        self.options = ["!strip"]

        return [f"usr/lib/grub/{arch}-{platform}"]

# generate platform subpackages
for arch, platform, cfl, ldfl, desc in _platforms:
    _genplatform(arch, platform, desc)

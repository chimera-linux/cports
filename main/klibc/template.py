pkgname = "klibc"
pkgver = "2.0.9"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_check_target = "test"
hostmakedepends = ["gmake", "perl", f"binutils-{self.profile().arch}"]
makedepends = ["linux-headers"]
pkgdesc = "Minimal libc subset for use with initramfs"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND BSD-3-Clause"
url = "https://git.kernel.org/cgit/libs/klibc/klibc.git"
source = f"$(KERNEL_SITE)/libs/klibc/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "6dcca708913320d26309f05b0c2bf68071bf11b3dadcc4e6c7d923837fc23ee1"
# symlink to linux-headers
options = ["brokenlinks", "!lto"]

match self.profile().arch:
    case "x86_64": _arch = "x86_64"
    case "aarch64": _arch = "arm64"
    case "ppc64le" | "ppc64": _arch = "ppc64"
    case "riscv64": _arch = "riscv64"
    case _:
        broken = f"Unknown CPU architecture: {self.profile().arch}"

def init_configure(self):
    eflags = [
        "KLIBCARCH=" + _arch,
        "INSTALLROOT=" + str(self.chroot_destdir),
        "CONFIG_DEBUG_INFO=y"
    ]
    if self.cross_build:
        eflags += ["CROSS_COMPILE={self.profile().triplet}-"]

    self.make_build_args += eflags
    self.make_install_args += eflags
    self.make_check_args += eflags

def do_configure(self):
    # use symlinks to linux api headers

    self.rm("linux", recursive = True, force = True)
    self.mkdir("linux/include", parents = True)

    for p in ["linux", "asm-generic", "asm"]:
        self.ln_s(f"/usr/include/{p}", "linux/include")

def pre_install(self):
    self.install_dir("usr/lib")
    self.install_link("usr/lib", "lib")

def post_install(self):
    self.install_license("usr/klibc/LICENSE")

    # remove bundled copies
    for p in ["linux", "asm-generic", "asm"]:
        self.rm(
            self.destdir / f"usr/lib/klibc/include/{p}",
            recursive = True, force = True
        )
        self.install_link(f"/usr/include/{p}", f"usr/lib/klibc/include/{p}")

    # remove helper symlink
    self.rm(self.destdir / "lib")

    # initramfs-tools
    self.install_file(
        self.files_path / "klibc-progs.initramfs-tools",
        "usr/share/initramfs-tools/hooks",
        mode = 0o755, name = "klibc-progs"
    )

@subpackage("klibc-devel")
def _devel(self):
    self.depends += ["linux-headers"]
    self.options = ["!splitstatic"]
    return [
        "usr/bin",
        "usr/lib/klibc/include",
        "usr/lib/klibc/lib",
        "usr/share/man"
    ]

@subpackage("klibc-progs")
def _progs(self):
    self.depends += [f"klibc={pkgver}-r{pkgrel}"]
    return ["usr/lib/klibc", "usr/share/initramfs-tools"]

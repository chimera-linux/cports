# update linux-modules-zfs when bumping
pkgname = "linux"
pkgver = "6.0.2"
pkgrel = 0
make_dir = "build"
# necessary for efistub
make_env = {"CBUILD_BYPASS_STRIP_WRAPPER": "1"}
hostmakedepends = ["base-kernel-devel"]
depends = ["base-kernel"]
pkgdesc = "Linux kernel 5.19.x"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://kernel.org"
source = f"https://cdn.kernel.org/pub/linux/kernel/v{pkgver[0]}.x/linux-{pkgver}.tar.xz"
sha256 = "a13c26388cacccb684cd9f51109596a280c8186b7e95174d31ee7c5718e95c9d"
# no meaningful checking to be done
options = [
    "!check", "!debug", "!strip", "!scanrundeps", "!scanshlibs",
    "!lto", "textrels", "foreignelf" # vdso32
]

match self.profile().arch:
    case "ppc64le" | "ppc64": _arch = "powerpc"
    case "aarch64": _arch = "arm64"
    case "x86_64": _arch = "x86_64"
    case "riscv64": _arch = "riscv"
    case _:
        broken = f"Unknown CPU architecture: {self.profile().arch}"

if self.profile().cross:
    broken = "linux-devel does not come out right"

def do_configure(self):
    cfgarch = self.profile().arch
    cfgname = f"config-{cfgarch}.generic"

    self.cp(self.files_path / cfgname, self.cwd)

    epoch = self.source_date_epoch or 0
    args = []

    if self.profile().cross:
        args += [f"CROSS_COMPILE={self.profile().triplet}"]

    self.do(
        "chimera-buildkernel",
        "prepare",
        f"ARCH={_arch}",
        f"CONFIG_FILE={self.chroot_cwd}/{cfgname}",
        f"OBJDIR={self.make_dir}",
        f"JOBS={self.make_jobs}",
        f"LOCALVERSION=-{pkgrel}-generic",
        f"EPOCH={epoch}",
        *args
    )

def do_build(self):
    self.do("chimera-buildkernel", "build", env = make_env)

def do_install(self):
    self.do("chimera-buildkernel", "install", self.chroot_destdir)

@subpackage("linux-devel")
def _devel(self):
    self.depends += ["clang"]
    self.options = ["foreignelf", "!scanshlibs"]
    return ["usr/src", "usr/lib/modules/*/build"]

@subpackage("linux-dbg")
def _dbg(self):
    self.pkgdesc += " (debug files)"
    self.options = [
        "!scanrundeps", "!strip", "!scanshlibs", "foreignelf", "textrels"
    ]
    return ["usr/lib/debug", "boot/System.map-*"]

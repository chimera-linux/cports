pkgname = "linux"
pkgver = "5.15.34"
pkgrel = 0
make_dir = "build"
hostmakedepends = ["base-kernel-devel"]
depends = ["base-kernel"]
pkgdesc = "Linux kernel 5.15.x"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://kernel.org"
source = f"https://cdn.kernel.org/pub/linux/kernel/v{pkgver[0]}.x/linux-{pkgver}.tar.xz"
sha256 = "a7514685392f0f89b337fa252a10a004c6a97d23e8d1126059c8e373398fdb69"
# no meaningful checking to be done
options = [
    "!check", "!debug", "!strip", "!scanrundeps", "!scanshlibs",
    "!lto", "textrels", "foreignelf" # vdso32
]

# we don't use LLVM_IAS for the time being, as ppc is not compatible with it
hostmakedepends += ["binutils", f"binutils-{self.profile().arch}"]

match self.profile().arch:
    case "ppc64le" | "ppc64": _arch = "powerpc"
    case "aarch64": _arch = "arm64"
    case "x86_64": _arch = "x86_64"
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
    self.do("chimera-buildkernel", "build")

def do_install(self):
    self.do("chimera-buildkernel", "install", self.chroot_destdir)

@subpackage("linux-devel")
def _devel(self):
    self.depends += ["binutils", "clang"]
    self.options = ["foreignelf", "!scanshlibs"]
    return ["usr/src", "usr/lib/modules/*/build"]

@subpackage("linux-dbg")
def _dbg(self):
    self.pkgdesc += " (debug files)"
    self.options = [
        "!scanrundeps", "!strip", "!scanshlibs", "foreignelf", "textrels"
    ]
    return ["usr/lib/debug", "boot/System.map-*"]

pkgname = "cpupower"
pkgver = "6.7.1"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_target = "cpupower"
make_build_args = [
    "-C",
    "tools",
    # FIXME: cpufreq-bench is completely broken with optimisations because of
    # int UB that gets optimised out and then breaks in div-by-zero
    "CPUFREQ_BENCH=0",
    "LLVM=1",
    "V=1",
    "NLS=false",
    "WERROR=0",
    "DEBUG=false",
    "STRIP=/bin/true",
    "libdir=/usr/lib",
    "mandir=/usr/share/man",
    "prefix=/usr",
    "sbindir=/usr/bin",
]
make_install_target = "cpupower_install"
make_install_args = list(make_build_args)
hostmakedepends = ["gmake"]
makedepends = ["linux-headers", "pciutils-devel"]
pkgdesc = "Linux CPU power management tools"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://kernel.org"
source = f"https://cdn.kernel.org/pub/linux/kernel/v{pkgver[:pkgver.find('.')]}.x/linux-{pkgver}.tar.xz"
sha256 = "1ecffa568e86a2202ba5533ad9034bc263a9aa14e189597a94f09b3854ad68c3"
# nope
options = ["!check"]


@subpackage("cpupower-devel")
def _devel(self):
    return self.default_devel()

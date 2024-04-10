pkgname = "cpupower"
pkgver = "6.8.4"
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
sha256 = "d5dec495fc00605fa9e04114df547fbc92b33d9ea7a4a2b7073c589590e79e63"
# nope
options = ["!check"]


@subpackage("cpupower-devel")
def _devel(self):
    return self.default_devel()

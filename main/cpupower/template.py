pkgname = "cpupower"
pkgver = "6.4.12"
pkgrel = 2
build_style = "makefile"
make_cmd = "gmake"
_make_args = [
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
make_build_target = "cpupower"
make_build_args = _make_args
make_install_target = "cpupower_install"
make_install_args = _make_args
hostmakedepends = ["gmake"]
makedepends = ["linux-headers", "pciutils-devel"]
pkgdesc = "Linux CPU power management tools"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://kernel.org"
source = f"https://cdn.kernel.org/pub/linux/kernel/v{pkgver[:pkgver.find('.')]}.x/linux-{pkgver}.tar.xz"
sha256 = "cca91be956fe081f8f6da72034cded96fe35a50be4bfb7e103e354aa2159a674"
# nope
options = ["!check"]


@subpackage("cpupower-devel")
def _devel(self):
    return self.default_devel()

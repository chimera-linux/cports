pkgname = "linux-tools"
pkgver = "6.4.12"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
_make_args = [
    "-C",
    "tools",
    # FIXME: cpufreq-bench is completely broken with optimisations because of
    # int UB that gets optimised out and then breaks in div-by-zero
    "CPUFREQ_BENCH=0",
    "LLVM=1",
    "NLS=false",
    "WERROR=0",
    "libdir=/usr/lib",
    "mandir=/usr/share/man",
    "prefix=/usr",
    "sbindir=/usr/bin",
]
make_build_target = ""
make_build_args = _make_args + [
    "cpupower",
]
make_install_target = ""
make_install_args = _make_args + [
    "cpupower_install",
]
hostmakedepends = [
    "gmake",
]
makedepends = [
    "linux-headers",
    "pciutils-devel",
]
pkgdesc = "Linux Kernel userspace tools"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-only"
url = "https://www.kernel.org"
source = f"https://cdn.kernel.org/pub/linux/kernel/v{pkgver[:pkgver.find('.')]}.x/linux-{pkgver}.tar.xz"
sha256 = "cca91be956fe081f8f6da72034cded96fe35a50be4bfb7e103e354aa2159a674"
# vis breaks everything
hardening = []
# nah 💀
options = ["!check"]


def init_build(self):
    self.make_build_args += [f"CC={self.get_tool('CC')}"]


@subpackage("cpupower")
def _cpupower(self):
    self.pkgdesc = "Linux standard cpu power management tool"
    return [
        "usr/bin/cpupower",
        "usr/share/bash-completion/completions/cpupower",
        "usr/share/man/man1/cpupower*",
    ]


@subpackage("libcpupower")
def _libcpupower(self):
    self.pkgdesc = "Linux cpupower library"
    return [
        "usr/lib/libcpupower.so.*",
    ]


@subpackage("libcpupower-devel")
def _libcpupower_devel(self):
    self.pkgdesc = "Linux cpupower library (development files)"
    return [
        "usr/include/cpufreq.h",
        "usr/include/cpuidle.h",
        "usr/include/powercap.h",
        "usr/lib/libcpupower.*",
    ]

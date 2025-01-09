pkgname = "perf"
pkgver = "6.12.8"
pkgrel = 0
build_wrksrc = "tools/perf"
build_style = "makefile"
make_build_args = [
    "-f",
    "Makefile.perf",
    "LIBBPF_DYNAMIC=1",
    "LLVM=1",
    "NO_LIBAUDIT=1",
    "NO_LIBBABELTRACE=1",
    "NO_LIBPFM4=1",
    "NO_LIBUNWIND=1",
    "NO_SDT=1",
    "STRIP=/bin/true",
    "V=1",
    "WERROR=0",
    "libdir=/usr/lib",
    "perfexecdir=/usr/lib/perf-core",
    "mandir=/usr/share/man",
    "prefix=/usr",
    "sbindir=/usr/bin",
    "tipdir=/usr/share/doc/perf-tip",
]
make_install_args = [
    "install-python_ext",
    *make_build_args,
]
make_use_env = True
hostmakedepends = [
    "asciidoc",
    "bash",
    "bison",
    "flex",
    "pkgconf",
    "python-setuptools",
    "xmlto",
]
makedepends = [
    "audit-devel",  # for archs without syscall_table like riscv
    "capstone-devel",
    "elfutils-devel",
    "libbpf-devel",
    "libnuma-devel",
    "libtraceevent-devel",
    "linux-headers",
    "openssl-devel",
    "perl",
    "python-devel",
    "slang-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Linux performance analyzer"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://perf.wiki.kernel.org/index.php/Main_Page"
source = f"https://cdn.kernel.org/pub/linux/kernel/v{pkgver[: pkgver.find('.')]}.x/linux-{pkgver}.tar.xz"
sha256 = "2291da065ca04b715c89ee50362aec3f021a7414bc963f1b56736682c8122979"
# nope
# docs are a single tips file that gets displayed in the TUI
options = ["!check", "!splitdoc"]

if self.profile().arch == "ppc":
    broken = "segfaults during build"


def init_build(self):
    self.make_build_args += [f"EXTRA_CFLAGS={self.get_cflags(shell=True)}"]
    self.make_install_args += [f"EXTRA_CFLAGS={self.get_cflags(shell=True)}"]


def post_install(self):
    # relink hardlink
    self.uninstall("usr/bin/trace")
    self.install_link("usr/bin/trace", "perf")
    # valid as both
    self.uninstall("etc/bash_completion.d")
    self.install_completion("perf-completion.sh", "bash")
    self.install_completion("perf-completion.sh", "zsh")
    # pointless tests
    self.uninstall("usr/lib/perf-core/tests")

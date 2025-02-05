pkgname = "bcc"
# keep in sync with contrib/libbpf-tools
pkgver = "0.33.0"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DCMAKE_USE_LIBBPF_PACKAGE=ON",
    "-DENABLE_EXAMPLES=OFF",
    "-DENABLE_LIBDEBUGINFOD=OFF",
    "-DENABLE_LLVM_SHARED=ON",
    "-DENABLE_NO_PIE=OFF",
    "-DENABLE_TESTS=OFF",
    f"-DREVISION={pkgver}",
    "-DRUN_LUA_TESTS=OFF",
]
hostmakedepends = [
    "bison",
    "cmake",
    "flex",
    "ninja",
    "pkgconf",
    "python-setuptools",
]
makedepends = [
    "clang-devel",
    "clang-tools-extra",  # for cmake
    "elfutils-devel",
    "libbpf-devel",
    "libxml2-devel",
    "linux-headers",
    "llvm-devel",
    "zlib-ng-compat-devel",
]
depends = [
    self.with_pkgver("bcc-python"),
    # dep of half the programs in /usr/share/bcc/tools
    "bash",
]
pkgdesc = "Toolkit for creating eBPF programs"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/iovisor/bcc"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "83b486bffca939baf74742c29d4f02ce90df740c26fe147549987f5c1fd32a8b"
tool_flags = {
    # see libbpf comment about bpf headers
    "CFLAGS": ["-I/usr/include/bpf/uapi"],
    "CXXFLAGS": ["-I/usr/include/bpf/uapi"],
}
# no way to run them in bwrap
options = ["!check"]


def post_install(self):
    # bpf-ps, elf binary
    self.rename(
        "usr/share/bcc/introspection/bps", "usr/bin/bps", relative=False
    )
    self.install_link("usr/share/bcc/introspection/bps", "../../../bin/bps")


@subpackage("bcc-devel")
def _(self):
    return self.default_devel()


@subpackage("bcc-libs")
def _(self):
    self.subdesc = "runtime libraries"
    return self.default_libs()


@subpackage("bcc-python")
def _(self):
    self.subdesc = "python module"
    self.depends += [self.with_pkgver("bcc-libs")]
    # transitional
    self.provides = [self.with_pkgver("python-bcc")]
    return ["usr/lib/python*"]

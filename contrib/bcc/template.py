pkgname = "bcc"
# keep in sync with contrib/libbpf-tools
pkgver = "0.30.0"
pkgrel = 0
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
    "zlib-devel",
]
depends = [
    f"python-bcc={pkgver}-r{pkgrel}",
    # dep of half the programs in /usr/share/bcc/tools
    "bash",
]
pkgdesc = "Toolkit for creating eBPF programs"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/iovisor/bcc"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d113f842965fd84f8bf2f3e9dda73a2cae59a4d27bec3fa87d0b57ee99b58273"
tool_flags = {
    # see libbpf comment about bpf headers
    "CFLAGS": ["-I/usr/include/bpf/uapi"],
    "CXXFLAGS": ["-I/usr/include/bpf/uapi"],
}
# no way to run them in bwrap
options = ["!check"]


def post_install(self):
    # bpf-ps, elf binary
    self.install_dir("usr/bin")
    self.mv(
        self.destdir / "usr/share/bcc/introspection/bps",
        self.destdir / "usr/bin",
    )
    self.install_link("usr/share/bcc/introspection/bps", "../../../bin/bps")


@subpackage("bcc-devel")
def _devel(self):
    return self.default_devel()


@subpackage("bcc-libs")
def _libs(self):
    self.pkgdesc = f"{pkgdesc} (runtime libraries)"
    return self.default_libs()


@subpackage("python-bcc")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (python module)"
    self.depends += [f"bcc-libs={pkgver}-r{pkgrel}"]
    return ["usr/lib/python*"]

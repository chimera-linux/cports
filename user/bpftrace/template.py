pkgname = "bpftrace"
pkgver = "0.27.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # cant run them anyway
    "-DBUILD_TESTING=OFF",
    "-DUSE_SYSTEM_LIBBPF=ON",
]
hostmakedepends = [
    "asciidoctor",
    "bison",
    "cmake",
    "flex",
    "ninja",
    "vim-xxd",
]
makedepends = [
    "bcc-devel",
    "cereal",
    "elfutils-devel",
    "libbpf-devel",
    "libbpf-devel-static",
    "libedit-devel",
    "libffi8-devel",
    "libpcap-devel",
    "libxml2-devel",
    "linux-headers",
    "lldb-devel",
    "llvm-clang-devel",
    "llvm-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "High-level eBPF tracing language"
license = "Apache-2.0"
url = "https://github.com/bpftrace/bpftrace"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "52a923555b6e16fe13a285b6713637bfaab30a5efa60f44c03134bd832342012"
# bpftrace/bpftrace-aotrt binaries need keeping BEGIN/END_trigger syms
# just skip strip for now until we can plumb through --keep-symbol to objcopy
options = ["!strip", "llvmflags"]

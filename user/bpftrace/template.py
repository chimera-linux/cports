pkgname = "bpftrace"
pkgver = "0.24.1"
pkgrel = 1
build_style = "cmake"
configure_args = [
    # cant run them anyway
    "-DBUILD_TESTING=OFF",
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
    "clang-devel",
    "clang-tools-extra",  # cmake detection
    "elfutils-devel",
    "libbpf-devel",
    "libedit-devel",
    "libffi8-devel",
    "libpcap-devel",
    "libxml2-devel",
    "linux-headers",
    "lldb-devel",
    "llvm-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "High-level eBPF tracing language"
license = "Apache-2.0"
url = "https://github.com/bpftrace/bpftrace"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "493265e0687312e6825ef07a6fcbc5327b5ca207c25f2b4738ca1461f90485ac"
# bpftrace/bpftrace-aotrt binaries need keeping BEGIN/END_trigger syms
# just skip strip for now until we can plumb through --keep-symbol to objcopy
options = ["!strip"]

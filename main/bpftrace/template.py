pkgname = "bpftrace"
pkgver = "0.22.1"
pkgrel = 0
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/bpftrace/bpftrace"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "31369abf18a42a970ad094e7e92af9547208a38a4e4a3bcb0ffa470fb4f50016"
# bpftrace/bpftrace-aotrt binaries need keeping BEGIN/END_trigger syms
# just skip strip for now until we can plumb through --keep-symbol to objcopy
options = ["!strip"]

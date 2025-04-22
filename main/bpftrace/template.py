pkgname = "bpftrace"
pkgver = "0.23.2"
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
license = "Apache-2.0"
url = "https://github.com/bpftrace/bpftrace"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7e0da01b23599d6ad9762b61cda5be2b72c3526414c56093d4b63d9f720de300"
# bpftrace/bpftrace-aotrt binaries need keeping BEGIN/END_trigger syms
# just skip strip for now until we can plumb through --keep-symbol to objcopy
options = ["!strip"]

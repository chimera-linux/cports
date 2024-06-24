pkgname = "bpftrace"
pkgver = "0.21.1"
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
    "libpcap-devel",
    "libxml2-devel",
    "linux-headers",
    "lldb-devel",
    "llvm-devel",
    "zlib-devel",
]
pkgdesc = "High-level eBPF tracing language"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/bpftrace/bpftrace"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6bd8f83ba741670d73dc0302cd21e749714ce0b2881fed26734e50587ef6fab4"
# bpftrace/bpftrace-aotrt binaries need keeping BEGIN/END_trigger syms
# just skip strip for now until we can plumb through --keep-symbol to objcopy
options = ["!strip"]

pkgname = "bpftrace"
pkgver = "0.21.0"
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
sha256 = "8bbca667633fd7b64077cd59b493b94bfab19af582a824091582299aaca76b04"
# bpftrace/bpftrace-aotrt binaries need keeping BEGIN/END_trigger syms
# just skip strip for now until we can plumb through --keep-symbol to objcopy
options = ["!strip"]

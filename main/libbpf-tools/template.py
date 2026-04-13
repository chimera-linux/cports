pkgname = "libbpf-tools"
pkgver = "0.36.1"
pkgrel = 0
archs = ["aarch64", "ppc64le", "riscv64", "x86_64"]
build_wrksrc = "libbpf-tools"
build_style = "makefile"
make_build_args = [
    "prefix=/usr",
    "V=1",
    "APP_PREFIX=bpf-",
    "BPFTOOL=bpftool",
    "BPFTOOL_OUTPUT=/usr/bin/bpftool",
    "USE_BLAZESYM=0",
]
make_install_args = [*make_build_args]
hostmakedepends = [
    "bpftool",
    "pkgconf",
]
makedepends = [
    "argp-standalone",
    "libbpf-devel",
    "linux-headers",
]
pkgdesc = "Standalone eBPF programs from BCC"
license = "LGPL-2.1-only OR BSD-2-Clause"
url = "https://github.com/iovisor/bcc/tree/master/libbpf-tools"
source = f"https://github.com/iovisor/bcc/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3b16f1eb6a5b90a5a68686c0f4195455f1c58da5ae40f004e931c19e98fa8d98"
tool_flags = {
    # see libbpf comment about bpf headers
    "CFLAGS": ["-I/usr/include/bpf/uapi"],
    "CXXFLAGS": ["-I/usr/include/bpf/uapi"],
    "LDFLAGS": ["-largp"],
}
# check: no tests
# distlicense: no actual bsd license in the folders, just headers
options = ["!check", "!distlicense"]

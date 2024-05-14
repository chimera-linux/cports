pkgname = "libbpf-tools"
pkgver = "0.30.0"
pkgrel = 0
archs = ["aarch64", "ppc64le", "riscv64", "x86_64"]
build_wrksrc = "libbpf-tools"
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["prefix=/usr", "V=1", "APP_PREFIX=bpf-"]
make_install_args = list(make_build_args)
hostmakedepends = [
    "bpftool",
    "gmake",
    "pkgconf",
]
makedepends = [
    "argp-standalone",
    "libbpf-devel",
    "linux-headers",
]
pkgdesc = "Standalone eBPF programs from BCC"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-only OR BSD-2-Clause"
url = "https://github.com/iovisor/bcc/tree/master/libbpf-tools"
source = f"https://github.com/iovisor/bcc/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d113f842965fd84f8bf2f3e9dda73a2cae59a4d27bec3fa87d0b57ee99b58273"
tool_flags = {
    # see libbpf comment about bpf headers
    "CFLAGS": ["-I/usr/include/bpf/uapi"],
    "CXXFLAGS": ["-I/usr/include/bpf/uapi"],
    "LDFLAGS": ["-largp"],
}
# check: no tests
# distlicense: no actual bsd license in the folders, just headers
options = ["!check", "!distlicense"]

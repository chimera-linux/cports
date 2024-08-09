pkgname = "musl-allocator-scudo"
pkgver = "18.1.8"
pkgrel = 0
archs = ["aarch64", "ppc64le", "ppc64", "riscv64", "x86_64"]
build_wrksrc = "lib/scudo/standalone"
makedepends = ["linux-headers"]
pkgdesc = "Scudo allocator for musl"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/compiler-rt-{pkgver}.src.tar.xz"
sha256 = "e054e99a9c9240720616e927cb52363abbc8b4f1ef0286bad3df79ec8fdf892f"
tool_flags = {
    "CXXFLAGS": [
        "-DSCUDO_DISABLE_TBI",
        "-ffreestanding",
        "-fno-exceptions",
        "-fno-rtti",
        "-fno-align-functions",
        "-fno-unwind-tables",
        "-fno-asynchronous-unwind-tables",
        "-ffunction-sections",
        "-fdata-sections",
        "-Iinclude",
    ]
}
options = ["!lto", "!strip"]


def post_extract(self):
    self.cp(self.files_path / "musl-wrappers.cpp", "lib/scudo/standalone")


def do_build(self):
    from cbuild.util import compiler

    cxx = compiler.CXX(self)
    inps = [
        "checksum",
        "common",
        "condition_variable_linux",
        "crc32_hw",
        "flags",
        "flags_parser",
        "linux",
        "mem_map",
        "mem_map_linux",
        "musl-wrappers",
        "release",
        "report",
        "report_linux",
        "string_utils",
        "timing",
    ]

    for inp in inps:
        cxx.invoke([f"{inp}.cpp"], f"{inp}.o", True)

    self.do("ar", "rcs", "musl-scudo.a", *map(lambda v: f"{v}.o", inps))


def do_install(self):
    self.install_file("musl-scudo.a", "usr/lib")

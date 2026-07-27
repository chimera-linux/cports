pkgname = "intel-graphics-compiler"
pkgver = "2.38.2"
pkgrel = 0
_llvmver = "17.0.6"
_oclclangver = "17.0.8"
_vciver = "0.25.0"
_spirvllvmver = "17.0.25"
_spirvheadershash = "948a3b0997e2dffea5484b3df7bd5590c5b844cc"
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
    "-DIGC_OPTION__ARCHITECTURE_TARGET=Linux64",
    "-DIGC_OPTION__SPIRV_TOOLS_MODE=Prebuilds",
    "-DIGC_OPTION__CLANG_MODE=Source",
    "-DIGC_OPTION__LLD_MODE=Source",
    f"-DIGC_OPTION__LLVM_PREFERRED_VERSION={_llvmver}",
    "-DIGC_OPTION__LLVM_MODE=Source",
    "-DIGC_OPTION__VC_INTRINSICS_MODE=Source",
    "-DLLVM_BUILD_TOOLS=ON",
]
hostmakedepends = [
    "bash",
    "bison",
    "cmake",
    "flex",
    "git",
    "meson",
    "ninja",
    "pkgconf",
    "python",
    "python-mako",
    "python-pyyaml",
]
makedepends = ["spirv-tools-devel"]
pkgdesc = "Intel Graphics Compiler for OpenCL"
license = "MIT"
url = "https://github.com/intel/intel-graphics-compiler"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/llvm/llvm-project/archive/refs/tags/llvmorg-{_llvmver}.tar.gz",
    f"https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/refs/tags/v{_spirvllvmver}.tar.gz",
    f"https://github.com/intel/opencl-clang/archive/refs/tags/v{_oclclangver}.tar.gz",
    f"https://github.com/intel/vc-intrinsics/archive/refs/tags/v{_vciver}.tar.gz",
    f"https://github.com/KhronosGroup/SPIRV-Headers/archive/{_spirvheadershash}.tar.gz",
]
source_paths = [
    ".",
    "llvm-project",
    "llvm-project/llvm/projects/llvm-spirv",
    "llvm-project/llvm/projects/opencl-clang",
    "vc-intrinsics",
    "spirv-headers",
]
sha256 = [
    "24f707f08d9b87e7e6857f8a83d9944990189c051ce9b3c91c291bdc1563246f",
    "81494d32e6f12ea6f73d6d25424dbd2364646011bb8f7e345ca870750aa27de1",
    "f7402f05cdb43254e97c0214fdcc9c8f359f1940005e520cbfbbbfb326752fa9",
    "b5708a6d10d30cfd24d774c944d60518f8a59dd3ce40517fe586b0ff480663bf",
    "83d6e0528feb6a47f7818e7c1dd3305dd8a48fb1103d279571dad517a93a8d39",
    "19eff765f08d0b8ff5f80ba3c2e902a6baf54123bff50ca383db633ee5b6f778",
]
# suppress harmless signed-overflow UB in llvm
hardening = ["!int"]
# see: https://github.com/intel/intel-graphics-compiler/issues/362
options = ["!cross", "!lto"]

tool_flags = {
    "CFLAGS": [
        "-fno-semantic-interposition",
        "-Wno-error=macro-redefined",
    ],
    "CXXFLAGS": [
        "-fno-semantic-interposition",
        "-Wno-error=macro-redefined",
        "-Wno-error=pointer-to-int-cast",
        "-Wno-error=nontrivial-memcall",
    ],
    "LDFLAGS": ["-Wl,-Bsymbolic"],
}


def init_configure(self):
    llvm = f"{self.chroot_srcdir}/llvm-project"
    self.configure_args += [
        f"-DIGC_OPTION__LLVM_SOURCES_DIR={llvm}",
        f"-DIGC_OPTION__CLANG_SOURCES_DIR={llvm}/clang",
        f"-DIGC_OPTION__lld_SOURCES_DIR={llvm}/lld",
        f"-DDEFAULT_IGC_LLVM_SOURCES_DIR={llvm}",
        f"-DIGC_OPTION__VC_INTRINSICS_SOURCES_DIR={self.chroot_srcdir}/vc-intrinsics",
        f"-DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR={self.chroot_srcdir}/spirv-headers",
        f"-DIGC_BUILD__SPIRV-Headers_DIR={self.chroot_srcdir}/spirv-headers",
    ]

    # igc expects llvm-spirv's public headers in the include path
    self.configure_env["CXXFLAGS"] = self.get_cxxflags(
        extra_flags=[f"-I{llvm}/llvm/projects/llvm-spirv/include"],
        shell=True,
    )


def pre_configure(self):
    # igc expects vc-intrinsics next to the source
    self.ln_s(f"{self.chroot_srcdir}/vc-intrinsics", "../vc-intrinsics")


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("intel-graphics-compiler-devel")
def _(self):
    return self.default_devel()

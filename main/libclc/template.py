pkgname = "libclc"
pkgver = "23.1.6"
pkgrel = 0
build_style = "cmake"
_clc_triples = [
    "amdgcn-amd-amdhsa-llvm",
    "nvptx64-nvidia-cuda",
    "spirv32-unknown-unknown",
    "spirv64-unknown-unknown",
    "spirv32-unknown-vulkan",
    "spirv64-unknown-vulkan",
]
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
]
cmake_dir = "libclc"
hostmakedepends = [
    "cmake",
    "libedit-devel",
    "libffi8-devel",
    "llvm-devel",
    "ncurses-devel",
    "ninja",
    "pkgconf",
    "python",
    "spirv-llvm-translator",
    "zlib-ng-compat-devel",
]
pkgdesc = "Open implementation of the OpenCL C programming language"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://libclc.llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "d3b86ab29cfb4445a6652e5c2642ccc75e04e38084dde3701d323320f35a31da"
hardening = ["!int"]
# whatever
options = ["!check", "!lto", "!strip", "!debug", "llvmflags"]


def configure(self):
    from cbuild.util import cmake

    with self.use_profile("host"):
        for trip in _clc_triples:
            with self.stamp(f"{trip}_configure") as s:
                s.check()
                cmake.configure(
                    self,
                    f"build-{trip}",
                    self.cmake_dir,
                    [
                        f"-DLLVM_DEFAULT_TARGET_TRIPLE={trip}",
                        *self.configure_args,
                    ],
                )


def build(self):
    from cbuild.util import cmake

    for trip in _clc_triples:
        with self.stamp(f"{trip}_build") as s:
            s.check()
            cmake.build(self, f"build-{trip}")


def install(self):
    from cbuild.util import cmake

    for trip in _clc_triples:
        cmake.install(self, f"build-{trip}")

    # mesa wants these
    self.install_link(
        "usr/share/clc/spirv-mesa3d-.spv", "spirv32-unknown-unknown/libclc.spv"
    )
    self.install_link(
        "usr/share/clc/spirv64-mesa3d-.spv",
        "spirv64-unknown-unknown/libclc.spv",
    )

    # mesa wants a .pc file
    self.install_file(
        self.files_path / "libclc.pc",
        "usr/share/pkgconfig",
        template={"VERSION": pkgver},
    )
    self.install_license("LICENSE.TXT")

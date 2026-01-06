pkgname = "lldb"
pkgver = "21.1.8"
pkgrel = 0
archs = ["aarch64", "loongarch64", "ppc64le", "ppc64", "riscv64", "x86_64"]
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DLLDB_ENABLE_LUA=OFF",  # maybe later
    "-DLLDB_ENABLE_PYTHON=ON",
    "-DLLDB_ENABLE_LIBEDIT=ON",
]
hostmakedepends = [
    "clang-tools-extra",
    "cmake",
    "ninja",
    "pkgconf",
    "python-devel",
    "swig",
]
makedepends = [
    "clang-devel",
    "libedit-devel",
    "libffi8-devel",
    "libxml2-devel",
    "linux-headers",
    "llvm-devel",
    "ncurses-devel",
    "python-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "LLVM debugger"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://llvm.org"
source = [
    f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/lldb-{pkgver}.src.tar.xz",
    f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/cmake-{pkgver}.src.tar.xz",
]
source_paths = [".", "llvm-cmake"]
sha256 = [
    "e28d73ed3f9e231f798ed66865e652a641eb0666cfa6c7b36e116da92fb72e56",
    "85735f20fd8c81ecb0a09abb0c267018475420e93b65050cc5b7634eab744de9",
]
# tests are not enabled
options = ["!check"]


def init_configure(self):
    self.configure_args += [
        f"-DLLVM_COMMON_CMAKE_UTILS={self.chroot_cwd}/llvm-cmake",
    ]

    if self.profile().cross:
        self.configure_args += [
            "-DLLDB_TABLEGEN="
            + str(self.chroot_cwd / "build_host/bin/lldb-tblgen")
        ]


def pre_configure(self):
    if not self.profile().cross:
        return

    from cbuild.util import cmake

    self.log("building host tblgen...")

    with self.profile("host"):
        with self.stamp("host_lldb_configure"):
            # need to pass the triplets so builtins are found
            cmake.configure(self, "build_host", self.cmake_dir, [])

        with self.stamp("host_lldb_tblgen") as s:
            s.check()
            cmake.build(self, "build_host", ["--target", "bin/lldb-tblgen"])


def post_install(self):
    from cbuild.util import python

    self.install_license("LICENSE.TXT")

    # fix up python liblldb symlink so it points to versioned one
    # unversioned one is in devel package so we cannot point to it
    for f in (self.destdir / "usr/lib").glob("python3*"):
        fp = f / "site-packages/lldb"
        if not fp.is_dir():
            continue
        for s in fp.glob("_lldb.*.so"):
            if s.is_symlink():
                s.unlink()
                s.with_name("_lldb.so").symlink_to(
                    f"../../../liblldb.so.{pkgver}"
                )
    # also precompile bytecode
    python.precompile(self, "usr/lib")


@subpackage("lldb-devel")
def _(self):
    return self.default_devel()

pkgname = "lldb"
pkgver = "23.1.6"
pkgrel = 0
archs = ["aarch64", "loongarch64", "ppc64le", "ppc64", "riscv64", "x86_64"]
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DLLDB_ENABLE_LUA=OFF",  # maybe later
    "-DLLDB_ENABLE_PYTHON=ON",
    "-DLLDB_ENABLE_LIBEDIT=ON",
    "-DLLDB_BUILD_INTEL_PT=ON",
    "-DLIBIPT_INCLUDE_PATH=/usr/include",
    "-DLIBIPT_LIBRARY_PATH=/usr/lib",
]
cmake_dir = "lldb"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "python-devel",
    "swig",
]
makedepends = [
    "libedit-devel",
    "libffi8-devel",
    "libipt-devel",
    "libxml2-devel",
    "linux-headers",
    "llvm-clang-devel",
    "llvm-devel",
    "ncurses-devel",
    "python-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "LLVM debugger"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "d3b86ab29cfb4445a6652e5c2642ccc75e04e38084dde3701d323320f35a31da"
# tests are not enabled
options = ["!check", "llvmflags"]


def init_configure(self):
    if self.profile.cross:
        self.configure_args += [
            "-DLLDB_TABLEGEN="
            + str(self.chroot_cwd / "build_host/bin/lldb-tblgen")
        ]


def pre_configure(self):
    if not self.profile.cross:
        return

    from cbuild.util import cmake

    self.log("building host tblgen...")

    with self.use_profile("host"):
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


@split("devel")
def _(self):
    return self.default_devel()

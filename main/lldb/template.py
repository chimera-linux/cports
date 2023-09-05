pkgname = "lldb"
pkgver = "16.0.6"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-Wno-dev",
    "-DLLVM_COMMON_CMAKE_UTILS=cmake",
    "-DLLDB_ENABLE_LUA=NO",  # maybe later
    "-DLLDB_ENABLE_PYTHON=YES",
    "-DLLDB_ENABLE_LIBEDIT=YES",
    "-DLLDB_USE_SYSTEM_SIX=YES",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "python-devel",
    "clang-tools-extra",
    "swig",
]
makedepends = [
    "llvm-devel",
    "clang-devel",
    "libffi-devel",
    "zlib-devel",
    "xz-devel",
    "libedit-devel",
    "libxml2-devel",
    "ncurses-devel",
    "python-devel",
    "linux-headers",
]
pkgdesc = "LLVM debugger"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/{pkgname}-{pkgver}.src.tar.xz"
sha256 = "e70a2360aff09553ab327f0f87a08ab869cea991068df38fd3e530368d4d3fae"
# tests are not enabled
options = ["!check"]


def post_extract(self):
    # not shipped with standalone lldb tarball
    self.mkdir("cmake/Modules", parents=True)
    self.cp(self.files_path / "FindLibEdit.cmake", self.cwd / "cmake/modules")
    self.cp(self.files_path / "CMakePolicy.cmake", self.cwd / "cmake/Modules")


def init_configure(self):
    if not self.profile().cross:
        return
    self.configure_args.append(
        "-DLLDB_TABLEGEN=" + str(self.chroot_cwd / "build_host/bin/lldb-tblgen")
    )


def pre_configure(self):
    if not self.profile().cross:
        return

    from cbuild.util import make, cmake

    self.log("building host tblgen...")

    with self.profile("host"):
        with self.stamp("host_lldb_configure"):
            # need to pass the triplets so builtins are found
            cmake.configure(self, self.cmake_dir, "build_host", [])

        with self.stamp("host_lldb_tblgen") as s:
            s.check()
            make.Make(self, wrksrc="build_host").invoke(["bin/lldb-tblgen"])


def post_install(self):
    from cbuild.util import python

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
        python.precompile(self, str(fp.relative_to(self.destdir)))


@subpackage("lldb-devel")
def _devel(self):
    return self.default_devel()

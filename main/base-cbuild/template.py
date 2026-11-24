pkgname = "base-cbuild"
pkgver = "0.1"
pkgrel = 15
_llvmver = 23
build_style = "meta"
# musl must be built first to provide shlibs for later packages during stage 0
depends = [
    "apk-tools",
    "chimerautils-extra",
    "fakeroot-core",
    "gmake",
    "libarchive-progs",
    "llvm-clang",
    "llvm-runtimes",
    "musl-devel",
    "ncurses",
    self.with_pkgver("base-cbuild-progs"),
]
provides = ["bootstrap:cbuild=9999-r0"]
replaces = ["apk-tools"]
replaces_priority = 100
pkgdesc = "Core package set for cbuild containers"
license = "custom:meta"
url = "https://chimera-linux.org"
options = ["bootstrap", "brokenlinks"]

if self.stage > 0:
    depends += [
        "apk-tools-static-bin",
        "bc-gh",
        "resolvconf",
        "resolvconf-none",
        "tzdb",
    ]

if self.stage > 2:
    depends += ["ccache"]


def build(self):
    from cbuild.util import compiler

    self.cp(self.files_path / "cbuild-cross-cc.c", ".")
    self.cp(self.files_path / "cbuild-lld-wrapper.c", ".")

    cc = compiler.C(self)
    cc.invoke(["cbuild-cross-cc.c"], "cbuild-cross-cc")
    cc.invoke(["cbuild-lld-wrapper.c"], "cbuild-lld-wrapper")


def install(self):
    self.install_bin("cbuild-cross-cc")
    self.install_bin("cbuild-lld-wrapper")

    # replace regular ld and ld.lld symlinks
    self.install_dir(f"usr/lib/llvm{_llvmver}/bin")
    self.install_link(
        f"usr/lib/llvm{_llvmver}/bin/ld.lld", "../../../bin/cbuild-lld-wrapper"
    )
    self.install_link(
        f"usr/lib/llvm{_llvmver}/bin/ld64.lld",
        "../../../bin/cbuild-lld-wrapper",
    )

    # different default apk config
    self.install_file(self.files_path / "config", "usr/lib/apk")


@subpackage("base-cbuild-progs")
def _(self):
    # make sure to use our wrapper symlinks
    self.replaces = [f"llvm{_llvmver}-lld"]
    self.replaces_priority = 100
    self.options = ["!scancmd"]

    return ["usr/bin", f"usr/lib/llvm{_llvmver}"]

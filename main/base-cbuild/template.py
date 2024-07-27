pkgname = "base-cbuild"
pkgver = "0.1"
pkgrel = 6
build_style = "meta"
pkgdesc = "Core package set for cbuild containers"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"

# musl must be built first to provide shlibs for later packages during stage 0
depends = [
    "musl-devel",
    "llvm",
    "clang",
    "lld",
    "ncurses",
    "chimerautils-extra",
    "apk-tools",
    "bmake",
    "bsdtar",
    "fakeroot-core",
    self.with_pkgver("base-cbuild-progs"),
]
provides = ["apk-tools-cache-link=9999-r0"]

options = ["bootstrap", "brokenlinks"]

if self.stage > 0:
    depends += [
        "apk-tools-static-bin",
        "bc-gh",
        "resolvconf",
        "resolvconf-none",
        "tzdata",
    ]

if self.stage > 1:
    depends += ["ccache"]


def do_build(self):
    from cbuild.util import compiler

    self.cp(self.files_path / "cbuild-cross-cc.c", ".")
    self.cp(self.files_path / "cbuild-lld-wrapper.c", ".")

    cc = compiler.C(self)
    cc.invoke(["cbuild-cross-cc.c"], "cbuild-cross-cc")
    cc.invoke(["cbuild-lld-wrapper.c"], "cbuild-lld-wrapper")


def do_install(self):
    self.install_bin("cbuild-cross-cc")
    self.install_bin("cbuild-lld-wrapper")

    # replace regular ld and ld.lld symlinks
    self.install_link("usr/bin/ld.lld", "cbuild-lld-wrapper")
    self.install_link("usr/bin/ld64.lld", "cbuild-lld-wrapper")


@subpackage("base-cbuild-progs")
def _cprogs(self):
    # make sure to use our wrapper symlinks
    self.replaces = ["lld"]
    self.replaces_priority = 100
    self.options = ["!scancmd"]

    return self.default_progs()

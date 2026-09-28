pkgname = "musl-mallocng"
pkgver = "1.2.6"
pkgrel = 1
_commit = "9fa28ece75d8a2191de7c5bb53bed224c5947417"
_mimalloc_ver = "2.2.7"
build_style = "gnu_configure"
configure_args = [
    "--prefix=/usr",
    "--disable-gcc-wrapper",
    "--with-malloc=mallocng",
]
configure_gen = []
depends = [
    "base-files",
    f"musl-progs~{pkgver}",
    "virtual:musl-safety-override!base-files",
]
provides = ["so:libc.so=0"]
provider_priority = 0
replaces = [f"musl~{pkgver}"]
pkgdesc = "Musl C library with malloc-ng allocator"
license = "MIT"
url = "http://www.musl-libc.org"
source = [
    f"https://git.musl-libc.org/cgit/musl/snapshot/musl-{_commit}.tar.gz",
    f"https://github.com/microsoft/mimalloc/archive/refs/tags/v{_mimalloc_ver}.tar.gz",
]
source_paths = [".", "mimalloc"]
sha256 = [
    "d3baf222d234f2121e71b7eabd0c17667b7a3733b3077e99f9920c69cb5899df",
    "8e0ed89907a681276bff2e49e9a048b47ba51254ab60daf6b3c220acac456a95",
]
compression = "deflate"
# scp makes it segfault
hardening = ["!scp"]
# does not ship tests
options = ["!check", "!lto"]


def post_extract(self):
    # reported in libc.so --version
    with open(self.cwd / "VERSION", "w") as f:
        f.write(pkgver)
    # copy in our mimalloc unified source
    self.cp(self.files_path / "mimalloc-verify-syms.sh", ".")
    self.cp(self.files_path / "mimalloc.c", "mimalloc/src")
    # now we're ready to get patched
    # but also remove musl's x86_64 asm memcpy as it's actually
    # noticeably slower than the c implementation
    self.rm("src/string/x86_64/memcpy.s")
    self.rm("src/string/x86_64/memmove.s")


def pre_install(self):
    self.install_dir("usr/lib")
    # ensure all files go in /usr/lib
    self.install_link("lib", "usr/lib")

    self.install_license("COPYRIGHT")


def post_install(self):
    # no need for the symlink anymore
    self.uninstall("lib")

    # fix up ld-musl-whatever so it does not point to absolute path
    for f in (self.destdir / "usr/lib").glob("ld-musl-*.so.1"):
        f.unlink()
        f.symlink_to("libc.so")

    # remove devel stuff provided by main package
    self.uninstall("usr/include")
    self.uninstall("usr/lib/*.o", glob=True)
    for f in (self.destdir / "usr/lib").glob("*.a"):
        if f.name == "libc.a":
            continue
        f.unlink()


@subpackage("musl-mallocng-devel-static")
def _(self):
    self.depends = [f"musl-devel~{pkgver}"]

    return ["usr/lib/libc.a"]

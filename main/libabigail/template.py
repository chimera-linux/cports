pkgname = "libabigail"
pkgver = "2.5"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--disable-apidoc",
    "--disable-ctf",
    "--disable-deb",
    "--disable-fedabipkgdiff",
    "--disable-rpm",
    "--disable-rpm415",
    "--enable-abidb",
    "--enable-bash-completion",
    "--enable-btf",
    "--enable-manual",
    "--enable-python3",  # test stuff
    "--enable-tar",
]
make_build_args = ["man"]
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "python",
    "python-sphinx",
]
makedepends = [
    "bash-completion",
    "chimerautils-devel",
    "elfutils-devel",
    "libbpf-devel",
    "libxml2-devel",
]
pkgdesc = "Library and tooling for ABI-related tasks"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0 WITH LLVM-exception"
url = "https://sourceware.org/libabigail"
source = f"https://mirrors.kernel.org/sourceware/libabigail/libabigail-{pkgver}.tar.xz"
sha256 = "7cfc4e9b00ae38d87fb0c63beabb32b9cbf9ce410e52ceeb5ad5b3c5beb111f3"
tool_flags = {
    # see libbpf comment about bpf headers
    "CFLAGS": ["-I/usr/include/bpf/uapi"],
    "CXXFLAGS": ["-I/usr/include/bpf/uapi"],
}
# CFI: fails most tests
hardening = ["vis", "!cfi"]
# FIXME: fail due to abi diff in musl headers, some bashisms, ..
options = ["!check"]


def post_install(self):
    self.do(
        "make",
        "-C",
        f"{self.make_dir}/doc/manuals",
        f"DESTDIR={self.chroot_destdir}",
        "install-man-and-info-doc",
    )
    for comp in ["abicompat", "abidiff", "abidw", "abilint", "abipkgdiff"]:
        self.install_completion(f"bash-completion/{comp}", "bash", name=comp)
    self.install_license("LICENSE.txt")


@subpackage("libabigail-devel")
def _(self):
    return self.default_devel()


@subpackage("libabigail-progs")
def _(self):
    return self.default_progs()

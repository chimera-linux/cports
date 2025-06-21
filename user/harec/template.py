pkgname = "harec"
pkgver = "0.25.2"
pkgrel = 0
archs = ["aarch64", "riscv64", "x86_64"]
build_style = "makefile"
make_build_args = [
    f"ARCH={self.profile().arch}",
    f"VERSION={pkgver}-chimera",
]
make_check_args = [*make_build_args]
depends = ["qbe"]
checkdepends = ["binutils", *depends]
pkgdesc = "Hare compiler"
license = "GPL-3.0-only"
url = "https://git.sr.ht/~sircmpwn/harec"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "e2038a6feeadcd6d4dfd7d7ab000bec91f32617720632829f5658916cd3cb17a"
tool_flags = {
    # Taken from configs/linux.mk
    "CFLAGS": ["-std=c11", "-D_XOPEN_SOURCE=700", "-Iinclude"],
}
hardening = ["vis", "cfi"]


def pre_build(self):
    self.cp("configs/linux.mk", "config.mk")

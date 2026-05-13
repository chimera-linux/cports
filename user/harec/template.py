pkgname = "harec"
pkgver = "0.26.0"
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
sha256 = "5581bc16dcf22969c7d33b0f2a9535ba37d4cf1bb39dec252e98ff2781175629"
tool_flags = {
    # Taken from configs/linux.mk
    "CFLAGS": ["-std=c11", "-D_XOPEN_SOURCE=700", "-Iinclude"],
}
hardening = ["vis", "cfi"]


def pre_build(self):
    self.cp("configs/linux.mk", "config.mk")

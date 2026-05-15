pkgname = "fortify-headers"
pkgver = "3.0.1"
pkgrel = 0
_commit = "fa01a693ae41beda27dbf0948bd30bc8b57d90fc"
build_style = "makefile"
make_check_target = "clang"
make_check_args = ["-C", "tests", "run"]
make_use_env = True
pkgdesc = "Standalone fortify implementation"
license = "0BSD"
url = "https://github.com/jvoisin/fortify-headers"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "3479b38ed29ca917cb61050fde60d2096b7a63cf911bdb92e31745cbf51dd48e"
# tool_flags = {"CFLAGS": ["-Wno-macro-redefined"]}
options = ["bootstrap"]


def build(self):
    pass

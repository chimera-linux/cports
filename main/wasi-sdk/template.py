pkgname = "wasi-sdk"
pkgver = "21"
pkgrel = 0
build_style = "meta"
depends = [
    "wasi-libc",
    "clang-rt-crt-wasi",
    "libcxx-wasi",
]
pkgdesc = "WebAssembly C/C++ toolchain"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/WebAssembly/wasi-sdk"
options = ["brokenlinks"]


def do_install(self):
    for at in ["wasm32-unknown-wasi", "wasm32-unknown-wasi-threads"]:
        # convenient cross symlinks
        self.install_dir("usr/bin")
        self.install_link(f"usr/bin/{at}-clang", "clang")
        self.install_link(f"usr/bin/{at}-clang++", "clang++")
        self.install_link(f"usr/bin/{at}-clang-cpp", "clang-cpp")
        self.install_link(f"usr/bin/{at}-cc", "cc")
        self.install_link(f"usr/bin/{at}-c++", "c++")
        # ccache cross symlinks
        self.install_dir("usr/lib/ccache/bin")
        self.install_link(
            f"usr/lib/ccache/bin/{at}-clang", "../../../bin/ccache"
        )
        self.install_link(
            f"usr/lib/ccache/bin/{at}-clang++", "../../../bin/ccache"
        )
        self.install_link(f"usr/lib/ccache/bin/{at}-cc", "../../../bin/ccache")
        self.install_link(f"usr/lib/ccache/bin/{at}-c++", "../../../bin/ccache")
        # arch config file
        with open(self.destdir / f"usr/bin/{at}.cfg", "w") as cf:
            cf.write("--sysroot /usr/wasm32-unknown-wasi\n")

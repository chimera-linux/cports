pkgname = "wasi-clang"
pkgver = "24"
pkgrel = 0
build_style = "meta"
depends = [
    "clang",
    "clang-rt-crt-wasi",
    "libcxx-wasi",
    "wasi-libc",
]
replaces = ["wasi-sdk<25"]
pkgdesc = "WebAssembly C/C++ toolchain"
subdesc = "compier symlinks"
license = "custom:none"
url = "https://github.com/WebAssembly/wasi-sdk"
options = ["brokenlinks"]


def install(self):
    for at in [
        "wasm32-wasip1",
        "wasm32-wasip1-threads",
        "wasm32-wasip2",
        "wasm32-unknown-wasip1",
        "wasm32-unknown-wasip1-threads",
        "wasm32-unknown-wasip2",
    ]:
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

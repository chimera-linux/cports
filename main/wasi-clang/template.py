pkgname = "llvm-clang-wasi"
# actually 23, but we can't set it to 23 for upgrades' sake
# TODO: do it for llvm 24
pkgver = "24"
_llvmver = 23
pkgrel = 2
build_style = "meta"
depends = [f"llvm{_llvmver}-clang-wasi"]
renames = ["wasi-clang"]
replaces = ["wasi-sdk<25"]
pkgdesc = "Clang metapackage for WebAssembly"
license = "custom:meta"
url = "https://chimera-linux.org"
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
        for binf in [
            "clang",
            "clang++",
            "clang-cpp",
            "cc",
            "c++",
        ]:
            self.install_link(f"usr/bin/{at}-{binf}", f"{at}-{binf}-{_llvmver}")
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

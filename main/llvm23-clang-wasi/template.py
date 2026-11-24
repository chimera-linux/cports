pkgname = "llvm23-clang-wasi"
pkgver = "23.1.6"
_llvm_majver = pkgver[0:2]
pkgrel = 1
build_style = "meta"
depends = [
    f"llvm{_llvm_majver}-clang-rt-crt-wasi",
    f"virtual:llvm-runtimes-wasi!llvm{_llvm_majver}-runtimes-wasi",
]
pkgdesc = "Clang metapackage for WebAssembly - 23.x"
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
        pfx = f"usr/lib/llvm{_llvm_majver}"
        self.install_dir("usr/bin")
        self.install_dir(f"{pfx}/bin")
        for binf in [
            "clang",
            "clang++",
            "clang-cpp",
            "cc",
            "c++",
        ]:
            self.install_link(f"{pfx}/bin/{at}-{binf}", binf)
            self.install_link(
                f"usr/bin/{at}-{binf}-{_llvm_majver}",
                f"../lib/llvm{_llvm_majver}/bin/{binf}",
            )
        # ccache cross symlinks
        self.install_dir("usr/lib/ccache/bin")
        self.install_link(
            f"usr/lib/ccache/bin/{at}-clang-{_llvm_majver}",
            "../../../bin/ccache",
        )
        self.install_link(
            f"usr/lib/ccache/bin/{at}-clang++-{_llvm_majver}",
            "../../../bin/ccache",
        )
        self.install_link(
            f"usr/lib/ccache/bin/{at}-cc-{_llvm_majver}", "../../../bin/ccache"
        )
        self.install_link(
            f"usr/lib/ccache/bin/{at}-c++-{_llvm_majver}", "../../../bin/ccache"
        )
        # arch config file
        with open(self.destdir / f"{pfx}/bin/{at}.cfg", "w") as cf:
            cf.write("--sysroot /usr/wasm32-unknown-wasi\n")

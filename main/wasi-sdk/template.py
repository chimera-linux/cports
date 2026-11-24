pkgname = "wasi-sdk"
pkgver = "24"
pkgrel = 2
build_style = "meta"
depends = [
    "llvm-clang-wasi",
    "wasm-component-ld",
]
pkgdesc = "WebAssembly C/C++ toolchain"
license = "Apache-2.0"
url = "https://github.com/WebAssembly/wasi-sdk"
options = ["brokenlinks"]

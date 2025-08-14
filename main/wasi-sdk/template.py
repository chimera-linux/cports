pkgname = "wasi-sdk"
pkgver = "24"
pkgrel = 1
build_style = "meta"
depends = [
    "wasi-clang",
    "wasm-component-ld",
]
pkgdesc = "WebAssembly C/C++ toolchain"
license = "Apache-2.0"
url = "https://github.com/WebAssembly/wasi-sdk"
options = ["brokenlinks"]

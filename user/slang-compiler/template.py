pkgname = "slang-compiler"
pkgver = "2026.20"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DSLANG_ENABLE_DXIL=FALSE",
    "-DSLANG_SLANG_LLVM_FLAVOR=USE_SYSTEM_LLVM",
    "-DSLANG_INSTALL_USER_SKILLS=OFF",
    "-DSLANG_RHI_ENABLE_OPTIX=OFF",
    "-DSLANG_USE_SYSTEM_VULKAN_HEADERS=TRUE",
    "-DSLANG_USE_SYSTEM_SPIRV_HEADERS=TRUE",
    "-DSLANG_USE_SYSTEM_SPIRV_TOOLS=TRUE",
    "-DSLANG_USE_SYSTEM_LZ4=TRUE",
    "-DSLANG_USE_SYSTEM_GLSLANG=TRUE",
    "-DSLANG_ENABLE_PCH=FALSE",
    "-DSLANG_ENABLE_GFX=FALSE",
]
hostmakedepends = [
    "clang-devel",
    "cmake",
    "glslang-progs",
    "llvm-devel",
    "ninja",
    "pkgconf",
    "python",
    "spirv-tools-devel",
    "zlib-ng-compat-devel",
]
makedepends = [
    "glm",
    "glslang-devel",
    "lz4-devel-static",
    "nlohmann-json",
    "spirv-headers",
    "spirv-tools-devel",
    "vulkan-headers",
]
depends = ["spirv-tools", f"{pkgname}-libs"]
pkgdesc = "Compiler for the slang-shader language"
license = "Apache-2.0 WITH LLVM-exception"
url = "https://shader-slang.org"
source = [
    f"https://github.com/shader-slang/slang/archive/refs/tags/v{pkgver}.tar.gz",
    "https://github.com/martinus/unordered_dense/archive/73f3cbb237e84d483afafc743f1f14ec53e12314.tar.gz",
    "https://github.com/richgel999/miniz/archive/6ef6c68f4fcbb8287aa8edf9c6670804932f41c6.tar.gz",
    "https://github.com/swiftlang/swift-cmark/archive/924936d0427cb25a61169739a7660230bffa6ea6.tar.gz",
    "https://github.com/shader-slang/slang-rhi/archive/b856e6350ea09f63a16a6c7497faa1d741fdd735.tar.gz",
    "https://github.com/fastfloat/fast_float/archive/e0b53eaf63c6d00e0725788ef1dbb759aa321d79.tar.gz",
    "https://github.com/lua/lua/archive/3fe7be956f23385aa1950dc31e2f25127ccfc0ea.tar.gz",
    "https://github.com/tinyobjloader/tinyobjloader/archive/d541711a794343de4ef5ea76f037c9fb9c127a55.tar.gz",
    "https://github.com/ocornut/imgui/archive/8936b58fe26e8c3da834b8f60b06511d537b4c63.tar.gz",
]

source_paths = [
    ".",
    "external/unordered_dense",
    "external/miniz",
    "external/cmark",
    "external/slang-rhi",
    "external/fast_float",
    "external/lua",
    "external/tinyobjloader",
    "external/imgui",
]
sha256 = [
    "f58bda28ae5ad57e098b1b028d03b0ef466bb70b7d4f9fe266722938ec6453cb",
    "16188ed4804a670f6b00637a53e135190668dddc12b10f5233e20b403b9df9e2",
    "d9ef3c09f98b0dba3aa60e520284ed54042b0baa86116312be3f36e26393ae27",
    "1c51659bd47c34df1c8976f893adc43ba039a98f6eac4fa95d53d1e08ba6072a",
    "4c629dc48692fadfdb9dccaa035b18bf85573a1462094823f0078d7577f64c71",
    "f6259a3543e75ae705ec80835d1568622b444d389922dcc314af7250c26e8643",
    "4776526f89abeea61cce41a056577859180dbb2d4cb6c1dad00955872a1007bb",
    "95d14866c083640365245a3241b421c0bbad5c9d7c816bb2cbd61a00ff4d40be",
    "a1e4443190d78976e0901039dd2207e1d59a4b5b818489232568bdb69ff79ce6",
]
hardening = []


@subpackage("slang-compiler-libs")
def _(self):
    return self.default_libs()


@subpackage("slang-compiler-devel")
def _(self):
    return self.default_devel()
